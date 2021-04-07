import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from components.age import Age
from components.asa import Asa
from components.op_code import OpCode
from components.op_time import OpTime
from components.municipalities import Municipalities
from components.statistics_code import StatisticsCode
from components.care_type import CareType
from components.short_notice import ShortNotice
from components.anesthesia import Anesthesia
from components.operator import Operator


class ActiveFilters:
    @staticmethod
    def get_component():
        widget = dbc.Table(
            style={"width": "40em"},
            bordered=False,
            id="active_filters",
            children=[html.Tbody(ActiveFilters._build_rows())],
        )
        return widget

    @staticmethod
    def _build_rows():
        row1 = html.Tr([html.Td(id="active_age"), html.Td(id="active_asa")])
        row2 = html.Tr(
            [html.Td(id="active_anesthesia"), html.Td(id="active_care_type")]
        )
        row3 = html.Tr([html.Td(id="active_op_code"), html.Td(id="active_op_time")])
        row4 = html.Tr(
            [html.Td(id="active_municipalities"), html.Td(id="active_statistics_code")]
        )
        row5 = html.Tr(
            [html.Td(id="active_short_notice"), html.Td(id="active_operator")]
        )
        return [row1, row2, row3, row4, row5]
