import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

from components.age import Age_widget
from components.anestesi import Anestesi_widget
from components.asa import Asa_widget
from components.Reset_and_search import Reset_and_search
from components.kommuner import Kommuner_widget

from tab_selection import tab_selection
<<<<<<< HEAD

=======
import dash_bootstrap_components as dbc
from components.reset_and_search.Reset_and_search import reset_and_search
from search_result.search_result import search_result
>>>>>>> 1d4b5a7c8ef8ea5674e0a25a37e586d4d9a9c3a5

# TODO Kolla upp hur man skulle kunna se värdena på patienten man ska ersätta samtidigt som man letar efter en ny,
#   för att slippa bläddra fram o tillbaka

app = dash.Dash(external_stylesheets=[dbc.themes.GRID])  # create Dash object

app.layout = html.Div(
    # Top of hierarcy
    id='Main',
    children=[
        tab_selection(),
        Reset_and_search.reset_and_search(),

        # TODO: Move this to proper place:
        html.H1(
            id='h1',
            children='Plando-prototype'),
<<<<<<< HEAD
        dbc.Col([
            Asa_widget.asa_widget(),
            Anestesi_widget.anestesi_widget(),
            Age_widget.age_widget(),
            Kommuner_widget.kommuner_widget(),
            ]
        )
=======
        dbc.Col(
            [asa_widget(), anestesi_widget(), age_widget()]
        ),
        search_result(),
>>>>>>> 1d4b5a7c8ef8ea5674e0a25a37e586d4d9a9c3a5

        # Top
    ]
)

app.run_server(debug=True)
