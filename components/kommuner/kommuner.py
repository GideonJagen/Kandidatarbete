import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

def kommuner_widget():
    widget = html.Div(
        id='Antal kommuner?',
        children=[
            html.H4('Kommuner'),
            kommuner_radiobuttons(),
        ]
    )
    return widget

def kommuner_radiobuttons():
    options = [
        {'label':'Hela VGR', 'value':'all'},
        {'label':'Kranskommuner', 'value':'close'},
    ]
    widget = dcc.RadioItems(
        id='kommuner_radiobuttons',
        options=options,
        labelStyle={'display':'block'},
        value='all',
     )
    return widget