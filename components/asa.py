import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

class Asa_widget():

    @staticmethod
    def asa_widget():
        widget = html.Div(
            id='asa',
            children = [
            html.H4(
            id='asa_h4',
            children='ASA-klass',
            style={
            'borderWidth': '1px',
            'borderStyle': 'solid',
            'margin': '0px'
            }
            ),
            dcc.Checklist(
            id = 'asa_checklist',
            options=[
                    {'label': 'ASA 1', 'value': 'asa1'},
                    {'label': 'ASA 2', 'value': 'asa2'},
                    {'label': 'ASA 3', 'value': 'asa3'},
                    {'label': 'ASA 4', 'value': 'asa4'},
                    {'label': 'ASA 5', 'value': 'asa5'},
                    {'label': 'ASA 6', 'value': 'asa6'},
                    {'label': 'Ej specificerat', 'value': 'es'}
            ],
            labelStyle={'display': 'inline-block'},
            style={
            'width': '100%',
            'borderWidth': '1px',
            'borderStyle': 'solid',
            'margin': '0px'
            }
            )
            ],
            style={
            'width': '15%',
            'borderWidth': '1px',
            'borderStyle': 'solid',
            'textAlign': 'center',
            'margin': '5px'
            }
            )
        return widget
