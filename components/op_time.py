import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
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
    def add_op_time_callback(app):
        @app.callback(
            Output(component_id="opTime_slider", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_component(n_clicks):
            return OpTime.STANDARD_VALUE

        return app
