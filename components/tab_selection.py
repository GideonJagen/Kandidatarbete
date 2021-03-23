import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from components.op_code_selection import OpCodeSelection
from components.op_time_slider import OpTimeWidget
from components.statistics_code import StatisticsCodeWidget
from components.vardtyp import VardtypWidget
from components.age import AgeWidget
from components.anestesi import AnestesiWidget
from components.asa import AsaWidget
from components.kommuner import KommunerWidget


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
        filter_col_a = dbc.Col(
            [
                VardtypWidget.vardtyp_widget(),
                KommunerWidget.kommuner_widget(),
                AnestesiWidget.anestesi_widget(),
            ]
        )

        filter_col_b = dbc.Col(
            [
                AgeWidget.age_widget(),
                StatisticsCodeWidget.statistics_code_widget(),
                AsaWidget.asa_widget(),
            ]
        )

        tab = dbc.Tab(
            dbc.Row([filter_col_a, filter_col_b]),
            label="Patient",
        )
        return tab

    @staticmethod
    def _operation_tab():
        widget = dbc.Tab(
            label="Operation",
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
