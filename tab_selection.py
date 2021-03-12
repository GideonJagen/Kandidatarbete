import dash_core_components as dcc
import dash_html_components as html

from components.opCode_selection import OpCode_selection
from components.opTime_slider import OpTime_widget
from components.statistics_code import Statistics_code_widget
from components.vardtyp import Vardtyp_widget


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
            Statistics_code_widget.statistics_code_widget(),
            Vardtyp_widget.vardtyp_widget(),
        ],
    )
    return widget


def operation_tab():
    widget = dcc.Tab(
        id="operation_tab",
        label="Operation",
        children=[
            OpTime_widget.opTime_widget(5, 120),
            OpCode_selection.opCode_selection(
                ["NH132", "SU145", "LU987", "NX132", "SX145", "LX987"]
            ),
        ],
    )
    return widget


def anesthesia_tab():
    widget = dcc.Tab(id="anesthesia_tab", label="Anestesi", children=[])
    return widget
