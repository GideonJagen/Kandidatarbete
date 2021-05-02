import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


class Priority:
    STANDARD_VALUE = []
    SELECT_STAT_CODES = "Välj prioriteter"

    @staticmethod
    def get_component():
        widget = dbc.FormGroup(
            id="priority_widget",
            children=[
                dbc.Label(
                    "Prioritet",
                    className="label col-form-label-lg font-weight-bold mb-n4 pd-n4",
                ),
                html.Hr(style={"margin-top": 0, "margin-bottom": 10}),
                dbc.RadioItems(
                    id="priority_radio_items",
                    value="Visa alla",
                    options=[
                        {"label": "Visa alla", "value": "Visa alla"},
                        {"label": "Välj: ", "value": "Välj"},
                    ],
                ),
                dbc.Collapse(
                    id="priority_collapse",
                    is_open=False,
                    children=[
                        Priority._priority_checklist(),
                    ],
                ),
            ],
        )
        return widget

    @staticmethod
    def _priority_checklist():
        codes = [
            {"label": "30 dagar", "value": "30 dagar"},
            {"label": "60 dagar", "value": "60 dagar"},
            {"label": "90 dagar", "value": "90 dagar"},
        ]

        # TODO: Replace this dropdown with a dbc component, if there's a suitable replacement
        checklist = dbc.Checklist(
            id="priority_checklist",
            options=codes,
            labelStyle={"display": "inline-block"},
        )
        return checklist

    @staticmethod
    def add_callback(app):
        app = Priority._add_callback(app)

        @app.callback(
            Output(component_id="priority_checklist", component_property="value"),
            Output(component_id="priority_radio_items", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_component(n_clicks):
            return Priority.STANDARD_VALUE, "Visa alla"

        return app

    @staticmethod
    def _add_callback(app):
        @app.callback(
            Output(component_id="priority_collapse", component_property="is_open"),
            Input(component_id="priority_radio_items", component_property="value"),
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
            Output(component_id="active_priority", component_property="children"),
            Input(component_id="priority_checklist", component_property="value"),
            Input(component_id="priority_radio_items", component_property="value"),
        )
        def update_str(value_cl, value_ri):
            return Priority.value_to_string(value_cl, value_ri)

        return app

    @staticmethod
    def value_to_string(value_cl, value_ri):
        return f"Prioritet: {' ,'.join([str(s) for s in value_cl]) if 0 < len(value_cl) < 7 and value_ri == 'Välj' else 'Alla'}"
