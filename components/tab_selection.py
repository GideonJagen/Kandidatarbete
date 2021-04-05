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
                Caretype.getComponent(),
                Municipalities.getComponent(),
                Anaesthetic.getComponent(),
            ]
        )

        filter_col_b = dbc.Col(
            [
                Age.getComponent(),
                StatisticsCode.getComponent(),
                Asa.getComponent(),
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
                OpTime.getComponent(5, 120),
                OpCode.getComponent(),
                Operator.getComponent(),
            ]
        )

        card = dbc.Card([dbc.Row([filter_col_a])])
        return card
