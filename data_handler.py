from functools import reduce
from typing import List
import pandas as pd
import time
import numpy as np


class DataHandler:
    df = pd.read_csv("output.csv", sep=";")

    @staticmethod
    def filter_conditions(inputs) -> List:
        """
        Make that each of the inputs values are handled as individual conditions
        """
        conditions = []

        # Add the conditions to the list of conditions
        conditions.extend(
            (
                # Är op patients ålder i rätt intervall?
                DataHandler.df["PatientÅlderVidOp"].isin(
                    range(inputs["age"]["min"], inputs["age"]["max"])
                ),
                # Är op tidsåtgång i rätt intervall?
                DataHandler.df["KravOperationstidMinuter"].isin(
                    range(inputs["op_time"]["min"], inputs["op_time"]["max"])
                ),
                # Är op ASA klass en match?
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
                # Har op matchande statistikkod?
                DataHandler.df["Statistikkod"].isin(inputs["stat_code"])
                if inputs["stat_code"]
                else True,
                # Har op matchande operationskod?
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

        conditions = DataHandler.filter_conditions(inputs)

        filtered = np.where(reduce(lambda a, b: a & b, conditions))

        data = DataHandler.df.iloc[filtered].to_dict("records")
        print("---Filtering took %s seconds ---" % (time.time() - start_time))
        return data
