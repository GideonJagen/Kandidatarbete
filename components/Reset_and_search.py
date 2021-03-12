import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

class Reset_and_search():

    @staticmethod
    def reset_and_search():
        widget = html.Div(
        id = 'reset_and_search',
        children = [
        dbc.Row(
        children=[
        dbc.Col(children=[Reset_and_search.reset_filter_button()]),
        dbc.Col(children=[Reset_and_search.search_button()]),
        ])],
        style = {
        'width' : '500px'
        }
        )
        return widget

    @staticmethod
    def reset_filter_button():
        widget = html.Button(
        'Nollställ filter',
        id='reset_filter_button',
        style={
        'width' : '200px',
        'height' : '75px',
        'font-size': '16px',
        'background-color' : '#CC3311'
        }
        )
        return widget


    @staticmethod
    def search_button():
        widget = html.Button(
        'Filtrera',
        id='search_button',
        style={
        'width' : '200px',
        'height' : '75px',
        'font-size': '16px',
        'background-color' : '#009988'
        }
        )
        return widget
