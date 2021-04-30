import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash


class Asa:
    STANDARD_VALUE = []  # Basera på data

    @staticmethod
    def get_component():
        widget = dbc.FormGroup(
            children=[
                dbc.Label(
                    html.Span(
                        [
                            "ASA-klass ",
                            html.I(className="fas fa-info-circle", id="asa_info"),
                        ]
                    ),
                    className="label col-form-label-lg font-weight-bold mb-n4 pd-n4",
                ),
                Asa._asa_tooltip(),
                html.Hr(className="sidebar-separator"),
                Asa._asa_radio_items(),
                Asa._asa_checklist(),
            ],
        )
        return widget

    @staticmethod
    def _asa_radio_items():
        radio_items = dbc.RadioItems(
            id="asa_radio_items",
            value="all",
            options=[
                {"label": "Visa alla", "value": "all"},
                {"label": "Välj: ", "value": "selection"},
            ],
        )
        return radio_items

    @staticmethod
    def _asa_checklist():
        collapse = dbc.Collapse(
            id="asa_collapse",
            is_open=False,
            children=[
                dbc.Checklist(
                    id="asa_checklist",
                    options=[
                        {"label": "ASA 1", "value": 1},
                        {"label": "ASA 2", "value": 2},
                        {"label": "ASA 3", "value": 3},
                        {"label": "ASA 4", "value": 4},
                        {"label": "Saknas", "value": 0},
                    ],
                    labelStyle={"display": "inline-block"},
                ),
            ],
        )
        return collapse

    @staticmethod
    def _asa_tooltip():
        tooltip = dbc.Tooltip(
            "För att inkludera patienter som ej klassats av narkosläkare, "
            "välj ”Ej klassad” utöver önskade klasser och inkludera sedan "
            "önskad ASA-klass som nyckelord i kategorin ”Nyckelord”",
            target="asa_info",
            placement="auto",
            style={"text-transform": "none"},
        )
        return tooltip

    @staticmethod
    def add_callback(app):
        app = Asa._add_callback(app)

        @app.callback(
            Output(component_id="asa_checklist", component_property="value"),
            Output(component_id="asa_radio_items", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_component(n_clicks):
            return Asa.STANDARD_VALUE, "all"

        return app

    @staticmethod
    def _add_callback(app):
        @app.callback(
            Output(component_id="asa_collapse", component_property="is_open"),
            Input(component_id="asa_radio_items", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def collapse(value, reset):
            context = dash.callback_context
            if context.triggered[0]["prop_id"].split(".")[0] == "reset_filter_button":
                return False
            return value == "selection"

        return app

    @staticmethod
    def add_str_callback(app):
        @app.callback(
            Output(component_id="active_asa", component_property="children"),
            Input(component_id="asa_checklist", component_property="value"),
            Input(component_id="asa_radio_items", component_property="value"),
        )
        def update_str(value_cl, value_ri):
            return Asa.value_to_string(value_cl, value_ri)

        return app

    @staticmethod
    def value_to_string(value_cl, value_ri):
        return f"ASA-klass: {', '.join([str(val) for val in value_cl]) if len(value_cl) > 0 and value_ri == 'Välj' and len(value_cl) < 5 else 'Alla' }"
