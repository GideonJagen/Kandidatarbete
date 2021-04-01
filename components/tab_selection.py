import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from components.op_code_selection import OpCode
from components.op_time_slider import OpTime
from components.statistics_code import StatisticsCode
from components.caretype import Caretype
from components.age import Age
from components.anestesi import Anaesthetic
from components.asa import Asa
from components.municipalities import Municipalities
from components.operator import Operator


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
                Caretype.caretype_widget(),
                Municipalities.municipalities_component(),
                Anaesthetic.anaesthetic_widget(),
            ]
        )

        filter_col_b = dbc.Col(
            [
                Age.age_widget(),
                StatisticsCode.statistics_code_widget(),
                Asa.asa_widget(),
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
                OpTime.op_time_widget(5, 120),
                OpCode.op_code_selection(),
                Operator.operator_widget(),
            ]
        )

        card = dbc.Card([dbc.Row([filter_col_a])])
        return card
