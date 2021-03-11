import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from asa.asa import *
from anestesi.anestesi import *
from age.age import *


DATA_PATH = "data/data.csv"

app = dash.Dash(external_stylesheets=[dbc.themes.GRID])


app.layout = html.Div(
id='main',
children = [
html.H1(
id='h1',
children='Plando-prototype'),
dbc.Col([asa_widget(), anestesi_widget(), age_widget()])
]
)

@app.callback(
   Output(component_id='eighty', component_property='style'),
   [Input(component_id='age_radio', component_property='value')])


def show_hide_element(visibility_state):
    if visibility_state == 'on':
        return {'display': 'block'}
    if visibility_state == 'off':
        return {'display': 'none'}


app.run_server(debug=True)
