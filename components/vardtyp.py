import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

# Döpa om till vårdform, som det heter i datan


class VardtypWidget:
    STANDARD_VALUE = "all"

    @staticmethod
    def vardtyp_widget():
        widget = dbc.FormGroup(
            [dbc.Label("Vårdtyp"), VardtypWidget._vardtyp_radiobuttons()]
        )
        return widget

    @staticmethod
    def _vardtyp_radiobuttons():
        options = [
            {"label": "Öppenvård", "value": "open"},
            {"label": "Slutenvård", "value": "closed"},
            {"label": "Visa alla", "value": "all"},
        ]
        widget = dbc.RadioItems(
            id="vardtyp_radiobuttons",
            options=options,
            labelStyle={"display": "block"},
            value="all",
        )
        return widget

    @staticmethod
    def _vardtyp_dropdown():
        options = [
            {"label": "Öppenvård", "value": "open"},
            {"label": "Slutenvård", "value": "closed"},
            {"label": "Visa alla", "value": "all"},
        ]
        widget = dcc.Dropdown(
            id="vardtyp_dropdown",
            options=options,
            placeholder="Välj Vårdtyp",
        )
        return widget

    @staticmethod
    def add_vardtyp_callback(app):
        @app.callback(
            Output(component_id="vardtyp_radiobuttons", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_opTime(n_clicks):
            return VardtypWidget.STANDARD_VALUE

        return app
