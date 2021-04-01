import dash_bootstrap_components as dbc
import dash_html_components as html

from components.op_code_selection import OpCode
from components.op_time_slider import OpTime
from components.statistics_code import StatisticsCode
from components.caretype import Caretype
from components.age import Age
from components.anestesi import Anaesthetic
from components.asa import Asa
from components.municipalities import Municipalities
from components.operator import Operator


class SideBar:
    SEARCH_FILTER = "Sökfilter"
    OPEN_FILTER = "Öppna filter"
    REQUEST_FILL_FORM = "Var god fyll i relevanta sökfält"

    @staticmethod
    def sidebar_component():
        component = html.Div(
            children=[
                html.Div(
                    [
                        html.H2(SideBar.SEARCH_FILTER),
                        SideBar._close_sidebar_button(),
                    ],
                    className="d-flex justify-content-between",
                ),
                html.Hr(),
                html.P(SideBar.REQUEST_FILL_FORM),
                SideBar._filter_form(),
            ],
            className="p-1",
        )
        return component

    @staticmethod
    def _close_sidebar_button():
        component = dbc.Button("X", className="btn btn-warning")
        return component

    @staticmethod
    def _open_sidebar_button():
        component = dbc.Button(SideBar.OPEN_FILTER, className="btn btn-primary")
        return component

    @staticmethod
    def _filter_form():
        component = dbc.Form(
            children=[
                Caretype.caretype_widget(),
                Municipalities.municipalities_component(),
                Anaesthetic.anaesthetic_widget(),
                Age.age_widget(),
                StatisticsCode.statistics_code_widget(),
                Asa.asa_widget(),
                OpTime.op_time_widget(5, 120),
                OpCode.op_code_selection(),
                Operator.operator_widget(),
            ],
        )
        return component
