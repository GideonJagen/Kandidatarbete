import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

# TODO Make wrapper for callbacks/ make function to add all callbacks
# TODO Make callback for op_code, gör likt statistikkod widget
from components.age import AgeWidget
from components.anestesi import AnestesiWidget
from components.asa import AsaWidget
from components.reset_and_search import ResetAndSearch
from components.kommuner import KommunerWidget
from components.search_result import SearchResult
from components.tab_selection import TabSelectionWidget
from components.vardtyp import VardtypWidget
from components.op_time_slider import OpTimeWidget
from components.statistics_code import StatisticsCodeWidget
from components.op_code_selection import OpCodeSelection
from data_handler import DataHandler

# TODO Kolla upp hur man skulle kunna se värdena på patienten man ska ersätta samtidigt som man letar efter en ny,
#   för att slippa bläddra fram o tillbaka
DataHandler.init_data()  # Should be done by the import data widget
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])  # create Dash object
app.layout = html.Div(
    # Top of hierarcy
    id="Main",
    style={"backgroundColor": "#F7F7F7"},
    children=[
        html.H1(id="h1", children="Plando-prototype"),
        # TabSelectionWidget.filter_tabs(),
        TabSelectionWidget.filter_tabs(),
        ResetAndSearch.reset_and_search(),
        # TODO: Move this to proper place:
        dbc.Col(
            [
                SearchResult.search_result(),
            ]
        )
        # Top
    ],
)

app = SearchResult.search_result_callback(app)
app = OpTimeWidget.add_op_time_callback(app)
app = VardtypWidget.add_vardtyp_callback(app)
app = StatisticsCodeWidget.add_statistics_code_callback(app)
app = AsaWidget.add_asa_callback(app)
app = KommunerWidget.add_kommuner_callback(app)
app = AgeWidget.add_age_callback(app)
app = AnestesiWidget.add_anestesi_callback(app)
app = OpCodeSelection.add_op_code_callback(app)
app.run_server(debug=True)
