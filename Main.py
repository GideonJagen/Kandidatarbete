import dash
import dash_core_components as dcc
import dash_html_components as html
from opTime_selection.opTime_slider import opTime_widget
from opCode_selection.opCode_selection import opCode_selection
import dash_bootstrap_components as dbc
from DataHandler import *


app = dash.Dash(external_stylesheets=[dbc.themes.GRID]) #create Dash object

app.layout = html.Div(
#Top of hierarcy
id='Main',
children=[
opTime_widget(5,120),
opCode_selection(dummy_data['Opkategori_text'].values.tolist())

#Top
]

)




app.run_server(debug=True)
