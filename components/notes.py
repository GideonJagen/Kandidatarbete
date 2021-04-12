import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash


class Notes:
    current_notes = ""

    @staticmethod
    def get_component():
        widget = dbc.Col(
            className="col-3 ml-3 mr-3",
            children=[
                dbc.Row(
                    children=[
                        dbc.Input(id="notes_input", placeholder="Press ENTER to submit")
                    ]
                ),
                dbc.Row(
                    style={"height": "75%"},  # why doesnt row classes work?????????
                    children=[
                        dbc.Textarea(
                            readOnly=True,
                            className="shadow-sm",
                            style={
                                "resize": "none",
                                "background-color": "#c2e4ef",
                            },
                            id="notes",
                            placeholder="",
                            bs_size="md",
                        )
                    ],
                ),
                dbc.Row(
                    justify="end",
                    children=[
                        dbc.Button(
                            id="reset_notes",
                            color="link",
                            children="Återställ",
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
            Output(component_id="notes_input", component_property="value"),
            Input(component_id="reset_notes", component_property="n_clicks"),
            Input(component_id="notes_input", component_property="n_submit"),
            Input(component_id="notes_input", component_property="value"),
        )
        def reset(n_clicks, n_submit, note):
            context = dash.callback_context

            if context.triggered[0]["prop_id"].split(".")[0] == "reset_notes":
                Notes.current_notes = ""
                return Notes.current_notes, None
            elif context.triggered[0]["prop_id"].split(".")[1] == "n_submit":
                if note:
                    Notes.current_notes += f"• {note} \n"
                return Notes.current_notes, None
            return Notes.current_notes, note

        return app
