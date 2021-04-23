class Constants:
    BEHANDLINGS_NUMMER = "Behandlingsnr"
    ANM_TIDPUNKT = "Anmälningstidpunkt"
    SISTA_OP_TIDPUNKT = "SistaOpTidpunkt"
    OP_KATEGORI = "Opkategori_text"
    PRIORITET_DAGAR = "Prioritet_dagar"
    ASA_KLASS = "ASAklass"
    OP_TID = "KravOperationstidMinuter"  # Change to "Operationstid" column name
    PATIENT_ALDER = "PatientÅlderVidOp"
    VECKODAG = "Veckodag"
    VARDFORM = "Vårdform_text"
    STAT_KOD = "Statistikkod"
    OP_KORT = "OpkortText"
    KVAR_PRIO_TID = "Kvar på prio-tid"
    PLANERAD_OPERATOR = "Planerade operatörer (Ansvarig)"
    INFO_TILL_PLANERARE = "Information till planerare/koordinator"
    KOMMUN = "kommun"  # ???

    @staticmethod
    def get_all_columns():
        return [
            Constants.BEHANDLINGS_NUMMER,
            Constants.ANM_TIDPUNKT,
            Constants.SISTA_OP_TIDPUNKT,
            Constants.OP_KATEGORI,
            Constants.PRIORITET_DAGAR,
            Constants.ASA_KLASS,
            Constants.OP_TID,
            Constants.PATIENT_ALDER,
            Constants.VECKODAG,
            Constants.VARDFORM,
            Constants.STAT_KOD,
            Constants.OP_KORT,
            Constants.KVAR_PRIO_TID,
            Constants.PLANERAD_OPERATOR,
        ]
