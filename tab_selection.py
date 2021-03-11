import dash_core_components as dcc
from opTime_selection.opTime_slider import opTime_widget
from opCode_selection.opCode_selection import opCode_selection
import dash_html_components as html
def tab_selection():
    """
    Top of tab hierarcy, contains all tabs
    """
    widget = html.Div(children = [dcc.Tabs(
    id='tabs_selection',
    value=None,
    children=[
    patient_tab(),
    anesthesia_tab(),
    operation_tab(),
    ]
    )])
    return widget

def patient_tab():
    widget = dcc.Tab(
    id='patient_tab',
    label='Patient',
    children=[
    html.H4('David Johnsson, extremt jävla frisk')
    ]
    )
    return widget

def operation_tab():
    widget = dcc.Tab(
    id='operation_tab',
    label='Operation',
    children=[
    opTime_widget(5,120),
    opCode_selection(['NH132', 'SU145', 'LU987','NX132', 'SX145', 'LX987']),
    ])
    return widget



def anesthesia_tab():
    widget = dcc.Tab(
    id='anesthesia_tab',
    label = 'Anestesi',
    children = []
    )
    return widget
