import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

from components.age import AgeWidget
from components.anestesi import AnestesiWidget
from components.asa import AsaWidget
from components.Reset_and_search import ResetAndSearch
from components.kommuner import KommunerWidget

from tab_selection import tab_selection


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
        html.H1(id="h1", children="Plando-prototype"),
        dbc.Col(
            [
                AsaWidget.asa_widget(),
                AnestesiWidget.anestesi_widget(),
                AgeWidget.age_widget(),
                KommunerWidget.kommuner_widget(),
            ]
        )
        # Top
    ],
)

app.run_server(debug=True)
