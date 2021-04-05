import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash
import dash_html_components as html
from dash.dependencies import Input, Output
from data_handler import LoadedData

# Todo to avoid an even more massive callback (search_result) i decided to add a button with the functionality
# of actually loading the file. When a file is selected, the widget stores it but it is not acctually loaded until
# the load button is pressed, this way we can also avoid loading incorrect file and display messages at the same time.
#


class UploadWidget:
    @staticmethod
    def upload_widget():
        upload = dbc.FormGroup(
            style={"padding": "1em"},
            children=[
                dcc.Upload(
                    id="upload",
                    children=[dbc.Label(id="file-label", children=["Välj ny fil"])],
                ),
                dbc.Collapse(
                    id="load_collapse",
                    # TODO gör typ grön när datan visas, dvs när knappen klickas
                    children=[dbc.Button(id="load_button", children=["Visa data"])],
                ),
            ],
        )
        return upload

    @staticmethod
    def add_upload_widget_callback(app):
        @app.callback(
            Output(component_id="load_collapse", component_property="is_open"),
            Output(component_id="file-label", component_property="children"),
            Output(component_id="filetype-warning", component_property="is_open"),
            Input(component_id="upload", component_property="filename"),
            Input(
                component_id="filetype_warning_close_button",
                component_property="n_clicks",
            ),
            prevent_initial_call=True,
        )
        def show_load_button(filename, n_clicks):
            if isinstance(filename, str) and filename.endswith(".csv"):
                return True, filename, False
            context = dash.callback_context
            if (
                context.triggered[0]["prop_id"].split(".")[0]
                == "filetype_warning_close_button"
            ):
                return False, "Välj ny fil", False
            return False, "Välj ny fil", True

        return app
