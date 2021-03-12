import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

dcc.RangeSlider(
    min=0,
    max=10,
    step=None,
    marks={
        0: '0 °F',
        3: '3 °F',
        5: '5 °F',
        7.65: '7.65 °F',
        10: '10 °F'
    },
    value=[3, 7.65]
)


def age_widget():
    widget = html.Div([
        dcc.RangeSlider(
            min=0,
            max=10,
            step=None,
            marks={
                0: '0',
                2: '16',
                8: '80',
                10: 'max'
            },
            value=[0,10]
        )
        ])
    return widget
