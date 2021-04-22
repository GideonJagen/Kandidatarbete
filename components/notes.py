import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from data_handling import LoadedData
import numpy as np


class Notes:
    current_notes = ""
    PLACEHOLDER_MSG = (
        "Fyll i behandlingsnummer på patienten som ska ersättas i rutan ovan."
    )

    @staticmethod
    def get_component():
        widget = dbc.Col(
            className="col-3 ml-3 mr-3",
            children=[Notes._input_row(), Notes._notes_row(), Notes._reset_row()],
        )
        return widget

    @staticmethod
    def _input_row():
        return dbc.Row(
            children=[
                dbc.Input(id="notes_input", placeholder="Tryck ENTER för att söka")
            ]
        )

    @staticmethod
    def _notes_row():
        return dbc.Row(
            style={"height": "75%"},  # why doesnt row classes work?????????
            children=[
                dbc.Textarea(
                    placeholder=Notes.PLACEHOLDER_MSG,
                    readOnly=True,
                    className="shadow-sm",
                    style={
                        "resize": "none",
                        "background-color": "var(--c-light-blue)",
                    },
                    id="notes",
                    bs_size="md",
                )
            ],
        )

    @staticmethod
    def _reset_row():
        return dbc.Row(
            justify="end",
            children=[
                dbc.Button(
                    id="reset_notes",
                    color="link",
                    children="Återställ",
                )
            ],
        )

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(component_id="notes", component_property="value"),
            Output(component_id="notes_input", component_property="value"),
            Output(component_id="notes_input", component_property="invalid"),
            Output(component_id="notes_input", component_property="valid"),
            Input(component_id="reset_notes", component_property="n_clicks"),
            Input(component_id="notes_input", component_property="n_submit"),
            Input(component_id="notes_input", component_property="value"),
        )
        def reset(n_clicks, n_submit, input):
            valid_input = False
            invalid_input = False  # Yes this is how it works.
            input_value = input

            def get_outputs():
                return Notes.current_notes, input_value, invalid_input, valid_input

            context = dash.callback_context

            if context.triggered[0]["prop_id"].split(".")[0] == "reset_notes":
                Notes.current_notes = ""
                input_value = None
                invalid_input = False
                valid_input = False

            elif context.triggered[0]["prop_id"].split(".")[1] == "n_submit":
                if input and input.isnumeric():
                    patient = LoadedData.find_patient(input)
                    if len(patient) > 0:
                        Notes.current_notes = LoadedData.patient_to_string(patient)
                        valid_input = True
                        invalid_input = False
                        input_value = None
                    else:
                        valid_input = False
                        invalid_input = True
                        Notes.current_notes = (
                            f"Ingen patient med behandlingsnummer: {input} hittades."
                        )
                        input_value = None
                else:
                    Notes.current_notes = "Värdet måste vara numeriskt!"
            else:
                input_value = input
            return get_outputs()

        return app
