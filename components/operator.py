import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


class OperatorWidget:
    STANDARD_VALUE_RI = "all"
    STANDARD_VALUE_DD = None
    STANDARD_OPERATORS = [
        "Clara",
        "David",
        "Gideon",
        "Johan",
        "Linnea",
        "Raoul",
    ]  # Made up for testing purposes

    @staticmethod
    def operator_widget():
        widget = dbc.FormGroup(
            children=[
                dbc.Label("Operatör"),
                OperatorWidget._operator_radiobuttons(),
                OperatorWidget._operator_dropdown(),
            ],
        )
        return widget

    @staticmethod
    def _operator_radiobuttons():
        options = [
            {"label": "Visa alla", "value": "all"},
            {"label": "Filtrera efter operatör", "value": "operator"},
            {"label": "Visa endast icke-tilldelade patienter", "value": "blank"},
        ]

        widget = dbc.RadioItems(
            id="operator_radiobuttons",
            options=options,
            value=OperatorWidget.STANDARD_VALUE_RI,
        )
        return widget

    @staticmethod
    def _operator_dropdown():

        widget = html.Div(
            [
                dcc.Dropdown(
                    id="operator_dropdown",
                    placeholder="Välj operatör",
                    multi=True,
                    value=OperatorWidget.STANDARD_VALUE_DD,
                    options=[
                        {"label": operator, "value": operator}
                        for operator in OperatorWidget.STANDARD_OPERATORS
                    ],
                    style={"display": "block"},
                )
            ]
        )
        return widget

    @staticmethod
    def add_operator_callbacks(app):
        app = OperatorWidget.reset_operator_ri_callback(app)
        app = OperatorWidget.reset_operator_dd_callback(app)
        app = OperatorWidget.show_hide_element_callback(app)
        return app

    @staticmethod
    def reset_operator_ri_callback(app):
        @app.callback(
            Output(component_id="operator_radiobuttons", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_operator_ri(n_clicks):
            return OperatorWidget.STANDARD_VALUE_RI

        return app

    @staticmethod
    def reset_operator_dd_callback(app):
        @app.callback(
            Output(component_id="operator_dropdown", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_operator_dd(visibility_state):
            if visibility_state == "all" or visibility_state == "blank":
                return OperatorWidget.STANDARD_VALUE_DD

        return app

    @staticmethod
    def show_hide_element_callback(app):
        @app.callback(
            Output(component_id="operator_dropdown", component_property="style"),
            Input(component_id="operator_radiobuttons", component_property="value"),
        )
        def show_hide_element(visibility_state):
            if visibility_state == "operator":
                return {"display": "block"}
            if visibility_state == "all" or visibility_state == "blank":
                return {"display": "none"}

        return app
