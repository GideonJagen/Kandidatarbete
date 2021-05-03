class Constants:
    BEHANDLINGS_NUMMER = "Behandlingsnr"
    PATIENT = "Patient"
    ANM_TIDPUNKT = "Anmälningsdatum"
    OP_KATEGORI = "Opkategori_text"
    ASA_KLASS = "ASA-klassificering (preoperativt)"
    OP_TID = "Operationstid"  # Change to "Operationstid" column name
    PATIENT_ALDER = "Patient (Ålder)"
    VECKODAG = "Veckodag"
    VARDFORM = "Vårdform"
    PRIORITET = "Prioritet"
    STAT_CODE = "Statistikkod (Ange vilken/vilka)"
    BENAMNING = "Benämning"
    KVAR_PRIO_TID = "Kvar på prio-tid"
    PLANERAD_OPERATOR = "Planerade operatörer (Ansvarig)"
    INFO_TILL_PLANERARE = "Information till planerare/koordinator"
    KOMMUN = "Patient (Kommun)"  # ???

    @staticmethod
    def get_all_columns():
        return [
            Constants.BEHANDLINGS_NUMMER,
            Constants.ANM_TIDPUNKT,
            # Constants.SISTA_OP_TIDPUNKT,
            Constants.OP_KATEGORI,
            # Constants.PRIORITET_DAGAR,
            Constants.ASA_KLASS,
            Constants.OP_TID,
            Constants.PATIENT_ALDER,
            Constants.VECKODAG,
            Constants.VARDFORM,
            Constants.PRIORITET,
            Constants.BENAMNING,
            Constants.KVAR_PRIO_TID,
            Constants.PLANERAD_OPERATOR,
            Constants.PATIENT,
        ]
