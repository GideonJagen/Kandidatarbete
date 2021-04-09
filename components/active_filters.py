import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from components.reset_filter_button import ResetFilterButton
from components.age import Age
from components.anesthesia import Anesthesia
from components.asa import Asa
from components.care_type import CareType
from components.municipalities import Municipalities
from components.op_code import OpCode
from components.op_time import OpTime
from components.operator import Operator
from components.short_notice import ShortNotice
from components.statistics_code import StatisticsCode


class ActiveFilters:
    @staticmethod
    def get_component():
        widget = dbc.Col(
            children=[
                ResetFilterButton.get_component(),
                dbc.Table(
                    className="table table-striped table-dark",
                    style={"width": "40em"},
                    bordered=False,
                    borderless=True,
                    id="active_filters",
                    children=[html.Tbody(ActiveFilters._build_rows())],
                ),
            ]
        )
        return widget

    @staticmethod
    def _get_component():
        widget = dbc.Row(
            children=[
                dbc.Col(
                    children=[
                        dbc.Row(
                            children=[
                                dbc.Label(id="active_age"),
                                dbc.Label(id="active_asa"),
                            ]
                        ),
                        dbc.Row(
                            children=[
                                dbc.Label(id="active_anesthesia"),
                                dbc.Label(id="active_op_time"),
                            ]
                        ),
                        dbc.Row(
                            children=[
                                dbc.Label(id="active_short_notice"),
                                dbc.Label(id="active_care_type"),
                            ]
                        ),
                        dbc.Row(
                            children=[
                                dbc.Label(id="active_op_code"),
                                dbc.Label(id="active_statistics_code"),
                            ]
                        ),
                        dbc.Row(
                            children=[
                                dbc.Label(id="active_municipalities"),
                                dbc.Label(id="active_operator"),
                            ]
                        ),
                    ]
                ),
            ]
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
