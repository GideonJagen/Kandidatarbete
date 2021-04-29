import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


class Operator:
    STANDARD_OPERATORS = [
        "Clara",
        "David",
        "Gideon",
        "Johan",
        "Linnea",
        "Raoul",
    ]  # Made up for testing purposes

    @staticmethod
    def get_component():
        widget = dbc.FormGroup(
            children=[
                dbc.Label(
                    "Operatör",
                    className="label col-form-label-lg font-weight-bold mb-n4 pd-n4",
                ),
                html.Hr(style={"margin-top": 0, "margin-bottom": 10}),
                Operator._operator_radioitems(),
                Operator._operator_collapse(),
            ],
        )
        return widget

    @staticmethod
    def _operator_radioitems():
        options = [
            {"label": "Visa alla", "value": "all"},
            {
                "label": "Visa endast icke tilldelade patienter",
                "value": "blank",
            },
            {
                "label": "Filtrera efter operatör",
                "value": "operator",
            },
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
                for operator in Operator.STANDARD_OPERATORS
            ],
            style={"display": "block", "min-width": "15em"},
        )
        return widget

    @staticmethod
    def _operator_include_unassigned_checkbox():
        component = dbc.FormGroup(
            [
                dbc.Checkbox(
                    id="operator_include_unassigned_checkbox",
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
            id="operator_collapse",
            children=[
                dbc.Form(
                    [
                        dbc.FormGroup(Operator._operator_dropdown(), className="mx-3"),
                        Operator._operator_include_unassigned_checkbox(),
                    ],
                    style={"visibility": "visible"},
                    id="operator_dropdown_and_checkbox",
                    inline=True,
                )
            ],
        )
        return widget

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(component_id="operator_collapse", component_property="is_open"),
            Output(component_id="operator_radioitems", component_property="value"),
            Output(component_id="operator_dropdown", component_property="value"),
            Output(
                component_id="operator_include_unassigned_checkbox",
                component_property="checked",
            ),
            Input(component_id="operator_radioitems", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def collapse(value, reset):
            collapse_is_open = False
            radio_items = value
            dropdown_value = None
            operator_include_unassigned_checkbox = False

            def get_output():
                return (
                    collapse_is_open,
                    radio_items,
                    dropdown_value,
                    operator_include_unassigned_checkbox,
                )

            context = dash.callback_context
            if context.triggered[0]["prop_id"].split(".")[0] == "reset_filter_button":
                radio_items = "all"
                return get_output()

            elif value == "operator":
                collapse_is_open = True
                return get_output()

            return get_output()

        return app

    @staticmethod
    def add_str_callback(app):
        @app.callback(
            Output(component_id="active_operator", component_property="children"),
            Input(component_id="operator_dropdown", component_property="value"),
        )
        def update_str(value):
            return Operator.value_to_string(value)

        return app

    @staticmethod
    def value_to_string(value):
        return f"Operatör: {value if value else 'Alla'}"
