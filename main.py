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
from components.upload import UploadWidget
from components.operator import Operator
from components.number_patients import PatientCount
from components.short_notice import ShortNotice
from components.sidebar import SideBar
from data_handler import DataFilterer

# TODO Kolla upp hur man skulle kunna se värdena på patienten man ska ersätta samtidigt som man letar efter en ny,
#   för att slippa bläddra fram o tillbaka

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

content = dbc.Col(
    children=[
        html.H1(id="h1", children="Plando-prototype"),
        UploadWidget.upload_widget(),  # TODO Hitta bättre plats
        ResetFilterButton.reset_filter_button(),
        PatientCount.patient_counter(),
        SearchResult.search_result(),
    ],
    id="page-content",
)

app.layout = html.Div(
    id="main",
    children=[
        dbc.Row(
            [
                SideBar.sidebar_component(),
                content,
            ],
            className="p-3",
        ),
    ],
)


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
app = SideBar.add_sidebar_callbacks(app)
app = ShortNotice.add_short_notice_collapse_callback(app)
app = ShortNotice.add_short_notice_input_callback(app)
app.run_server(debug=True)
