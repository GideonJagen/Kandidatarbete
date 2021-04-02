import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

# TODO Make wrapper for callbacks/ make function to add all callbacks
# TODO Make callback for op_code, gör likt statistikkod widget
from components.age import AgeWidget
from components.anestesi import AnestesiWidget
from components.asa import AsaWidget
from components.reset_filter_button import ResetFilterButton
from components.kommuner import KommunerWidget
from components.search_result import SearchResult
from components.tab_selection import TabSelectionWidget
from components.vardform import VardformWidget
from components.op_time_slider import OpTimeWidget
from components.statistics_code import StatisticsCodeWidget
from components.op_code_selection import OpCodeSelection
from data_handler import DataFilterer
from components.upload import UploadWidget
from components.operator import OperatorWidget
from components.number_patients import NumberPatients
from components.short_notice import ShortNoticeWidget

# TODO Kolla upp hur man skulle kunna se värdena på patienten man ska ersätta samtidigt som man letar efter en ny,
#   för att slippa bläddra fram o tillbaka
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])  # create Dash object
app.layout = html.Div(
    # Top of hierarcy
    id="Main",
    style={"backgroundColor": "#F7F7F7"},
    children=[
        html.H1(id="h1", children="Plando-prototype"),
        UploadWidget.upload_widget(),  # TODO Hitta bättre plats
        dbc.Col(
            [
                TabSelectionWidget.filter_tabs(),
                ResetFilterButton.reset_filter_button(),
                ShortNoticeWidget.short_notice_widget(),
                NumberPatients.number_patients(),
                SearchResult.search_result(),
            ]
        )
        # Top
    ],
)

app = SearchResult.search_result_callback(app)
app = OpTimeWidget.add_op_time_callback(app)
app = VardformWidget.add_vardform_callback(app)
app = StatisticsCodeWidget.add_statistics_code_callback(app)
app = AsaWidget.add_asa_callback(app)
app = KommunerWidget.add_kommuner_callback(app)
app = AgeWidget.add_age_callback(app)
app = AnestesiWidget.add_anestesi_callback(app)
app = OpCodeSelection.add_op_code_callback(app)
app = OperatorWidget.add_operator_callbacks(app)
app = ShortNoticeWidget.add_short_notice_collapse_callback(app)
app = ShortNoticeWidget.add_short_notice_input_callback(app)
app.run_server(debug=True)
