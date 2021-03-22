import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


class AnestesiWidget:
    STANDARD_VALUE = []

    @staticmethod
    def anestesi_widget():
        widget = dbc.FormGroup(
            children=[
                dbc.Label("Anestesibedömning"),
                dbc.Checklist(
                    id="anestesi_checklist",
                    options=[
                        {"label": "Ej klar", "value": "ek"},
                        {"label": "Påbörjad", "value": "pb"},
                        {"label": "Klar", "value": "klar"},
                    ],
                ),
            ]
        )
        return widget

    @staticmethod
    def add_anestesi_callback(app):
        @app.callback(
            Output(component_id="anestesi_checklist", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_opTime(n_clicks):
            return AnestesiWidget.STANDARD_VALUE

        return app
