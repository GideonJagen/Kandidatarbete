import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


class Municipalities:
    STANDARD_VALUE = "all"

    @staticmethod
    def get_component():
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
            id="municipalities_radiobuttons",
            options=options,
            value=Municipalities.STANDARD_VALUE,
        )
        return widget

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(
                component_id="municipalities_radiobuttons", component_property="value"
            ),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_component(n_clicks):
            return Municipalities.STANDARD_VALUE

        return app
