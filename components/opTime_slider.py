import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

class OpTime_widget():
    STANDARD_VALUE = [5, 120] #standard value for the RangeSlider, change so its dependant on data 
    @staticmethod
    def opTime_widget(min_time, max_time):
        widget = html.Div(
            id='opTime_widget',
            children=[
                html.H4('Operationstid'),
                OpTime_widget._opTime_slider(min_time, max_time),
            ]
        )
        return widget

    @staticmethod
    def _opTime_slider(min_time, max_time):
        widget = dcc.RangeSlider(
            id='opTime_slider',
            min=min_time,
            max=max_time,
            marks={i: '{}min'.format(i) for i in range(min_time, max_time + 5, 5)},
            value = [min_time, max_time],
            step=5
        )
        return widget


    @staticmethod
    def reset_opTime_callback(app):
        @app.callback(
        Output(component_id = 'opTime_slider' , component_property = 'value'),
        Input(component_id = 'reset_filter_button' , component_property = 'n_clicks')
        )
        def reset_opTime(n_clicks):
            return OpTime_widget.STANDARD_VALUE

        return app
