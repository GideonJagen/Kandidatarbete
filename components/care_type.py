import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


class CareType:
    STANDARD_VALUE = "Alla"

    @staticmethod
    def get_component():
        widget = dbc.FormGroup(
            [
                dbc.Label(
                    "Vårdform",
                    className="label col-form-label-lg font-weight-bold mb-n4 pd-n4",
                ),
                html.Hr(style={"margin-top": 0, "margin-bottom": 10}),
                CareType._caretype_radioitems(),
            ]
        )
        return widget

    @staticmethod
    def _caretype_radioitems():
        options = [
            {"label": "Visa alla", "value": "Alla"},
            {"label": "Öppenvård", "value": "Öppen vård"},
            {"label": "Slutenvård", "value": "Sluten vård"},
        ]
        widget = dbc.RadioItems(
            id="care_type_radioitems",
            options=options,
            labelStyle={"display": "block"},
            value="all",
        )
        return widget

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(component_id="care_type_radioitems", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_component(n_clicks):
            return CareType.STANDARD_VALUE

        return app

    @staticmethod
    def add_str_callback(app):
        @app.callback(
            Output(component_id="active_care_type", component_property="children"),
            Input(component_id="care_type_radioitems", component_property="value"),
        )
        def update_str(value):
            return CareType.value_to_string(value)

        return app

    @staticmethod
    def value_to_string(value):
        return f"Vårdtyp: {value}"
