import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State

# TODO Make wrapper for callbacks/ make function to add all callbacks
# TODO Make callback for op_code, gör likt statistikkod widget
from components.age import Age
from components.anestesi import Anaesthetic
from components.asa import Asa
from components.reset_filter_button import ResetFilterButton
from components.municipalities import Municipalities
from components.search_result import SearchResult
from components.caretype import Caretype
from components.op_time_slider import OpTime
from components.statistics_code import StatisticsCode
from components.op_code_selection import OpCode
from data_handler import DataHandler
from components.upload import FileUpload
from components.operator import Operator
from components.number_patients import PatientCount
from components.sidebar import SideBar

# TODO Kolla upp hur man skulle kunna se värdena på patienten man ska ersätta samtidigt som man letar efter en ny,
#   för att slippa bläddra fram o tillbaka
DataHandler.init_data()  # Should be done by the import data widget

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])  # create Dash object

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 62.5,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0.5rem 1rem",
    "background-color": "#f8f9fa",
}

SIDEBAR_HIDDEN = {
    "position": "fixed",
    "top": 62.5,
    "left": "-16rem",
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0rem 0rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "transition": "margin-left .5s",
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE1 = {
    "transition": "margin-left .5s",
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

content = html.Div(
    children=[
        html.H1(id="h1", children="Plando-prototype"),
        FileUpload.upload_widget(),  # TODO Hitta bättre plats
        ResetFilterButton.reset_filter_button(),
        PatientCount.patient_counter(),
        SearchResult.search_result(),
    ],
    id="page-content",
    style=CONTENT_STYLE,
)

app.layout = html.Div(
    # Top of hierarcy
    id="main",
    style=CONTENT_STYLE,
    children=[
        dcc.Store(id="side_click"),
        SideBar.sidebar_component(),
        content,
        # Top
    ],
)


@app.callback(
    [
        Output("sidebar", "style"),
        Output("page-content", "style"),
        Output("side_click", "data"),
    ],
    [Input("btn_sidebar", "n_clicks")],
    [
        State("side_click", "data"),
    ],
)
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_style = SIDEBAR_HIDDEN
            content_style = CONTENT_STYLE
            cur_nclick = "HIDDEN"
        else:
            sidebar_style = SIDEBAR_STYLE
            content_style = CONTENT_STYLE
            cur_nclick = "SHOW"
    else:
        sidebar_style = SIDEBAR_STYLE
        content_style = CONTENT_STYLE
        cur_nclick = "SHOW"
    return sidebar_style, content_style, cur_nclick


app = SearchResult.search_result_callback(app)
app = OpTime.add_op_time_callback(app)
app = Caretype.add_caretype_callback(app)
app = StatisticsCode.add_statistics_code_callback(app)
app = Asa.add_asa_callback(app)
app = Municipalities.add_municipalities_callback(app)
app = Age.add_age_callback(app)
app = Anaesthetic.add_anaesthetic_callback(app)
app = OpCode.add_op_code_callback(app)
app = Operator.add_operator_callbacks(app)
app.run_server(debug=True)
