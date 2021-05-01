import base64
import io
import re

import pandas as pd

from resources.constants import Constants


class DataLoader:
    # Class stores loaded data and information about it, ex number of patients

    # Necessary because callbacks will try to search when program is built, key error exception will be thrown,
    # this is a temp fix
    CORRECT_FILE_TYPE = ".xls"
    COLUMNS = [
        Constants.BEHANDLINGS_NUMMER,
        Constants.ANM_TIDPUNKT,
        # Constants.OP_KATEGORI,
        Constants.ASA_KLASS,
        Constants.OP_TID,
        Constants.PATIENT_ALDER,
        # Constants.VECKODAG,
        Constants.VARDFORM,
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
            data = pd.read_excel(io.BytesIO(decoded), usecols=DataLoader.COLUMNS)
            DataLoader.loaded_data = data

            DataLoader._update_patient_count()
            DataLoader._add_prio_days_left_col()
            DataLoader._add_desirous_status()
            DataLoader._strip_age()
            DataLoader._convert_time()
            DataLoader._parse_op_code()

    @staticmethod
    def _update_patient_count():
        DataLoader.patient_count = len(DataLoader.loaded_data.values.tolist())

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
        DataLoader.loaded_data["Kvar på prio-tid"] = DataLoader.loaded_data.apply(
            lambda x: DataLoader._prio_days_left(
                x[Constants.ANM_TIDPUNKT], x[Constants.PRIORITET]
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

        DataLoader.loaded_data["angelägen"] = DataLoader.loaded_data[
            Constants.INFO_TILL_PLANERARE
        ].map(lambda x: _is_desirious(x))

    @staticmethod
    def _get_unique_values(col):
        return DataLoader.loaded_data[col].dropna().unique().tolist()

    @staticmethod
    def get_unique_label_values(col_name):
        label_values = [
            {"label": code, "value": code}
            for code in DataLoader._get_unique_values(col_name)
        ]
        return label_values

    @staticmethod
    def find_patient(treatment_nr):
        return DataLoader.loaded_data.loc[
            (DataLoader.loaded_data[Constants.BEHANDLINGS_NUMMER] == int(treatment_nr))
        ]

    @staticmethod
    def patient_to_string(patient_row):
        pid_nr, name = DataLoader._extract_pnr_name(
            patient_row[Constants.PATIENT].values[0]
        )
        patient_age = patient_row[Constants.PATIENT_ALDER].values[0]
        treatment_nr = patient_row[Constants.BEHANDLINGS_NUMMER].values[0]
        operation_time = patient_row[Constants.OP_TID].values[0]
        operator = patient_row[Constants.PLANERAD_OPERATOR].values[0]
        operation_code = patient_row[Constants.BENAMNING].values[0]
        priority = patient_row[Constants.PRIORITET].values[0]
        asa_class_doctor = patient_row[Constants.ASA_KLASS].values[0]
        asa_class_info = DataLoader.extract_asa_class(
            patient_row[Constants.INFO_TILL_PLANERARE].values[0]
        )

        patient_details_string = (
            f"Namn: {name} \n"
            f"Personnummer: {pid_nr} \n"
            f"Behandlingsnummer: {treatment_nr} \n"
            f"Operationstid: {operation_time} \n"
            f"Operatör: {operator} \n"
            f"Operationskod: {operation_code} \n"
            f"Ålder: {patient_age} \n"
            f"Statistikkod: {priority} \n"
            f"ASA-klass (Info till pl.): {asa_class_info} \n"
            f"ASA-klass (Läkare): {asa_class_doctor}"
        )

        return patient_details_string

    @staticmethod
    def _strip_age():
        DataLoader.loaded_data[Constants.PATIENT_ALDER] = DataLoader.loaded_data[
            Constants.PATIENT_ALDER
        ].map(lambda x: DataLoader._string_to_age(x))

    @staticmethod
    def _string_to_age(age: str):
        if type(age) == str:
            return int(age.split()[0])
        return 0

    @staticmethod
    def _convert_time():
        DataLoader.loaded_data[Constants.OP_TID] = DataLoader.loaded_data[
            Constants.OP_TID
        ].map(lambda x: DataLoader._time_to_minutes(x))

    @staticmethod
    def _time_to_minutes(time: str):
        h, m = time.split(":")
        return int(h) * 60 + int(m)

    @staticmethod
    def _parse_op_code():
        DataLoader.loaded_data[Constants.BENAMNING] = DataLoader.loaded_data[
            Constants.BENAMNING
        ].map(lambda x: DataLoader._split_op_code(x))

    @staticmethod
    def _split_op_code(op_code):
        if op_code is not None:
            return op_code.split()[0]
        return ""

    @staticmethod
    def _extract_pnr_name(string: str) -> (str, str):
        if type(string) is not str:
            return "", ""

        pnr = re.findall(r"^[0-9]{8}-[0-9]{4}", string)
        name = re.findall(r"(?<=^[0-9]{8}-[0-9]{4} - ).*", string)
        # TODO: Handle no found match
        return pnr[0], name[0]

    @staticmethod
    def extract_asa_class(string: str):
        if type(string) is not str:
            return None

        number = re.findall(r"(?<=[Aa][Ss][Aa] )[1-4]", string)
        return int(number[0]) if number else None
