import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

def anestesi_widget():
    widget = html.Div(
            id = 'anestesi',
            children = [
            html.H4(
            id = 'anestesi_h4',
            children = 'Anestesibedömning',
            style = {
            'borderWidth': '1px',
            'borderStyle': 'solid',
            'margin': '0px'
            }
            ),
            dcc.Checklist(
            id = 'anestesi_checklist',
            options = [
                    {'label': 'Ej klar', 'value': 'ek'},
                    {'label': 'Påbörjad', 'value': 'pb'},
                    {'label': 'Klar', 'value': 'klar'}
                    ],
            labelStyle = {'display': 'inline-block'},
            style = {
            'width': '100%',
            'borderWidth': '1px',
            'borderStyle': 'solid',
            'margin': '0px'
            }
            )
            ],
            style = {
            'width': '30%',
            'borderWidth': '1px',
            'borderStyle': 'solid',
            'textAlign': 'center',
            'margin': '5px'
            }
            )
    return widget
