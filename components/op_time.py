import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


class OpTime:
    MIN_TIME = 0  # TODO Uppdatera baserat på datan.
    MAX_TIME = 180

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
                OpTime._op_time_slider(),
            ],
        )

        return widget

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

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(component_id="opTime_slider", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_component(n_clicks):
            return [OpTime.MIN_TIME, OpTime.MAX_TIME]

        return app

    @staticmethod
    def add_str_callback(app):
        @app.callback(
            Output(component_id="active_op_time", component_property="children"),
            Input(component_id="opTime_slider", component_property="value"),
        )
        def update_str(value):
            return OpTime.value_to_string(value)

        return app

    @staticmethod
    def value_to_string(value):
        return f"Operationstid: {value[0]} - {value[1]}"
