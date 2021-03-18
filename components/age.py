import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


class AgeWidget:
    MIN_AGE = 0
    MAX_AGE = 150  # Not the actual value, this has to be fixed, magic number

    @staticmethod
    def age_widget():
        widget = html.Div(
            children=[
                html.H4("Ålder"),
                dcc.RangeSlider(
                    id="age",
                    min=AgeWidget.MIN_AGE,
                    max=AgeWidget.MAX_AGE,
                    step=None,
                    marks={
                        AgeWidget.MIN_AGE: "0",
                        16: "16",
                        80: "80",
                        AgeWidget.MAX_AGE: "max",
                    },
                    value=[AgeWidget.MIN_AGE, AgeWidget.MAX_AGE],
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
        def reset_opTime(n_clicks):
            return [AgeWidget.MIN_AGE, AgeWidget.MAX_AGE]

        return app
