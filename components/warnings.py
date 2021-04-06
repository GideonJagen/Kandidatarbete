import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


class Warnings_widget:
    @staticmethod
    def filetype_warning_widget():
        widget = dbc.Modal(
            id="filetype-warning",
            is_open=False,
            children=[
                dbc.ModalHeader("File not loaded: wrong filetype"),
                dbc.ModalBody("Make sure the file is of type: .csv"),
                dbc.ModalFooter(
                    children=[dbc.Button("Close", id="filetype_warning_close_button")]
                ),
            ],
        )
        return widget
