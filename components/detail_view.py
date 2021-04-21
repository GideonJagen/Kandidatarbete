import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from data_handling import LoadedData
from resources.constants import Constants
import numpy as np


class DetailView:
    current_notes = ""

    @staticmethod
    def get_component():
        widget = dbc.Col(
            className="col-3 ml-3 mr-3",
            children=[
                dbc.Row(
                    style={"height": "90%"},  # why doesnt row classes work?????????
                    children=[
                        dbc.Textarea(
                            id="detail-view",
                            readOnly=True,
                            className="shadow-sm",
                            style={
                                "resize": "none",
                                "background-color": "var(--c-light-blue)",
                            },
                            bs_size="md",
                        )
                    ],
                )
            ],
        )
        return widget

    @staticmethod
    def _row_to_string(data):

        return (
            f"Namn: David \n"
            f"Behandlingsnummer: {data[Constants.BEHANDLINGS_NUMMER]} \n"
            f"Info till planerare: \n"
            f"Kommun: \n"
        )

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(component_id="detail-view", component_property="value"),
            Input(component_id="search_result", component_property="selected_cells"),
            Input(component_id="search_result", component_property="page_size"),
            Input(component_id="search_result", component_property="page_current"),
            prevent_initial_callback=True,
        )
        def update_detail_view(row, page_size, page_nr):
            if row:
                row = row[0]["row"]
                true_row_nr = page_nr * page_size + row
                data = LoadedData.loaded_data.iloc[true_row_nr]
                return DetailView._row_to_string(data)
            return ""

        return app
