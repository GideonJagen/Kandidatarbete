import dash_core_components as dcc
import dash_html_components as html


class OpTimeWidget:
    @staticmethod
    def opTime_widget(min_time, max_time):
        widget = html.Div(
            id="opTime_widget",
            children=[
                html.H4("Operationstid"),
                OpTimeWidget._opTime_slider(min_time, max_time),
            ],
        )
        return widget

    @staticmethod
    def _opTime_slider(min_time, max_time):
        widget = dcc.RangeSlider(
            id="opTime_slider",
            min=min_time,
            max=max_time,
            marks={i: "{}min".format(i) for i in range(min_time, max_time + 5, 5)},
            step=5,
        )
        return widget
