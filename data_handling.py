import base64
import datetime
import io
import time
from datetime import timedelta
from functools import reduce
from typing import List

import numpy as np
import pandas as pd


class DataFilterer:
    @staticmethod
    def _filter_conditions(inputs) -> List:
        match_age = LoadedData.loaded_data["PatientÅlderVidOp"].isin(
            range(inputs["age"]["min"], inputs["age"]["max"] + 1)
        )

        match_op_time = LoadedData.loaded_data["KravOperationstidMinuter"].isin(
            range(inputs["op_time"]["min"], inputs["op_time"]["max"] + 1)
        )

        match_asa = (
            True
            if inputs["asa_radio"] == "Visa alla"
            else (
                (
                    LoadedData.loaded_data["ASAklass"].isin(inputs["asa"])
                    if inputs["asa"]
                    else True
                )
                | (
                    LoadedData.loaded_data["ASAklass"].isna()
                    if ("Saknas" in inputs["asa"])
                    else False
                )
            )
        )

        match_stat_code = (
            True
            if inputs["stat_code_radio"] == "Visa alla"
            else (
                LoadedData.loaded_data["Statistikkod"].isin(inputs["stat_code"])
                if inputs["stat_code"]
                else True
            )
        )

        match_op_code = (
            LoadedData.loaded_data["OpkortText"].isin(inputs["op_code"])
            if inputs["op_code"]
            else True
        )

        match_care_type = (
            LoadedData.loaded_data["Vårdform_text"].isin([inputs["caretype"]])
            if inputs["caretype"] and inputs["caretype"] != "Alla"
            else True
        )

        conditions = []
        conditions.extend(
            [
                match_age,
                match_op_time,
                match_asa,
                match_stat_code,
                match_op_code,
                match_care_type,
            ]
        )

        return conditions

    @staticmethod
    def _filter_vectorized(inputs) -> pd.DataFrame:
        start_time = time.time()
        print(inputs)
        conditions = DataFilterer._filter_conditions(inputs)
        filtered = np.where(reduce(lambda a, b: a & b, conditions))
        data = LoadedData.loaded_data.iloc[filtered].to_dict("records")
        print("---Filtering took %s seconds ---" % (time.time() - start_time))
        return data

    @staticmethod
    def search_data(inputs) -> dict:
        # Alternative solution for exception? Only thrown in one case but i want to avoid several if statements

        filtered_data = DataFilterer._filter_vectorized(inputs)
        search_result = {
            "data": filtered_data,
            "number_of_patients": f"Antal patienter: {len(filtered_data)} / {LoadedData.patient_count}",
        }
        return search_result


class LoadedData:
    # Class stores loaded data and information about it, ex number of patients

    # Necessary because callbacks will try to search when program is built, key error exception will be thrown,
    # this is a temp fix
    COLUMNS = [
        "Behandlingsnr",
        "Anmälningstidpunkt",
        "SistaOpTidpunkt",
        "Opkategori_text",
        "Prioritet_dagar",
        "ASAklass",
        "KravOperationstidMinuter",
        "KravFörberedelsetidMinuter",
        "KravtidEfterMinuter",
        "De_PlaneradOpsal_FK",
        "PlaneradStartOpsalTidpunkt",
        "PatientÅlderVidOp",
        "Veckodag",
        "Starttimme",
        "TotaltidStart",
        "Vårdform_text",
        "Statistikkod",
        "OpkortText",
        "Kvar på prio-tid",
    ]
    loaded_data = pd.DataFrame(columns=COLUMNS)
    patient_count = 0

    @staticmethod
    def load_data(filename, content):
        if filename.endswith(".csv"):
            data = content.split(",")[1]
            data = pd.read_csv(
                io.StringIO(base64.b64decode(data).decode("utf-8")), sep=";"
            )  # Data loaded by widget is wrong "format", cant access full path.
            LoadedData.loaded_data = data
            LoadedData._update_patient_count()
            LoadedData._add_prio_days_left_col()

    @staticmethod
    def _update_patient_count():
        LoadedData.patient_count = len(LoadedData.loaded_data.values.tolist())

    @staticmethod
    def _prio_days_left(booked_date, prio_days):
        """
        Calculate days left within the patients priority days
        """
        today = datetime.date.today()
        year, month, day = str(booked_date).split(sep="-")
        booked_date = datetime.date(int(year), int(month), int(day.split(" ")[0]))
        critical_date = booked_date + timedelta(prio_days)
        return (critical_date - today).days

    @staticmethod
    def _add_prio_days_left_col():
        """
        Atm just adds a column with calculated values from _prio_days_left,
        expand later to initialize "global" dataframe with the import data widget and
        use to add more columns if needed
        """
        LoadedData.loaded_data["Kvar på prio-tid"] = LoadedData.loaded_data.apply(
            lambda x: LoadedData._prio_days_left(
                x["Anmälningstidpunkt"], x["Prioritet_dagar"]
            ),
            axis=1,
        )

    @staticmethod
    def _get_unique_values(col):
        return LoadedData.loaded_data[col].unique().tolist()

    @staticmethod
    def get_unique_label_values(col_name):
        label_values = [
            {"label": code, "value": code}
            for code in LoadedData._get_unique_values(col_name)
        ]
        return label_values
