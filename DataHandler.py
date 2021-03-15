import pandas as pd
import time

# TODO ta bort dumma kommentarer
# TODO gör evaluering av

dummy_data = pd.read_csv("data.csv", sep=";")


def filter_data(data, inputs=None):
    inputs = {  # Genom att ta in ett dicitonary som detta kan man skapa kombinationer som därmed kan sökas efter specifikt, kan låta användaren skapa "genvägar"/spara filtrering för att jämföra resultat
        "age": [0, 2],
        "asa": ["asa1", "es"],
    }
    passed = []
    data = data.to_dict("records")
    for row in data:
        if _run_filters(inputs, row):
            passed.append(row)


def _run_filters(inputs, row):
    filter_functions = [_eval_age, _eval_asa]
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
    # print("Minimum age: {} | Maximum age: {} | Patient age: {} | Passed filter {} ".format(min_age, max_age, age, (age >= min_age and age <= max_age)))
    if age >= min_age and age <= max_age:
        return True
    return False


def _eval_asa(inputs, row):
    value_map = {
        "asa1": 1,
        "asa2": 2,
        "asa3": 3,
        "asa4": 4,
        "asa5": 5,
        "asa6": 6,
        "es": None,
    }

    if ("es" in inputs["asa"]) and pd.isna(row["ASAklass"]):
        return True
    passable = [value_map[input] for input in inputs["asa"]]
    return row["ASAklass"] in passable


start_time = time.time()
filter_data(dummy_data)
print("--- %s seconds ---" % (time.time() - start_time))
