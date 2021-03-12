import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


class AnestesiWidget:
    STANDARD_VALUE = []
    @staticmethod
    def anestesi_widget():
        widget = html.Div(
            id="anestesi",
            children=[
                html.H4(
                    id="anestesi_h4",
                    children="Anestesibedömning",
                    style={
                        "borderWidth": "1px",
                        "borderStyle": "solid",
                        "margin": "0px",
                    },
                ),
                dcc.Checklist(
                    id="anestesi_checklist",
                    options=[
                        {"label": "Ej klar", "value": "ek"},
                        {"label": "Påbörjad", "value": "pb"},
                        {"label": "Klar", "value": "klar"},
                    ],
                    labelStyle={"display": "inline-block"},
                    style={
                        "width": "100%",
                        "borderWidth": "1px",
                        "borderStyle": "solid",
                        "margin": "0px",
                    },
                ),
            ],
            style={
                "width": "30%",
                "borderWidth": "1px",
                "borderStyle": "solid",
                "textAlign": "center",
                "margin": "5px",
            },
        )
        return widget



    @staticmethod
    def reset_anestesi_callback(app):
        @app.callback(
        Output(component_id = 'anestesi_checklist' , component_property = 'value'),
        Input(component_id = 'reset_filter_button' , component_property = 'n_clicks')
        )
        def reset_opTime(n_clicks):
            return AnestesiWidget.STANDARD_VALUE

        return app
