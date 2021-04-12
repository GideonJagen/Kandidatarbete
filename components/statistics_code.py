import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash


class StatisticsCode:
    STANDARD_VALUE = []
    SELECT_STAT_CODES = "Välj statistikkoder"

    @staticmethod
    def get_component():
        widget = dbc.FormGroup(
            id="statistics_code_widget",
            children=[
                dbc.Label(
                    "Statistikkod",
                    className="label col-form-label-lg font-weight-bold mb-n4 pd-n4",
                ),
                html.Hr(style={"margin-top": 0, "margin-bottom": 10}),
                dbc.RadioItems(
                    id="statistics_radio_items",
                    value="Visa alla",
                    options=[
                        {"label": "Visa alla", "value": "Visa alla"},
                        {"label": "Välj: ", "value": "Välj"},
                    ],
                ),
                dbc.Collapse(
                    id="statistics_collapse",
                    is_open=False,
                    children=[
                        StatisticsCode._statistics_code_checklist(),
                    ],
                ),
            ],
        )
        return widget

    @staticmethod
    def _statistics_code_checklist():
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
        checklist = dbc.Checklist(
            id="statistics_checklist",
            options=codes,
            # placeholder=StatisticsCode.SELECT_STAT_CODES,
            # value=[],
            # multi=True,
            labelStyle={"display": "inline-block"},
        )
        return checklist

    @staticmethod
    def add_callback(app):
        app = StatisticsCode._add_callback(app)

        @app.callback(
            Output(component_id="statistics_checklist", component_property="value"),
            Output(component_id="statistics_radio_items", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_component(n_clicks):
            return StatisticsCode.STANDARD_VALUE, "Visa alla"

        return app

    @staticmethod
    def _add_callback(app):
        @app.callback(
            Output(component_id="statistics_collapse", component_property="is_open"),
            Input(component_id="statistics_radio_items", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def collapse(value, reset):
            context = dash.callback_context
            if context.triggered[0]["prop_id"].split(".")[0] == "reset_filter_button":
                return False
            return value == "Välj"

        return app

    @staticmethod
    def add_str_callback(app):
        @app.callback(
            Output(
                component_id="active_statistics_code", component_property="children"
            ),
            Input(component_id="statistics_checklist", component_property="value"),
            Input(component_id="statistics_radio_items", component_property="value"),
        )
        def update_str(value_cl, value_ri):
            return StatisticsCode.value_to_string(value_cl, value_ri)

        return app

    @staticmethod
    def value_to_string(value_cl, value_ri):
        return f"Statistikkod: {' ,'.join([str(s) for s in value_cl]) if len(value_cl) > 0 and value_ri == 'Välj' and len(value_cl) < 7 else 'Alla'}"
