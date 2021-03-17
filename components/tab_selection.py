import dash_core_components as dcc
import dash_html_components as html

from components.opCode_selection import OpCodeSelection
from components.opTime_slider import OpTimeWidget
from components.statistics_code import StatisticsCodeWidget
from components.vardtyp import VardtypWidget


def tab_selection():
    """
    Top of tab hierarcy, contains all tabs
    """
    widget = html.Div(
        children=[
            dcc.Tabs(
                id="tabs_selection",
                value=None,
                children=[
                    patient_tab(),
                    anesthesia_tab(),
                    operation_tab(),
                ],
            )
        ]
    )
    return widget


def patient_tab():
    widget = dcc.Tab(
        id="patient_tab",
        label="Patient",
        children=[
            html.H4("David Johnsson, extremt jävla frisk"),
            StatisticsCodeWidget.statistics_code_widget(),
            VardtypWidget.vardtyp_widget(),
        ],
    )
    return widget


def operation_tab():
    widget = dcc.Tab(
        id="operation_tab",
        label="Operation",
        children=[
            OpTimeWidget.opTime_widget(5, 120),
            OpCodeSelection.opCode_selection(
                [
                    "NH132",
                    "SU145",
                    "LU987",
                    "NX132",
                    "SX145",
                    "LX987",
                    "ND766",
                    "QD824",
                    "ED568",
                ]
            ),
        ],
    )
    return widget


def anesthesia_tab():
    widget = dcc.Tab(id="anesthesia_tab", label="Anestesi", children=[])
    return widget
