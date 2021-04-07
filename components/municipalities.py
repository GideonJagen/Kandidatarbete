import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


class Municipalities:
    STANDARD_VALUE = "Hela VGR"

    @staticmethod
    def get_component():
        widget = dbc.FormGroup(
            children=[
                dbc.Label("Kommuner"),
                Municipalities._municipalities_radioitems(),
            ],
        )
        return widget

    @staticmethod
    def _municipalities_radioitems():
        options = [
            {"label": "Hela VGR", "value": "Hela VGR"},
            {"label": "Kranskommuner", "value": "Kranskommuner"},
        ]

        widget = dbc.RadioItems(
            id="municipalities_radioitems",
            options=options,
            value=Municipalities.STANDARD_VALUE,
        )
        return widget

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(
                component_id="municipalities_radioitems", component_property="value"
            ),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_component(n_clicks):
            return Municipalities.STANDARD_VALUE

        return app

    @staticmethod
    def value_to_string(value):
        return f"Kommuner: {value}"
