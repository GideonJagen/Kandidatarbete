import dash_bootstrap_components as dbc
import dash_html_components as html

from components.op_code_selection import OpCodeSelection
from components.op_time_slider import OpTimeWidget
from components.statistics_code import StatisticsCodeWidget
from components.caretype import CaretypeWidget
from components.age import AgeWidget
from components.anestesi import AnestesiWidget
from components.asa import AsaWidget
from components.municipalities import MunicipalitiesWidget
from components.operator import OperatorWidget


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
                CaretypeWidget.caretype_widget(),
                MunicipalitiesWidget.municipalities_component(),
                AnestesiWidget.anestesi_widget(),
                AgeWidget.age_widget(),
                StatisticsCodeWidget.statistics_code_widget(),
                AsaWidget.asa_widget(),
                OpTimeWidget.op_time_widget(5, 120),
                OpCodeSelection.op_code_selection(),
                OperatorWidget.operator_widget(),
            ],
        )
        return component
