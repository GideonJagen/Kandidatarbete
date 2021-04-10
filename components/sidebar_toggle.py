import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


class SidebarToggle:

    is_open = True

    @staticmethod
    def get_component():
        component = dbc.Col(
            children=[
                SidebarToggle._sidebar_button(),
            ],
            id="sidebar_toggle",
            width=1,
            className="pl-0",
            style={
                "height": "inherit",
                "flex": "0 0 0",
            },
        )
        return component

    @staticmethod
    def _sidebar_button():
        component = dbc.Button(
            children=[
                html.I(
                    id="sidebar_toggle_icon",
                    className="fas fa-chevron-left",
                )
            ],
            id="btn_sidebar_toggle",
            color="primary",
            className="h-100 d-inline-block",
        )
        return component

    # TODO: Possibly modify such that the class style is not overwritten
    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(component_id="sidebar_content", component_property="style"),
            Output(component_id="sidebar_toggle_icon", component_property="className"),
            Input(component_id="btn_sidebar_toggle", component_property="n_clicks"),
            prevent_initial_call=True,
        )
        def _toggle_sidebar(n_clicks):
            SidebarToggle.is_open = not SidebarToggle.is_open
            return (
                {"display": "block"} if SidebarToggle.is_open else {"display": "none"},
                "fas fa-chevron-left"
                if SidebarToggle.is_open
                else "fas fa-chevron-right",
            )

        return app
