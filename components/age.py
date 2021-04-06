import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


class Age:
    MIN_AGE = 0
    MAX_AGE = 150  # Not the actual value, this has to be fixed, magic number

    @staticmethod
    def get_component():
        widget = dbc.FormGroup(
            [
                dbc.Label("Ålder"),
                dcc.RangeSlider(
                    id="age",
                    min=Age.MIN_AGE,
                    max=Age.MAX_AGE,
                    step=1,
                    marks={
                        Age.MIN_AGE: "0",
                        16: "16",
                        80: "80",
                        Age.MAX_AGE: "max",
                    },
                    value=[Age.MIN_AGE, Age.MAX_AGE],
                ),
            ]
        )
        return widget

    @staticmethod
    def add_age_callback(app):
        @app.callback(
            Output(component_id="age", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_component(n_clicks):
            return [Age.MIN_AGE, Age.MAX_AGE]

        return app
