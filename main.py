import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

from components.age import Age
from components.anesthesia import Anesthesia
from components.asa import Asa
from components.care_type import CareType
from components.file_upload import FileUpload
from components.municipalities import Municipalities
from components.op_code import OpCode
from components.op_time import OpTime
from components.operator import Operator
from components.patient_count import PatientCount
from components.reset_filter_button import ResetFilterButton
from components.search_result import SearchResult
from components.short_notice import ShortNotice
from components.sidebar import Sidebar
from components.statistics_code import StatisticsCode
from components.warnings import Warnings
from components.active_filters import ActiveFilters

# TODO Make wrapper for callbacks/ make function to add all callbacks
# TODO Make callback for op_code, gör likt statistikkod widget
# TODO Kolla upp hur man skulle kunna se värdena på patienten man ska ersätta samtidigt som man letar efter en ny,
#   för att slippa bläddra fram o tillbaka

# TODO Kolla upp hur man skulle kunna se värdena på patienten man ska ersätta samtidigt som man letar efter en ny,
#   för att slippa bläddra fram o tillbaka

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

content = dbc.Col(
    children=[
        html.H1(id="h1", children="Plando-prototype"),
        ActiveFilters.get_component(),
        FileUpload.get_component(),  # TODO Hitta bättre plats
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
                Sidebar.get_component(),
                content,
            ],
            className="p-3",
        ),
    ],
)

app = FileUpload.add_callback(app)
app = FileUpload.add_load_button_callback(app)
app = SearchResult.add_callback(app)
app = OpTime.add_callback(app)
app = CareType.add_callback(app)
app = StatisticsCode.add_callback(app)
app = Asa.add_callback(app)
app = Municipalities.add_callback(app)
app = Age.add_callback(app)
app = Anesthesia.add_callback(app)
app = OpCode.add_callback(app)
app = Operator.add_callback(app)
app = Sidebar.add_callback(app)
app = ShortNotice.add_input_callback(app)
app = ShortNotice.add_collapse_callback(app)
app = Age.add_str_callback(app)
app = Anesthesia.add_str_callback(app)
app = Asa.add_str_callback(app)
app = CareType.add_str_callback(app)
app = Municipalities.add_str_callback(app)
app = OpCode.add_str_callback(app)
app = OpTime.add_str_callback(app)
app = Operator.add_str_callback(app)
app = ShortNotice.add_str_callback(app)
app = StatisticsCode.add_str_callback(app)


app.run_server(debug=True)
