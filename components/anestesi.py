import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


class Anaesthetic:
    STANDARD_VALUE = []

    @staticmethod
    def getComponent():
        widget = dbc.FormGroup(
            [dbc.Label("Anestesibedömning"), Anaesthetic._anaesthetic_checklist()]
        )
        return widget

    @staticmethod
    def _anaesthetic_checklist():
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
    def add_anaesthetic_callback(app):
        @app.callback(
            Output(component_id="anaesthesia_checklist", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_opTime(n_clicks):
            return Anaesthetic.STANDARD_VALUE

        return app
