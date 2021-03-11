import pandas as pd
import datetime
import random


def gen_weekday_range(start, end):
    """
    Returns a list of weekdsays between two dates.
    Elements in list of type: Timestamps
    """
    dates = pd.date_range(start, end).tolist()
    weekdays = [date for date in dates if date.day_of_week not in [5, 6]]
    return weekdays


print(gen_weekday_range('2021-01-01', '2021-02-02')[0])

"""
Behandlingsnr, Anmälningstidpunkt, SistaOpTidpunkt, Opkategori_text, Prioritet_dagar, KortVarsel, ASAklass,
KravOperationstidMinuter, KravFörberedelsetidMinuter, KravtidEfterMinuter, PlaneradStartOpsalTidpunkt,
PlaneradSlutOpsalTidpunkt, De_PlaneradOpsal_FK, PatientÅlderVidOp, Veckodag, Starttimme, 'TotaltidStart'
"""


def get_random_time():
    minutes = random.choice(range(0, 60, 5))
    if minutes < 10:
        minutes = '0' + str(minutes)
    hours = random.choice(range(7, 15))
    if hours < 10:
        hours = '0' + str(hours)

    return '{}:{}:00'.format(hours, minutes)


def build_random_data(start_date, end_date, num_patients=100):
    date_range = gen_weekday_range(start_date, end_date)  # Dummy dates

    op_category = ['Elektiv', 'Akut']
    prio_days = [0, 7, 14, 30, 60, 90]
    asa_class = [1, 2, 3, 4, None]
    op_time_demand = range(20, 180, 5)
    preOp_time_demand = range(20, 105, 5)
    postOp_time_demand = range(10, 60, 5)
    op_rooms = [247, 249, 251, 253, 256]

    patients = []
    for i in range(num_patients):  # not using list builder because some data has to be calculated

        patient_booked = (random.randint(1, 10) < 7)
        if (patient_booked):
            booked_date = random.choice(date_range)
            op_date = random.choice(date_range[date_range.index(booked_date):]).date()
            day_of_week = booked_date.day_of_week
            start_time = get_random_time()

            patient = {
                'Behandlingsnr': random.randint(11111111, 99999999),
                'Anmälningstidpunkt': booked_date,
                'SistaOpTidpunkt': -1,
                'Opkategori_text': random.choice(op_category),
                'Prioritet_dagar': random.choice(prio_days),
                'ASAklass': random.choice(asa_class),
                'KravOperationstidMinuter': random.choice(op_time_demand),
                'KravFörberedelsetidMinuter': random.choice(preOp_time_demand),
                'KravtidEfterMinuter': random.choice(postOp_time_demand),
                'De_PlaneradOpsal_FK': random.choice(op_rooms),
                'PlaneradStartOpsalTidpunkt': '{} {}'.format(op_date, get_random_time()),
                'PatientÅlderVidOp': random.randint(10, 100),
                'Veckodag': day_of_week,
                'Starttimme': start_time,
                'TotaltidStart': '{} {} {}'.format(booked_date, day_of_week, start_time),
            }
            patients.append(patient)

        else:
            patient = {
                'Behandlingsnr': random.randint(11111111, 99999999),
                'Anmälningstidpunkt': random.choice(date_range),
                'SistaOpTidpunkt': -1,
                'Opkategori_text': random.choice(op_category),
                'Prioritet_dagar': random.choice(prio_days),
                'ASAklass': random.choice(asa_class),
                'KravOperationstidMinuter': random.choice(op_time_demand),
                'KravFörberedelsetidMinuter': random.choice(preOp_time_demand),
                'KravtidEfterMinuter': random.choice(postOp_time_demand),
                'De_PlaneradOpsal_FK': -1,
                'PlaneradStartOpsalTidpunkt': None,
                'PatientÅlderVidOp': random.randint(10, 100),
                'Veckodag': None,
                'Starttimme': None,
                'TotaltidStart': None,
            }
            patients.append(patient)

    return patients


data = build_random_data('2018-01-01', '2018-10-10', num_patients=100)
df = pd.DataFrame.from_dict(data)


def days_since_booking(booked_date):
    today = datetime.date.today()
    year, month, day = booked_date.split(sep='-')
    booked_date = datetime.date(int(year), int(month), int(day))
    return (today - booked_date).days


print(days_since_booking('2018-01-01'))

# df.to_excel("output.xlsx")
