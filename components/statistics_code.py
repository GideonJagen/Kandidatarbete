import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


class StatisticsCodeWidget:
    STANDARD_VALUE = []

    @staticmethod
    def statistics_code_widget():
        widget = html.Div(
            id="statistics_code_widget",
            children=[
                html.H4("Statistikkod"),
                StatisticsCodeWidget._statistics_code_dropdown(),
            ],
        )
        return widget

    @staticmethod
    def _statistics_code_dropdown():
        codes = [
            {"label": "30 dagar", "value": "30d"},
            {"label": "90 dagar", "value": "90d"},
            {"label": "6 månader", "value": "6m"},
            {"label": "9 månader", "value": "9m"},
            {"label": "1 år", "value": "1å"},
            {"label": ">1 år", "value": ">1å"},
        ]
        dropdown = dcc.Dropdown(
            id="statistics_dropdown",
            options=codes,
            placeholder="Välj statistikkoder",
            value=[],
            multi=True,
        )
        return dropdown

    @staticmethod
    def add_statistics_code_callback(app):
        @app.callback(
            Output(component_id="statistics_dropdown", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_opTime(n_clicks):
            return StatisticsCodeWidget.STANDARD_VALUE

        return app
