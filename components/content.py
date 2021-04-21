import dash_bootstrap_components as dbc

from components.active_filters import ActiveFilters
from components.filetype_warning import FiletypeWarning
from components.notes import Notes
from components.patient_count import PatientCount
from components.search_result import SearchResult
from components.detail_view import DetailView


class Content:
    @staticmethod
    def get_component():
        content = dbc.Col(
            children=[
                dbc.Row(
                    children=[
                        ActiveFilters.get_component(),
                        Notes.get_component(),
                        DetailView.get_component(),
                    ],
                    className="justify-content-start ml-0 mr-0",
                ),
                PatientCount.get_component(),
                SearchResult.get_component(),
                FiletypeWarning.get_component(),
            ],
            id="page-content",
            className="scrollable p-2",
            style={"background-color": "var(--c-very-light-blue)"},
        )
        return content
