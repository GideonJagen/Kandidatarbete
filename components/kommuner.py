import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

class Kommuner_widget():
    STANDARD_VALUE = 'all' #
    
    @staticmethod
    def kommuner_widget():
        widget = html.Div(
            id='Antal kommuner?',
            children=[
                html.H4('Kommuner'),
                Kommuner_widget._kommuner_radiobuttons(),
            ]
        )
        return widget

    @staticmethod
    def _kommuner_radiobuttons():
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
