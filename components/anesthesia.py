import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


class Anesthesia:
    STANDARD_VALUE = []

    @staticmethod
    def get_component():
        widget = dbc.FormGroup(
            [dbc.Label("Anestesibedömning"), Anesthesia._anesthesia_checklist()]
        )
        return widget

    @staticmethod
    def _anesthesia_checklist():
        checklist = dbc.Checklist(
            options=[
                {"label": "Ej klar", "value": "ek"},
                {"label": "Påbörjad", "value": "pb"},
                {"label": "Klar", "value": "klar"},
            ],
            id="anaesthesia_checklist",
        )

        return checklist

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(component_id="anaesthesia_checklist", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_component(n_clicks):
            return Anesthesia.STANDARD_VALUE

        return app
