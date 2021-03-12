import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html


def age_widget():
    widget = html.Div([
        dcc.RadioItems(
            id = 'age_radio',
            options=[
                {'label': '<16', 'value': 'off'},
                {'label': '≥16', 'value': 'on'}
            ],
            value = 'off'
        ),

        #uncheck when not visible?
        html.Div([
            dcc.Checklist(
            id = 'eighty',
            options = [{'label': 'Inkludera patienter över 80', 'value': 'eighty'}],
            labelStyle={'display': 'inline-block'}
            )
        ], style= {'display': 'block'}
        )
        ])
    return widget
