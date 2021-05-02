import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash


class OpTime:
    MIN_TIME = 0  # TODO Uppdatera baserat på datan.
    MAX_TIME = 200

    @staticmethod
    def get_component():

        widget = dbc.FormGroup(
            id="opTime_widget",
            children=[
                dbc.Label(
                    "Operationstid",
                    className="label col-form-label-lg font-weight-bold mb-n4 pd-n4",
                ),
                html.Hr(style={"margin-top": 0, "margin-bottom": 10}),
                # OpTime._op_time_slider(),
                OpTime._op_time_radio(),
                OpTime._op_time_collapse(),
            ],
        )

        return widget

    @staticmethod
    def _op_time_radio():
        options = [
            {"label": "Visa alla", "value": "all"},
            {"label": "Välj:", "value": "interval"},
        ]
        component = dbc.RadioItems(
            id="op_time_radio_items",
            options=options,
            value="all",
        )
        return component

    @staticmethod
    def _op_time_collapse():
        component = dbc.Collapse(
            id="op_time_collapse",
            children=[
                dbc.InputGroup(
                    [
                        dbc.Input(
                            id="op_time_min",
                            placeholder="Min tid",
                            type="number",
                            min=0,
                        ),
                        dbc.Input(
                            id="op_time_max",
                            placeholder="Max tid",
                            type="number",
                            min=0,
                        ),
                    ]
                )
            ],
        )
        return component

    @staticmethod
    def _op_time_slider():
        widget = dcc.RangeSlider(
            id="opTime_slider",
            min=OpTime.MIN_TIME,
            max=OpTime.MAX_TIME,
            marks={
                i: "{}min".format(i)
                if (i == OpTime.MIN_TIME or i == OpTime.MAX_TIME)
                else f"{i}"
                for i in range(OpTime.MIN_TIME, OpTime.MAX_TIME + 20, 20)
            },
            value=[OpTime.MIN_TIME, OpTime.MAX_TIME],
            step=20,
        )
        return widget

    # @staticmethod
    # def add_callback(app):
    #    @app.callback(
    #        Output(component_id="opTime_slider", component_property="value"),
    #        Input(component_id="reset_filter_button", component_property="n_clicks"),
    #    )
    #    def reset_component(n_clicks):
    #        return [OpTime.MIN_TIME, OpTime.MAX_TIME]

    #    return app

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(component_id="op_time_collapse", component_property="is_open"),
            Output(component_id="op_time_min", component_property="value"),
            Output(component_id="op_time_max", component_property="value"),
            Output(component_id="op_time_radio_items", component_property="value"),
            Input(component_id="op_time_radio_items", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def collapse(value, reset):
            context = dash.callback_context
            if context.triggered[0]["prop_id"].split(".")[0] == "reset_filter_button":
                return False, None, None, "all"
            elif value == "interval":
                return True, None, None, "interval"
            return (
                False,
                None,
                None,
                "all",
            )  # Just to be sure one item is always selected, looks better

        return app

    @staticmethod
    def add_input_callback(app):
        @app.callback(
            Output(component_id="op_time_min", component_property="valid"),
            Output(component_id="op_time_min", component_property="invalid"),
            Output(component_id="op_time_max", component_property="valid"),
            Output(component_id="op_time_max", component_property="invalid"),
            Input(component_id="op_time_min", component_property="value"),
            Input(component_id="op_time_max", component_property="value"),
        )
        def is_valid_input(min_val, max_val):
            """
            This is not a joke, valid and invalid are actually two different properties....... lol
            But other than looking good, we can use the bool of valid input in filtering.
            Let user put in max in wrong box? and just give filter by taking max and min of both?
            """
            min_valid = False
            min_invalid = True
            max_valid = False
            max_invalid = True
            if isinstance(min_val, str):
                min_valid = min_val.isnumeric()
                min_invalid = not min_valid
            if isinstance(max_val, str):
                max_valid = max_val.isnumeric()
                max_invalid = not max_valid
            return min_valid, min_invalid, max_valid, max_invalid

        return app

    @staticmethod
    def add_str_callback(app):
        @app.callback(
            Output(component_id="active_op_time", component_property="children"),
            Input(component_id="op_time_min", component_property="value"),
            Input(component_id="op_time_max", component_property="value"),
        )
        def update_str(value_min, value_max):
            return OpTime.value_to_string(value_min, value_max)

        return app

    @staticmethod
    def value_to_string(value_min, value_max):
        return f"Operationstid: {value_min if value_min else 0} - {value_max if value_max else 'Max' } minuter"
