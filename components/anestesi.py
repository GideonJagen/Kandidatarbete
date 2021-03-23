import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


class AnestesiWidget:
    STANDARD_VALUE = []

    @staticmethod
    def anestesi_widget():
        widget = dbc.FormGroup(
            [dbc.Label("Anestesibedömning"), AnestesiWidget._anestesi_checklist()]
        )
        return widget

    @staticmethod
    def _anestesi_checklist():
        checklist = dbc.Checklist(
            options=[
                {"label": "Ej klar", "value": "ek"},
                {"label": "Påbörjad", "value": "pb"},
                {"label": "Klar", "value": "klar"},
            ],
            id="anestesi_checklist",
        )

        return checklist

    @staticmethod
    def add_anestesi_callback(app):
        @app.callback(
            Output(component_id="anestesi_checklist", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_opTime(n_clicks):
            return AnestesiWidget.STANDARD_VALUE

        return app
