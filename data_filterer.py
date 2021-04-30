import time
from functools import reduce
from typing import List

import numpy as np
import pandas as pd

from data_loader import DataLoader
from resources.constants import Constants


class DataFilterer:
    @staticmethod
    def _filter_conditions(inputs) -> List:
        match_age = DataLoader.loaded_data[Constants.PATIENT_ALDER].isin(
            range(inputs["age"]["min"], inputs["age"]["max"] + 1)
        )

        # match_op_time = LoadedData.loaded_data[Constants.OP_TID].isin(
        #     range(inputs["op_time"]["min"], inputs["op_time"]["max"] + 1)
        # )

        # match_asa = (
        #     True
        #     if inputs["asa_radio"] == "Visa alla"
        #     else (
        #         (
        #             LoadedData.loaded_data[Constants.ASA_KLASS].isin(inputs["asa"])
        #             if inputs["asa"]
        #             else True
        #         )
        #         | (
        #             LoadedData.loaded_data[Constants.ASA_KLASS].isna()
        #             if ("Saknas" in inputs["asa"])
        #             else False
        #         )
        #     )
        # )

        match_stat_code = (
            True
            if inputs["stat_code_radio"] == "Visa alla"
            else (
                DataLoader.loaded_data[Constants.PRIORITET].isin(inputs["stat_code"])
                if inputs["stat_code"]
                else True
            )
        )

        match_op_code = (
            DataLoader.loaded_data[Constants.BENAMNING].isin(inputs["op_code"])
            if inputs["op_code"]
            else True
        )

        match_care_type = (
            DataLoader.loaded_data[Constants.VARDFORM].isin([inputs["caretype"]])
            if inputs["caretype"] and inputs["caretype"] != "Alla"
            else True
        )

        def _does_operator_match(inputs):
            series = DataLoader.loaded_data[Constants.PLANERAD_OPERATOR]

            selection = inputs["operator_radio"]
            operators = inputs["assigned_to_operator"]
            include_unassigned = inputs["operator_include_unassigned"]

            if selection == "all":
                return True
            elif selection == "blank":
                return series.isna()
            elif selection == "operator" and operators is not None:
                matched_operator = series.isin(operators)
                no_operator = series.isna()
                return (
                    matched_operator | no_operator
                    if include_unassigned
                    else matched_operator
                )

            return True

        match_operator = _does_operator_match(inputs)

        conditions = []
        conditions.extend(
            [
                match_age,
                # match_op_time,
                # match_asa,
                match_stat_code,
                match_op_code,
                match_care_type,
                match_operator,
            ]
        )

        return conditions

    @staticmethod
    def _filter_vectorized(inputs) -> pd.DataFrame:
        start_time = time.time()
        print(inputs)
        conditions = DataFilterer._filter_conditions(inputs)
        filtered = np.where(reduce(lambda a, b: a & b, conditions))
        data = DataLoader.loaded_data.iloc[filtered].to_dict("records")
        print("---Filtering took %s seconds ---" % (time.time() - start_time))
        return data

    @staticmethod
    def search_data(inputs) -> dict:
        # Alternative solution for exception? Only thrown in one case but i want to avoid several if statements

        filtered_data = DataFilterer._filter_vectorized(inputs)
        search_result = {
            "data": filtered_data,
            "number_of_patients": f"Antal patienter: {len(filtered_data)} / {DataLoader.patient_count}",
        }
        return search_result
