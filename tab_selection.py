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
    value='patient_tab',
    style = {
    'width' : '50%'
    },
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
    value = 'patient_tab',
    children=[
        html.Div(
            style = tab_style,
            children = [
                html.H4('David Johnsson, extremt jävla frisk'),
                #NEXT WIDGET
        ])],
    )
    return widget



def operation_tab():
    widget = dcc.Tab(
    id='operation_tab',
    label='Operation',
    value = 'operation_tab',
    children=[
        html.Div(
            style = tab_style,
            children = [
                opTime_widget(5,120),
                opCode_selection(['NH132', 'SU145', 'LU987','NX132', 'SX145', 'LX987']),
                #NEXT WIDGET
                ],),]
    )
    return widget



def anesthesia_tab():
    widget = dcc.Tab(
    id='anesthesia_tab',
    label = 'Anestesi',
    value = 'anesthesia_tab',
    children = [
        html.Div(
            style = tab_style,
            children = [
                html.H4('Anestesi...'),
                #NEXT WIDGET

        ],),]
    )
    return widget



tab_style = {
    'height': '500px',
    'width' : '50%'
    }
