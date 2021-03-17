from functools import reduce
from typing import List

import pandas as pd
import time
import numpy as np

# TODO Söka efter förberedelsetid?

dummy_data = pd.read_csv("output.csv", sep=";")


def filter_data(inputs=None):
    start_time = time.time()
    data = dummy_data
    passed = []
    data = data.to_dict("records")
    for row in data:
        if _run_filters(inputs, row):
            passed.append(row)
    print("---Filtering took %s seconds ---" % (time.time() - start_time))
    return passed


def _run_filters(inputs, row):
    filter_functions = [_eval_age, _eval_asa, _eval_op_time]
    for func in filter_functions:
        if not func(inputs, row):
            return False
    return True


def _eval_age(inputs, row):
    value_map = {  # Translation of values from age widget
        # Magic numbers, find other solution?
        # Function vid widgeten som gör detta?
        0: 0,
        2: 16,
        8: 80,
        10: 150,
    }
    age_invl = inputs["age"]
    age = row["PatientÅlderVidOp"]
    min_age = value_map[age_invl[0]]
    max_age = value_map[age_invl[1]]
    # print("Minimum age: {} | Maximum age: {} | Patient age: {} | Passed filter {} ".format(min_age, max_age, age,
    # (age >= min_age and age <= max_age)))
    if min_age <= age <= max_age:
        return True
    return False


def _eval_asa(inputs, row):
    if len(inputs["asa"]) == 0:  # If none selected, all are passed
        return True
    value_map = {
        "asa1": 1,
        "asa2": 2,
        "asa3": 3,
        "asa4": 4,
        "asa5": 5,
        "asa6": 6,
        "es": -1,
    }
    if ("es" in inputs["asa"]) and pd.isna(row["ASAklass"]):
        return True
    passable = [value_map[input] for input in inputs["asa"]]
    return row["ASAklass"] in passable


def _eval_op_time(inputs, row):
    min_time = inputs["op_time"][0]
    max_time = inputs["op_time"][1]
    return min_time <= row["KravOperationstidMinuter"] <= max_time


def filter_conditions(inputs) -> List:
    """
    Make that each of the inputs values are handled as individual conditions
    """
    conditions = []
    df = dummy_data

    # Add the conditions to the list of conditions
    conditions.extend(
        (
            # Är op patients ålder i rätt intervall?
            df["PatientÅlderVidOp"].isin(
                range(inputs["age"]["min"], inputs["age"]["max"])
            ),
            # Är op tidsåtgång i rätt intervall?
            df["KravOperationstidMinuter"].isin(
                range(inputs["op_time"]["min"], inputs["op_time"]["max"])
            ),
            # Är op ASA klass en match?
            (df["ASAklass"].isin(inputs["asa"]) if inputs["asa"] else True)
            | (df["ASAklass"].isna() if (-1 in inputs["asa"]) else False),
            # Har op matchande statistikkod?
            df["Statistikkod"].isin(inputs["stat_code"])
            if inputs["stat_code"]
            else True,
            # Har op matchande operationskod?
            df["OpkortText"].isin(inputs["op_code"]) if inputs["op_code"] else True,
        )
    )

    return conditions


def filter_vectorized(inputs) -> pd.DataFrame:
    start_time = time.time()
    df = dummy_data
    print(inputs)

    conditions = filter_conditions(inputs)

    filtered = np.where(reduce(lambda a, b: a & b, conditions))

    data = df.iloc[filtered].to_dict("records")
    print("---Filtering took %s seconds ---" % (time.time() - start_time))
    return data
