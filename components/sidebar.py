import dash_bootstrap_components as dbc
import dash_html_components as html

from dash.dependencies import Input, Output

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

    is_open = True

    @staticmethod
    def sidebar_component():
        component = dbc.Row(
            children=[SideBar._sidebar_content(), SideBar._sidebar_button()],
            id="sidebar",
            className="p-1",
        )
        return component

    @staticmethod
    def _sidebar_content():
        component = dbc.Col(
            children=[
                html.H2(SideBar.SEARCH_FILTER),
                html.Hr(),
                html.P(SideBar.REQUEST_FILL_FORM),
                SideBar._filter_form(),
            ],
            id="sidebar_content",
        )
        return component

    @staticmethod
    def _sidebar_button():
        component = dbc.Button("X", id="btn_sidebar", className="btn btn-warning")
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

    @staticmethod
    def add_sidebar_callbacks(app):
        @app.callback(
            Output(component_id="sidebar_content", component_property="style"),
            Input(component_id="btn_sidebar", component_property="n_clicks"),
        )
        def _toggle_sidebar(n_clicks):
            SideBar.is_open = not SideBar.is_open
            return {"display": "contents"} if SideBar.is_open else {"display": "none"}

        return app
