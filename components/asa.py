import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


class Asa:
    STANDARD_VALUE = []  # Basera på data

    @staticmethod
    def get_component():
        widget = dbc.FormGroup(
            children=[
                dbc.Label(
                    "ASA-klass",
                    className="label col-form-label-lg font-weight-bold mb-n4 pd-n4",
                ),
                html.Hr(style={"margin-top": 0, "margin-bottom": 10}),
                dbc.Checklist(
                    id="asa_checklist",
                    options=[
                        {"label": "ASA 1", "value": 1},
                        {"label": "ASA 2", "value": 2},
                        {"label": "ASA 3", "value": 3},
                        {"label": "ASA 4", "value": 4},
                        {"label": "Saknas", "value": "Saknas"},
                    ],
                    labelStyle={"display": "inline-block"},
                ),
            ],
        )
        return widget

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(component_id="asa_checklist", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_component(n_clicks):
            return Asa.STANDARD_VALUE

        return app

    @staticmethod
    def add_str_callback(app):
        @app.callback(
            Output(component_id="active_asa", component_property="children"),
            Input(component_id="asa_checklist", component_property="value"),
        )
        def update_str(value):
            return Asa.value_to_string(value)

        return app

    @staticmethod
    def value_to_string(value):
        return f"ASA-klass: {', '.join([str(val) for val in value]) if len(value) > 0 else 'Alla' }"
