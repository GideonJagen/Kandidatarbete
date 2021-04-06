import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

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


class SideBar:
    SEARCH_FILTER = "Sökfilter"
    OPEN_FILTER = "Öppna filter"
    REQUEST_FILL_FORM = "Var god fyll i relevanta sökfält"

    is_open = True

    @staticmethod
    def get_component():
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
            style={"transition": "0.5s"},
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
                CareType.get_component(),
                Municipalities.get_component(),
                Anesthesia.get_component(),
                Age.get_component(),
                StatisticsCode.get_component(),
                Asa.get_component(),
                OpTime.get_component(20, 160),
                OpCode.get_component(),
                Operator.get_component(),
                ShortNotice.get_component(),
            ],
        )
        return component

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(component_id="sidebar_content", component_property="style"),
            Input(component_id="btn_sidebar", component_property="n_clicks"),
        )
        def _toggle_sidebar(n_clicks):
            SideBar.is_open = not SideBar.is_open
            # return {"width": "auto", "display": "block"} if SideBar.is_open else {"width": "0px", "display": "none"}
            return {"display": "block"} if SideBar.is_open else {"display": "none"}
            # return {"visibility": "visible"} if SideBar.is_open else {"visibility": "collapse"}

        return app
