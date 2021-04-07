import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output


class OpTime:
    STANDARD_VALUE = [10, 200]  # TODO Uppdatera baserat på datan.

    @staticmethod
    def get_component(min_time, max_time):

        widget = dbc.FormGroup(
            id="opTime_widget",
            children=[
                dbc.Label("Operationstid"),
                OpTime._op_time_slider(min_time, max_time),
            ],
        )

        return widget

    @staticmethod
    def _op_time_slider(min_time, max_time):
        widget = dcc.RangeSlider(
            id="opTime_slider",
            min=min_time,
            max=max_time,
            marks={
                i: "{}min".format(i) if (i == min_time or i == max_time) else f"{i}"
                for i in range(min_time, max_time + 20, 20)
            },
            value=OpTime.STANDARD_VALUE,
            step=5,
        )
        return widget

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(component_id="opTime_slider", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_component(n_clicks):
            return OpTime.STANDARD_VALUE

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
