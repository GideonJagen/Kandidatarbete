import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash


class OperatorWidget:
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
                OperatorWidget._operator_collapse(),
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
            value="all",
        )
        return widget

    @staticmethod
    def _operator_dropdown():
        widget = dcc.Dropdown(
            id="operator_dropdown",
            placeholder="Välj operatör",
            multi=True,
            value=None,
            options=[
                {"label": operator, "value": operator}
                for operator in OperatorWidget.STANDARD_OPERATORS
            ],
            style={"display": "block", "min-width": "15em"},
        )
        return widget

    @staticmethod
    def _no_operator_checkbox():
        component = dbc.FormGroup(
            [
                dbc.Checkbox(
                    id="no_operator_checkbox",
                    className="form-check-input",
                    checked=False,
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
    def _operator_collapse():
        widget = dbc.Collapse(
            id="collapse",
            # style={"width": "50em"},
            children=[
                dbc.Form(
                    [
                        dbc.FormGroup(
                            OperatorWidget._operator_dropdown(), className="mx-3"
                        ),
                        OperatorWidget._no_operator_checkbox(),
                    ],
                    style={"visibility": "visible"},
                    id="operator_dropdown_and_checkbox",
                    inline=True,
                )
            ],
        )
        return widget

    @staticmethod
    def add_operator_callback(app):
        @app.callback(
            Output(component_id="collapse", component_property="is_open"),
            Output(component_id="operator_radioitems", component_property="value"),
            Output(component_id="operator_dropdown", component_property="value"),
            Output(component_id="no_operator_checkbox", component_property="checked"),
            Input(component_id="operator_radioitems", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def collapse(value, reset):
            context = dash.callback_context
            if context.triggered[0]["prop_id"].split(".")[0] == "reset_filter_button":
                return False, "all", None, False
            elif value == "operator":
                return True, "operator", None, False
            return (
                False,
                value,
                None,
                False,
            )

        return app
