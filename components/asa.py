import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


class Asa:
    STANDARD_VALUE = []  # Basera på data

    @staticmethod
    def get_component():
        widget = dbc.FormGroup(
            children=[
                dbc.Label(
                    children="ASA-klass",
                ),
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
    def value_to_string(value):
        return f"ASA-klass: {', '.join([str(val) for val in value]) if len(value) > 0 else 'Alla' }"
