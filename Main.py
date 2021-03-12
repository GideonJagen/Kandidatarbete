import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

from components.age import AgeWidget
from components.anestesi import AnestesiWidget
from components.asa import AsaWidget
from components.Reset_and_search import ResetAndSearch
from components.kommuner import KommunerWidget
from components.search_result import SearchResult
from tab_selection import tab_selection
from components.vardtyp import VardtypWidget
from components.opTime_slider import OpTimeWidget
from components.statistics_code import StatisticsCodeWidget


# TODO Kolla upp hur man skulle kunna se värdena på patienten man ska ersätta samtidigt som man letar efter en ny,
#   för att slippa bläddra fram o tillbaka

app = dash.Dash(external_stylesheets=[dbc.themes.GRID])  # create Dash object

app.layout = html.Div(
    # Top of hierarcy
    id="Main",
    children=[
        tab_selection(),
        ResetAndSearch.reset_and_search(),
        # TODO: Move this to proper place:
        html.H1(
            id='h1',
            children='Plando-prototype'),
        dbc.Col([
            AsaWidget.asa_widget(),
            AnestesiWidget.anestesi_widget(),
            AgeWidget.age_widget(),
            KommunerWidget.kommuner_widget(),
            SearchResult.search_result(),


            ]
        )

        # Top
    ],
)

app = SearchResult.search_result_callback(app)
app = OpTimeWidget.reset_opTime_callback(app)
app = VardtypWidget.reset_vardtyp_callback(app)
app = StatisticsCodeWidget.reset_statistics_code_callback(app)
app = AsaWidget.reset_asa_callback(app)
app = KommunerWidget.reset_kommuner_callback(app)
app = AgeWidget.reset_age_callback(app)
app = AnestesiWidget.reset_anestesi_callback(app)
app.run_server(debug=True)
