import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_table
from datetime import date

def upload_widget():
    widget = html.Div(dcc.Upload(
    id='upload-file',
    children = [
        html.A('Choose a file')
    ],
    style={
        'width': '60%',
        'height': '100px',
        'lineHeight': '60px',
        'borderWidth': '2px',
        'borderStyle': 'dashed',
        'borderRadius': '5px',
        'textAlign': 'center',
        'margin': '50px',
        'verticalAlign' : 'center',
        'backgroundColor': 'rgb(250, 242, 195)'
        },
    ),
    )
    return widget



def selectDate_widget():
    widget = dcc.Input(
    id='date-picker',
    type='text',
    placeholder='YYYY-MM-DD',
    maxLength = 10,
    style={
    'height' : '50px',
    'font-size' : '20px',
    'textAlign': 'left',
            'backgroundColor': 'rgb(250, 242, 195)',
            'color' : 'rgb(50, 50, 50)'
    }
    )
    return widget


def booked_operations_widget():
    #cols = ['Date', 'Name', 'Operation-description', 'Surgeon']
    PAGE_SIZE = 250
    cols = ['Operationsdatum', 'BehandlingsNummer']

    widget = children = dash_table.DataTable(
    id = 'booked-operations',
    columns=[{"name": i, "id": i} for i in cols if i != "id"],
    data = None,
    selected_rows=[],
    #row_selectable = "single",
    page_current = 0,
    fixed_rows={ 'headers': True, 'data': 0 },
    page_size = PAGE_SIZE,
    style_header={
    'textAlign': 'left',
    'backgroundColor': 'rgb(83, 199, 240)',
    'color' : 'rgb(50,50,50)'
    },
    style_cell={'textAlign': 'left',
                'backgroundColor': 'rgb(250, 242, 195)',
                    'color' : 'rgb(50, 50, 50)'
        }
    )
    return widget



def load_button_widget():
    widget = html.Button(
    "Load data",
    id="load-button",)
    return widget


def similar_patients_widget():
    #cols = ['Date', 'Name', 'Operation-description', 'Surgeon']
    cols = ['HuvudDiagnosNamn1','Operationskort Undergrupp Namn','Anestesikort']
    widget = children = dash_table.DataTable(
    id = 'similar-patients',
    columns=[{"name": i, "id": i} for i in cols if i != 'id'],
    style_header={'textAlign': 'left',
                'backgroundColor': 'rgb(83, 199, 240)',
                'color' : 'rgb(50, 50, 50)'
    },
    style_cell={'textAlign': 'left',
                'backgroundColor': 'rgb(250, 242, 195)',
                'color' : 'rgb(50, 50, 50)'
    },
    fixed_rows={ 'headers': True, 'data': 0 }
    )
    return widget


def tables_widget():
    widget = dbc.Row(
    [
    html.Div(dbc.Col(booked_operations_widget()), style={'width':'20%',} ),


    html.Div(dbc.Col(similar_patients_widget()), style={'width':'80%'}),
    ]
    )
    return widget
