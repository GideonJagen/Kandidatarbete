from functools import reduce
from typing import List
import pandas as pd
import time
import numpy as np
from datetime import timedelta
import datetime


class DataHandler:
    df = pd.read_csv("output.csv", sep=";")

    @staticmethod
    def _filter_conditions(inputs) -> List:
        """
        Make that each of the inputs values are handled as individual conditions
        """
        conditions = []

        # Add the conditions to the list of conditions
        conditions.extend(
            (
                # Check if patient is in right age interval
                DataHandler.df["PatientÅlderVidOp"].isin(
                    range(inputs["age"]["min"], inputs["age"]["max"])
                ),
                # Check if patient is in right time interval
                DataHandler.df["KravOperationstidMinuter"].isin(
                    range(inputs["op_time"]["min"], inputs["op_time"]["max"])
                ),
                # Check if patient is in right ASA class
                (
                    DataHandler.df["ASAklass"].isin(inputs["asa"])
                    if inputs["asa"]
                    else True
                )
                | (
                    DataHandler.df["ASAklass"].isna()
                    if (-1 in inputs["asa"])
                    else False
                ),
                # Check if operation has matching statistcal code
                DataHandler.df["Statistikkod"].isin(inputs["stat_code"])
                if inputs["stat_code"]
                else True,
                # Check if operation has matching operation code
                DataHandler.df["OpkortText"].isin(inputs["op_code"])
                if inputs["op_code"]
                else True,
            )
        )

        return conditions

    @staticmethod
    def filter_vectorized(inputs) -> pd.DataFrame:
        start_time = time.time()
        print(inputs)

        conditions = DataHandler._filter_conditions(inputs)

        filtered = np.where(reduce(lambda a, b: a & b, conditions))

        data = DataHandler.df.iloc[filtered].to_dict("records")
        print("---Filtering took %s seconds ---" % (time.time() - start_time))
        return data

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
    def init_data():
        """
        Atm just adds a column with calculated values from _prio_days_left,
        expand later to initialize "global" dataframe with the import data widget and
        use to add more columns if needed
        """

        DataHandler.df["dagar_till_kritisk"] = DataHandler.df.apply(
            lambda x: DataHandler._prio_days_left(
                x["Anmälningstidpunkt"], x["Prioritet_dagar"]
            ),
            axis=1,
        )
