import dash_bootstrap_components as dbc
from data_handling import LoadedData


class FiletypeWarning:
    @staticmethod
    def get_component():
        widget = dbc.Modal(
            id="filetype-warning",
            is_open=False,
            children=[
                dbc.ModalHeader("File not loaded: wrong filetype"),
                dbc.ModalBody(
                    f"Make sure the file is of type: {LoadedData.CORRECT_FILE_TYPE}"
                ),
                dbc.ModalFooter(
                    children=[dbc.Button("Close", id="filetype_warning_close_button")]
                ),
            ],
        )
        return widget
