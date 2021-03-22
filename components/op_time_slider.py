import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


class OpTimeWidget:
    STANDARD_VALUE = [5, 120]  # TODO Uppdatera baserat på datan.

    @staticmethod
    def op_time_widget(min_time, max_time):
        widget = html.Div(
            id="opTime_widget",
            children=[
                html.H4("Operationstid"),
                dbc.Col(
                    [OpTimeWidget._op_time_slider(min_time, max_time)],
                    style={"width": "50%"},
                ),
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
                for i in range(min_time, max_time + 5, 5)
            },
            value=OpTimeWidget.STANDARD_VALUE,
            step=5,
        )
        return widget

    @staticmethod
    def add_op_time_callback(app):
        @app.callback(
            Output(component_id="opTime_slider", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_op_time(n_clicks):
            return OpTimeWidget.STANDARD_VALUE

        return app