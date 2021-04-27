import base64
import datetime
import io
import time
from datetime import timedelta
from functools import reduce
from typing import List
from resources.constants import Constants
import numpy as np
import pandas as pd


class DataFilterer:
    @staticmethod
    def _filter_conditions(inputs) -> List:
        match_age = LoadedData.loaded_data[Constants.PATIENT_ALDER].isin(
            range(inputs["age"]["min"], inputs["age"]["max"] + 1)
        )

        match_op_time = LoadedData.loaded_data[Constants.OP_TID].isin(
            range(inputs["op_time"]["min"], inputs["op_time"]["max"] + 1)
        )

        """match_asa = (
            True
            if inputs["asa_radio"] == "Visa alla"
            else (
                (
                    LoadedData.loaded_data[Constants.ASA_KLASS].isin(inputs["asa"])
                    if inputs["asa"]
                    else True
                )
                | (
                    LoadedData.loaded_data[Constants.ASA_KLASS].isna()
                    if ("Saknas" in inputs["asa"])
                    else False
                )
            )
        )"""

        match_stat_code = (
            True
            if inputs["stat_code_radio"] == "Visa alla"
            else (
                LoadedData.loaded_data[Constants.PRIORITET].isin(inputs["stat_code"])
                if inputs["stat_code"]
                else True
            )
        )

        match_op_code = (
            LoadedData.loaded_data[Constants.BENAMNING].isin(inputs["op_code"])
            if inputs["op_code"]
            else True
        )

        """match_care_type = (
            LoadedData.loaded_data[Constants.VARDFORM].isin([inputs["caretype"]])
            if inputs["caretype"] and inputs["caretype"] != "Alla"
            else True
        )"""

        conditions = []
        conditions.extend(
            [
                match_age,
                match_op_time,
                # match_asa,
                match_stat_code,
                match_op_code,
                # match_care_type,
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
        Constants.BEHANDLINGS_NUMMER,
        Constants.ANM_TIDPUNKT,
        # Constants.OP_KATEGORI,
        Constants.PRIORITET_DAGAR,
        Constants.ASA_KLASS,
        Constants.OP_TID,
        Constants.PATIENT_ALDER,
        # Constants.VECKODAG,
        # Constants.VARDFORM,
        Constants.PRIORITET,
        Constants.BENAMNING,
        # Constants.KVAR_PRIO_TID,
        Constants.PLANERAD_OPERATOR,
        Constants.INFO_TILL_PLANERARE,
        Constants.PATIENT,
        Constants.STAT_CODE,
    ]

    loaded_data = pd.DataFrame(columns=COLUMNS)
    patient_count = 0

    @staticmethod
    def load_data(filename, contents):
        content_type, content_string = contents.split(",")
        decoded = base64.b64decode(content_string)
        if ".xls" in filename:
            data = pd.read_excel(io.BytesIO(decoded), usecols=LoadedData.COLUMNS)
            LoadedData.loaded_data = data

            LoadedData._update_patient_count()
            LoadedData._add_prio_days_left_col()
            LoadedData._add_desirous_status()
            LoadedData._strip_age()
            LoadedData._convert_time()
            LoadedData._parse_op_code()

    @staticmethod
    def _update_patient_count():
        LoadedData.patient_count = len(LoadedData.loaded_data.values.tolist())

    @staticmethod
    def _prio_days_left(booked_date, prio_days):
        """
        Calculate days left within the patients priority days
        """
        # today = datetime.date.today()
        # year, month, day = str(booked_date).split(sep="-")
        # booked_date = datetime.date(int(year), int(month), int(day.split(" ")[0]))
        # critical_date = booked_date + timedelta(prio_days)
        return 1  # (critical_date - today).days

    @staticmethod
    def _add_prio_days_left_col():
        """
        Atm just adds a column with calculated values from _prio_days_left,
        expand later to initialize "global" dataframe with the import data widget and
        use to add more columns if needed
        """
        LoadedData.loaded_data["Kvar på prio-tid"] = LoadedData.loaded_data.apply(
            lambda x: LoadedData._prio_days_left(
                x[Constants.ANM_TIDPUNKT], x[Constants.PRIORITET_DAGAR]
            ),
            axis=1,
        )

    @staticmethod
    def _add_desirous_status():
        def _is_desirious(s):
            if type(s) is str:
                desirious = s.lower().find("angelägen")
                return False if desirious < 0 else True
            return False

        LoadedData.loaded_data["angelägen"] = LoadedData.loaded_data[
            Constants.INFO_TILL_PLANERARE
        ].map(lambda x: _is_desirious(x))

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

    @staticmethod
    def find_patient(treatment_nr):
        return LoadedData.loaded_data.loc[
            (LoadedData.loaded_data[Constants.BEHANDLINGS_NUMMER] == int(treatment_nr))
        ]

    @staticmethod
    def patient_to_string(patient_row, detailed=True):

        return (
            f"Namn: David \n"
            f"Behandlingsnummer: {patient_row[Constants.BEHANDLINGS_NUMMER].values[0]} \n"
            f"Operationstid: {patient_row[Constants.OP_TID].values[0]} \n"
            f"Operatör: {patient_row[Constants.PLANERAD_OPERATOR].values[0]} \n"
            f"Operationskod: {patient_row[Constants.BENAMNING].values[0]} \n"
            f"Ålder: {patient_row[Constants.PATIENT_ALDER].values[0]} \n"
            f"Statistikkod: {patient_row[Constants.PRIORITET].values[0]} \n"
            f"ASA-klass : {patient_row[Constants.ASA_KLASS].values[0]} \n"
        )

    @staticmethod
    def _strip_age():
        LoadedData.loaded_data[Constants.PATIENT_ALDER] = LoadedData.loaded_data[
            Constants.PATIENT_ALDER
        ].map(lambda x: LoadedData._string_to_age(x))

    @staticmethod
    def _convert_time():
        LoadedData.loaded_data[Constants.OP_TID] = LoadedData.loaded_data[
            Constants.OP_TID
        ].map(lambda x: LoadedData._time_to_minutes(x))

    @staticmethod
    def _time_to_minutes(time: str):
        print(time)
        h, m = time.split(":")
        return int(h) * 60 + int(m)

    @staticmethod
    def _string_to_age(age: str):
        if type(age) == str:
            return int(age.split()[0])
        return 0

    @staticmethod
    def _parse_op_code():
        LoadedData.loaded_data[Constants.BENAMNING] = LoadedData.loaded_data[
            Constants.BENAMNING
        ].map(lambda x: LoadedData._split_op_code(x))

    @staticmethod
    def _split_op_code(op_code):
        if op_code is not None:
            return op_code.split()[0]
        return ""
