import dash
import dash_core_components as dcc
import dash_html_components as html
from tab_selection import tab_selection
import dash_bootstrap_components as dbc
from DataHandler import *
from opTime_selection.opTime_slider import opTime_widget
from opCode_selection.opCode_selection import opCode_selection

#TODO Kolla upp hur man skulle kunna se värdena på patienten man ska ersätta samtidigt som man letar efter en ny,
#   för att slippa bläddra fram o tillbaka

app = dash.Dash(external_stylesheets=[dbc.themes.GRID]) #create Dash object

app.layout = html.Div(
#Top of hierarcy
id='Main',
children=[
tab_selection()

#Top
]
)




app.run_server(debug=True)
