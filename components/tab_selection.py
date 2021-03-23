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
    def filter_tabs():
        """
        Top of tab hierarcy, contains all tabs
        """
        widget = html.Div(
            [
                dbc.Tabs(
                    [
                        dbc.Tab(TabSelectionWidget._patient_tab(), label="Patient"),
                        dbc.Tab(TabSelectionWidget._operation_tab(), label="Operation"),
                    ]
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

        card = dbc.Card(
            dbc.Row([filter_col_a, filter_col_b]),
        )
        return card

    @staticmethod
    def _operation_tab():
        filter_col_a = dbc.Col(
            [
                OpTimeWidget.op_time_widget(5, 120),
                OpCodeSelection.op_code_selection(),
            ]
        )

        card = dbc.Card([dbc.Row([filter_col_a])])
        return card
