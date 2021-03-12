import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

class AgeWidget:
    STANDARD_VALUE = [0, 10]
    @staticmethod
    def age_widget():
        widget = html.Div(
            [
                dcc.RangeSlider(
                    id = 'age',
                    min=0,
                    max=10,
                    step=None,
                    marks={0: "0", 2: "16", 8: "80", 10: "max"},
                    value=[0, 10],
                )
            ]
        )
        return widget



    @staticmethod
    def reset_age_callback(app):
        @app.callback(
        Output(component_id = 'age' , component_property = 'value'),
        Input(component_id = 'reset_filter_button' , component_property = 'n_clicks')
        )
        def reset_opTime(n_clicks):
            return AgeWidget.STANDARD_VALUE

        return app
