import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
from datetime import date

def upload_widget():
    widget = dcc.Upload(
    id='upload-file',

    children = [
        html.A('Choose a file')
    ],
    style={
        'width': '100%',
        'height': '60px',
        'lineHeight': '60px',
        'borderWidth': '1px',
        'borderStyle': 'dashed',
        'borderRadius': '5px',
        'textAlign': 'center',
        'margin': '10px'
        },
    )
    return widget

def selectDate_widget():
    widget = dcc.DatePickerSingle(
    id='date-picker',
    date = None
    )
    return widget


def booked_operations_widget():
    #cols = ['Date', 'Name', 'Operation-description', 'Surgeon']
    cols = ['Operationsdatum', 'BehandlingsNummer']
    widget = dash_table.DataTable(
    id = 'booked-operations',
    columns=[{"name": i, "id": i} for i in cols],
    data = None
    ,
    )
    return widget



def load_button_widget():
    widget = html.Button(
    "Load data",
    id="load-button",)
    return widget




def similar_patients_widget():
    #cols = ['Date', 'Name', 'Operation-description', 'Surgeon']
    cols = ['Operationsdatum', 'BehandlingsNummer']
    widget = dash_table.DataTable(
    id = 'similar-patients',
    columns=[{"name": i, "id": i} for i in cols],
    data = None
    )
    return widget
