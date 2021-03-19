import dash_core_components as dcc
import dash_html_components as html

from components.op_code_selection import OpCodeSelection
from components.op_time_slider import OpTimeWidget
from components.statistics_code import StatisticsCodeWidget
from components.vardtyp import VardtypWidget
from components.age import AgeWidget
from components.anestesi import AnestesiWidget
from components.asa import AsaWidget
from components.kommuner import KommunerWidget
import dash_bootstrap_components as dbc


class TabSelectionWidget:
    @staticmethod
    def tab_selection():
        """
        Top of tab hierarcy, contains all tabs
        """
        widget = html.Div(
            children=[
                dcc.Tabs(
                    style={"width": "30%"},
                    id="tabs_selection",
                    value="patient_tab",
                    children=[
                        TabSelectionWidget._patient_tab(),
                        TabSelectionWidget._operation_tab(),
                    ],
                )
            ]
        )
        return widget

    @staticmethod
    def _patient_tab():
        widget = dcc.Tab(
            id="patient_tab",
            label="Patient",
            value="patient_tab",
            children=[
                html.Div(
                    id="patient_div",
                    style={
                        "height": "350px",
                        "width": "100%",
                    },
                    children=[
                        dbc.Row(
                            style={"backgroundColor": "#D1E5F0"},
                            children=[
                                dbc.Col(
                                    children=[
                                        AgeWidget.age_widget(),
                                        StatisticsCodeWidget.statistics_code_widget(),
                                        AsaWidget.asa_widget(),
                                    ]
                                ),
                                dbc.Col(
                                    children=[
                                        VardtypWidget.vardtyp_widget(),
                                        KommunerWidget.kommuner_widget(),
                                        AnestesiWidget.anestesi_widget(),
                                    ]
                                ),
                            ],
                        )
                    ],
                )
            ],
        )
        return widget

    @staticmethod
    def _operation_tab():
        widget = dcc.Tab(
            id="operation_tab",
            label="Operation",
            value="operation_tab",
            children=[
                html.Div(
                    id="operation_div",
                    style={
                        "height": "200px",
                        "width": "100%",
                        "backgroundColor": "#D1E5F0",
                    },
                    children=[
                        OpTimeWidget.op_time_widget(5, 120),
                        OpCodeSelection.op_code_selection(),
                    ],
                )
            ],
        )
        return widget
