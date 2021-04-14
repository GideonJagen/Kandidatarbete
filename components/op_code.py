import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from data_handling import LoadedData
import dash


class OpCode:
    STANDARD_VALUE_DD = None
    STANDARD_VALUE_OPT = "Visa alla"
    STANDARD_OP_CODES = []  # Made up for testing purposes

    @staticmethod
    def get_component():
        widget = dbc.FormGroup(
            id="opCode_selection",
            children=[
                dbc.Label(
                    "Operationskod",
                    className="label col-form-label-lg font-weight-bold mb-n4 pd-n4",
                ),
                html.Hr(style={"margin-top": 0, "margin-bottom": 10}),
                OpCode._op_code_dropdown(),
            ],
        )
        return widget

    @staticmethod
    def _op_code_dropdown():
        dropdown = dcc.Dropdown(
            id="opCode_dropdown",
            placeholder="Välj operationskod",
            multi=True,
            value=[],
            options=[
                {"label": code, "value": code} for code in OpCode.STANDARD_OP_CODES
            ],  # list builder to create dropdown options,
        )
        return dropdown

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(component_id="opCode_dropdown", component_property="value"),
            Output(component_id="opCode_dropdown", component_property="options"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
            Input(component_id="upload", component_property="filename"),
            Input(component_id="upload", component_property="contents"),
        )
        def reset_component(n_clicks, filename, contents):
            context = dash.callback_context
            if context.triggered[0]["prop_id"].split(".")[0] == "upload":
                LoadedData.load_data(filename, contents)
            unique = [
                {"label": code, "value": code}
                for code in LoadedData.get_unique_values("OpkortText")
            ]

            return OpCode.STANDARD_VALUE_DD, unique

        return app

    @staticmethod
    def add_str_callback(app):
        @app.callback(
            Output(component_id="active_op_code", component_property="children"),
            Input(component_id="opCode_dropdown", component_property="value"),
        )
        def update_str(value):
            return OpCode.value_to_string(value)

        return app

    @staticmethod
    def value_to_string(value):
        return f"Operationskod: {', '.join(value) if value else 'Alla'}"
