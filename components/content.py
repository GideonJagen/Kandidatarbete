import dash_bootstrap_components as dbc
import dash_html_components as html

from components.active_filters import ActiveFilters
from components.filetype_warning import FiletypeWarning
from components.notes import Notes
from components.patient_count import PatientCount
from components.search_result import SearchResult


class Content:
    @staticmethod
    def get_component():
        content = dbc.Col(
            className="col-8 mr-3",
            children=[
                html.H3(id="h4", children="Plando"),
                dbc.Row(
                    className="row p-1 justify-content-start",
                    children=[ActiveFilters.get_component(), Notes.get_component()],
                ),
                PatientCount.get_component(),
                SearchResult.get_component(),
                FiletypeWarning.get_component(),
            ],
            id="page-content",
        )
        return content
