import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


class Anesthesia:
    STANDARD_VALUE = []

    @staticmethod
    def get_component():
        widget = dbc.FormGroup(
            [
                dbc.Label(
                    "Anestesibedömning",
                    className="label col-form-label-lg font-weight-bold mb-n4 pd-n4",
                ),
                html.Hr(style={"margin-top": 0, "margin-bottom": 10}),
                Anesthesia._anesthesia_checklist(),
            ]
        )
        return widget

    @staticmethod
    def _anesthesia_checklist():
        checklist = dbc.Checklist(
            options=[
                {"label": "Ej klar", "value": "Ej klar"},
                {"label": "Påbörjad", "value": "Påbörjad"},
                {"label": "Klar", "value": "Klar"},
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

    @staticmethod
    def add_str_callback(app):
        @app.callback(
            Output(component_id="active_anesthesia", component_property="children"),
            Input(component_id="anaesthesia_checklist", component_property="value"),
        )
        def update_str(value):
            return Anesthesia.value_to_string(value)

        return app

    @staticmethod
    def value_to_string(value):
        return f"Anestesi: {', '.join([str(val) for val in value]) if len(value) > 0 else 'Alla'}"
