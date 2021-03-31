import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


class OperatorWidget:
    STANDARD_VALUE_RI = "all"
    STANDARD_VALUE_DD = None
    STANDARD_VALUE_CB = False
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
                OperatorWidget._operator_radioitems(),
                OperatorWidget._operator_dropdown_and_checkbox(),
            ],
        )
        return widget

    @staticmethod
    def _operator_radioitems():
        options = [
            {"label": "Visa alla", "value": "all"},
            {"label": "Visa endast icke tilldelade patienter", "value": "blank"},
            {"label": "Filtrera efter operatör", "value": "operator"},
        ]

        widget = dbc.RadioItems(
            id="operator_radioitems",
            options=options,
            value=OperatorWidget.STANDARD_VALUE_RI,
        )
        return widget

    @staticmethod
    def _operator_dropdown():
        widget = dcc.Dropdown(
            id="operator_dropdown",
            placeholder="Välj operatör",
            multi=True,
            value=OperatorWidget.STANDARD_VALUE_DD,
            options=[
                {"label": operator, "value": operator}
                for operator in OperatorWidget.STANDARD_OPERATORS
            ],
            style={"display": "block", "min-width": "200px"},
        )
        return widget

    @staticmethod
    def _no_operator_checkbox():
        component = dbc.FormGroup(
            [
                dbc.Checkbox(
                    id="no_operator_checkbox",
                    className="form-check-input",
                    checked=OperatorWidget.STANDARD_VALUE_CB,
                ),
                dbc.Label(
                    "Inkludera även icke tilldelade patienter",
                    html_for="standalone-checkbox",
                    className="form-check-label",
                ),
            ],
            check=True,
        )
        return component

    @staticmethod
    def _operator_dropdown_and_checkbox():
        component = dbc.Form(
            [
                dbc.FormGroup(OperatorWidget._operator_dropdown(), className="mx-3"),
                OperatorWidget._no_operator_checkbox(),
            ],
            style={"visibility": "visible"},
            id="operator_dropdown_and_checkbox",
            inline=True,
        )
        return component

    @staticmethod
    def add_operator_callbacks(app):
        app = OperatorWidget.reset_operator_ri_callback(app)
        app = OperatorWidget.reset_operator_dd_callback(app)
        app = OperatorWidget.reset_operator_cb_callback(app)
        app = OperatorWidget.show_hide_operator_callback(app)
        return app

    @staticmethod
    def reset_operator_ri_callback(app):
        @app.callback(
            Output(component_id="operator_radioitems", component_property="value"),
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
    def reset_operator_cb_callback(app):
        @app.callback(
            Output(component_id="no_operator_checkbox", component_property="checked"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_operator_dd(visibility_state):
            if visibility_state == "all" or visibility_state == "blank":
                return OperatorWidget.STANDARD_VALUE_CB

        return app

    @staticmethod
    def show_hide_operator_callback(app):
        @app.callback(
            Output(
                component_id="operator_dropdown_and_checkbox",
                component_property="style",
            ),
            Input(component_id="operator_radioitems", component_property="value"),
        )
        def show_hide_element(visibility_state):
            if visibility_state == "operator":
                return {"visibility": "visible"}
            if visibility_state == "all" or visibility_state == "blank":
                return {"visibility": "hidden"}

        return app
