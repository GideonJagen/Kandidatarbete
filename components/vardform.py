import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

# Döpa om till vårdform, som det heter i datan


class VardformWidget:
    STANDARD_VALUE = "all"

    @staticmethod
    def vardform_widget():
        widget = dbc.FormGroup(
            [dbc.Label("Vårdform"), VardformWidget._vardform_radiobuttons()]
        )
        return widget

    @staticmethod
    def _vardform_radiobuttons():
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
    def _vardform_dropdown():
        options = [
            {"label": "Öppenvård", "value": "open"},
            {"label": "Slutenvård", "value": "closed"},
            {"label": "Visa alla", "value": "all"},
        ]
        widget = dcc.Dropdown(
            id="vardform_dropdown",
            options=options,
            placeholder="Välj Vårdform",
        )
        return widget

    @staticmethod
    def add_vardform_callback(app):
        @app.callback(
            Output(component_id="vardform_radiobuttons", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_opTime(n_clicks):
            return VardformWidget.STANDARD_VALUE

        return app
