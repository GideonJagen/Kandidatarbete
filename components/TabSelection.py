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


class TabSelection:
    @staticmethod
    def get_component():
        """
        Top of tab hierarcy, contains all tabs
        """
        widget = html.Div(
            [
                dbc.Tabs(
                    [
                        dbc.Tab(TabSelection._patient_tab(), label="Patient"),
                        dbc.Tab(TabSelection._operation_tab(), label="Operation"),
                    ]
                )
            ]
        )
        return widget

    @staticmethod
    def _patient_tab():
        filter_col_a = dbc.Col(
            [
                Caretype.get_component(),
                Municipalities.get_component(),
                Anaesthetic.get_component(),
            ]
        )

        filter_col_b = dbc.Col(
            [
                Age.get_component(),
                StatisticsCode.get_component(),
                Asa.get_component(),
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
                OpTime.get_component(5, 120),
                OpCode.get_component(),
                Operator.getComponent(),
            ]
        )

        card = dbc.Card([dbc.Row([filter_col_a])])
        return card
