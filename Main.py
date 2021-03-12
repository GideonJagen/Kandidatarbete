import dash
import dash_html_components as html

from components.age.age import age_widget
from components.anestesi.anestesi import anestesi_widget
from components.asa.asa import asa_widget
from tab_selection import tab_selection
import dash_bootstrap_components as dbc
from components.reset_and_search.Reset_and_search import reset_and_search
from search_result.search_result import search_result

# TODO Kolla upp hur man skulle kunna se värdena på patienten man ska ersätta samtidigt som man letar efter en ny,
#   för att slippa bläddra fram o tillbaka

app = dash.Dash(external_stylesheets=[dbc.themes.GRID])  # create Dash object

app.layout = html.Div(
    # Top of hierarcy
    id='Main',
    children=[
        tab_selection(),
        reset_and_search(),

        # TODO: Move this to proper place:
        html.H1(
            id='h1',
            children='Plando-prototype'),
        dbc.Col(
            [asa_widget(), anestesi_widget(), age_widget()]
        ),
        search_result(),

        # Top
    ]
)

app.run_server(debug=True)
