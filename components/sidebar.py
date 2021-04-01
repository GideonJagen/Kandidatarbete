import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


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
                    className="d-flex justify-content-between"
                ),
                html.Hr(),
                html.P(SideBar.REQUEST_FILL_FORM)
            ],
            className="p-1"
        )
        return component

    @staticmethod
    def _close_sidebar_button():
        component = dbc.Button(
            "X", className="btn btn-warning"
        )
        return component

    @staticmethod
    def _open_sidebar_button():
        component = dbc.Button(
            SideBar.OPEN_FILTER, className="btn btn-primary"
        )
        return component
