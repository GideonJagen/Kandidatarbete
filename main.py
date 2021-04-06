import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State

# TODO Make wrapper for callbacks/ make function to add all callbacks
# TODO Make callback for op_code, gör likt statistikkod widget
# TODO Kolla upp hur man skulle kunna se värdena på patienten man ska ersätta samtidigt som man letar efter en ny,
#   för att slippa bläddra fram o tillbaka

from components.age import Age
from components.anesthesia import Anesthesia
from components.asa import Asa
from components.reset_filter_button import ResetFilterButton
from components.municipalities import Municipalities
from components.search_result import SearchResult
from components.caretype import Caretype
from components.op_time import OpTime
from components.statistics_code import StatisticsCode
from components.op_code import OpCode
from components.operator import Operator
from components.patient_count import PatientCount
from components.short_notice import ShortNotice
from components.sidebar import SideBar
from data_handler import DataFilterer
from components.upload import Upload
from components.warnings import Warnings

# TODO Kolla upp hur man skulle kunna se värdena på patienten man ska ersätta samtidigt som man letar efter en ny,
#   för att slippa bläddra fram o tillbaka

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

content = dbc.Col(
    children=[
        html.H1(id="h1", children="Plando-prototype"),
        Upload.get_component(),  # TODO Hitta bättre plats
        ResetFilterButton.get_component(),
        PatientCount.get_component(),
        SearchResult.get_component(),
        Warnings.get_component(),
    ],
    id="page-content",
)

app.layout = html.Div(
    id="main",
    children=[
        dbc.Row(
            [
                SideBar.get_component(),
                content,
            ],
            className="p-3",
        ),
    ],
)

app = Upload.add_upload_widget_callback(app)
app = Upload.add_load_button_callback(app)
app = SearchResult.search_result_callback(app)
app = OpTime.add_op_time_callback(app)
app = Caretype.add_caretype_callback(app)
app = StatisticsCode.add_statistics_code_callback(app)
app = Asa.add_asa_callback(app)
app = Municipalities.add_municipalities_callback(app)
app = Age.add_age_callback(app)
app = Anesthesia.add_anesthesia_callback(app)
app = OpCode.add_op_code_callback(app)
app = Operator.add_operator_callback(app)
app = SideBar.add_sidebar_callbacks(app)
app = ShortNotice.add_short_notice_collapse_callback(app)
app = ShortNotice.add_short_notice_input_callback(app)
app.run_server(debug=True)
