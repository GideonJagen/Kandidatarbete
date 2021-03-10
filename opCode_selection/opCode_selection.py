import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd



def opCode_selection(opCodes):
    """
    Highest hierarcy widget of opCode_selection function
    """
    widget = html.Div(
    id='opCode_selection',
    children=[
    html.H4('Operationskod'),
    opCode_options(),
    opCode_dropdown(opCodes)
    ]
    )
    return widget



def opCode_options():
    """
    Check buttons of top hierarcy widget
    """

    options = ['Visa alla' , 'Exkludera' , "Visa endast"]
    widget = dcc.RadioItems(
    id='opCode_options',
    options = [{'label' : opt , 'value' : opt} for opt in options],
    labelStyle={'display': 'inline-block'}
    )
    return widget



def opCode_dropdown(opCodes):
    """
    Dropdown list of top hierarcy widget
    """

    widget = dcc.Dropdown(
    id='opCode_dropdown',
    searchable = False,
    placeholder = 'Välj operationskod',
    options = [{'label' : code , 'value' : code} for code in opCodes] #list builder to create dropdown options,
    )
    return widget
