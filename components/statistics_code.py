import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


class StatisticsCode:
    STANDARD_VALUE = []
    SELECT_STAT_CODES = "Välj statistikkoder"

    @staticmethod
    def get_component():
        widget = dbc.FormGroup(
            id="statistics_code_widget",
            children=[
                dbc.Label("Statistikkod"),
                StatisticsCode._statistics_code_dropdown(),
            ],
        )
        return widget

    @staticmethod
    def _statistics_code_dropdown():
        codes = [
            {"label": "30 dagar", "value": "30 dagar"},
            {"label": "60 dagar", "value": "60 dagar"},
            {"label": "90 dagar", "value": "90 dagar"},
            {"label": "6 månader", "value": "6 månader"},
            {"label": "9 månader", "value": "9 månader"},
            {"label": "1 år", "value": "1 år"},
            {"label": ">1 år", "value": ">1 år"},
        ]

        # TODO: Replace this dropdown with a dbc component, if there's a suitable replacement
        dropdown = dcc.Dropdown(
            id="statistics_dropdown",
            options=codes,
            placeholder=StatisticsCode.SELECT_STAT_CODES,
            value=[],
            multi=True,
        )
        return dropdown

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(component_id="statistics_dropdown", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_component(n_clicks):
            return StatisticsCode.STANDARD_VALUE

        return app
