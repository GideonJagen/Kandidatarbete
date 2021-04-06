import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


class CareType:
    STANDARD_VALUE = "all"

    @staticmethod
    def get_component():
        widget = dbc.FormGroup(
            [dbc.Label("Vårdform"), CareType._caretype_radiobuttons()]
        )
        return widget

    @staticmethod
    def _caretype_radiobuttons():
        options = [
            {"label": "Öppenvård", "value": "Öppen vård"},
            {"label": "Slutenvård", "value": "Sluten vård"},
            {"label": "Visa alla", "value": "all"},
        ]
        widget = dbc.RadioItems(
            id="caretype_radiobuttons",
            options=options,
            labelStyle={"display": "block"},
            value="all",
        )
        return widget

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(component_id="caretype_radiobuttons", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_component(n_clicks):
            return CareType.STANDARD_VALUE

        return app
