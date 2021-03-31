import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

# Döpa om till vårdform, som det heter i datan


class CaretypeWidget:
    STANDARD_VALUE = "all"

    @staticmethod
    def caretype_widget():
        widget = dbc.FormGroup(
            [dbc.Label("Vårdform"), CaretypeWidget._caretype_radiobuttons()]
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
            id="vardform_radiobuttons",
            options=options,
            labelStyle={"display": "block"},
            value="all",
        )
        return widget

    @staticmethod
    def add_caretype_callback(app):
        @app.callback(
            Output(component_id="vardform_radiobuttons", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_opTime(n_clicks):
            return CaretypeWidget.STANDARD_VALUE

        return app
