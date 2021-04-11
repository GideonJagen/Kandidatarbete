import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


class Notes:
    current_notes = None

    @staticmethod
    def get_component():
        widget = dbc.Col(
            className="col-3 ml-3 mr-3",
            children=[
                dbc.Row(
                    style={"height": "10%"},
                    justify="end",
                    children=[
                        dbc.Button(
                            id="reset_notes",
                            color="link",
                            children="Återställ",
                            style={"height": "2.5em"},
                        )
                    ],
                ),
                dbc.Row(
                    style={"height": "90%"},
                    children=[
                        dbc.Textarea(
                            className="shadow-sm",
                            style={"resize": "none"},
                            id="notes",
                            placeholder="Anteckningar...",
                            bs_size="md",
                        )
                    ],
                ),
            ],
        )
        return widget

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(component_id="notes", component_property="value"),
            Input(component_id="reset_notes", component_property="n_clicks"),
        )
        def reset(n_clicks):
            return None

        return app
