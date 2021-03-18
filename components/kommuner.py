import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


class KommunerWidget:
    STANDARD_VALUE = "all"

    @staticmethod
    def kommuner_widget():
        widget = html.Div(
            id="Antal kommuner?",
            children=[
                html.H4("Kommuner"),
                KommunerWidget._kommuner_radiobuttons(),
            ],
        )
        return widget

    @staticmethod
    def _kommuner_radiobuttons():
        options = [
            {"label": "Hela VGR", "value": "all"},
            {"label": "Kranskommuner", "value": "close"},
        ]
        widget = dcc.RadioItems(
            id="kommuner_radiobuttons",
            options=options,
            labelStyle={"display": "block"},
            value=KommunerWidget.STANDARD_VALUE,
        )
        return widget

    @staticmethod
    def add_kommuner_callback(app):
        @app.callback(
            Output(component_id="kommuner_radiobuttons", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_opTime(n_clicks):
            return KommunerWidget.STANDARD_VALUE

        return app
