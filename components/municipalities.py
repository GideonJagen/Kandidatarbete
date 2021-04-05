import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


class Municipalities:
    STANDARD_VALUE = "all"

    @staticmethod
    def getComponent():
        widget = dbc.FormGroup(
            children=[
                dbc.Label("Kommuner"),
                Municipalities._municipalities_radiobuttons(),
            ],
        )
        return widget

    @staticmethod
    def _municipalities_radiobuttons():
        options = [
            {"label": "Hela VGR", "value": "all"},
            {"label": "Kranskommuner", "value": "close"},
        ]

        widget = dbc.RadioItems(
            id="kommuner_radiobuttons",
            options=options,
            value=Municipalities.STANDARD_VALUE,
        )
        return widget

    @staticmethod
    def add_municipalities_callback(app):
        @app.callback(
            Output(component_id="kommuner_radiobuttons", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_opTime(n_clicks):
            return Municipalities.STANDARD_VALUE

        return app
