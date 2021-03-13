import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd


class OpCodeSelection:
    STANDARD_VALUE_DD = None
    STANDARD_VALUE_OPT = "Visa alla"

    @staticmethod
    def opCode_selection(opCodes):
        """
        Highest hierarcy widget of opCode_selection function
        """
        widget = html.Div(
            id="opCode_selection",
            children=[
                html.H4("Operationskod"),
                OpCodeSelection._opCode_options(),
                OpCodeSelection._opCode_dropdown(opCodes),
            ],
        )
        return widget

    @staticmethod
    def _opCode_options():
        """
        Check buttons of top hierarcy widget
        """

        options = ["Visa alla", "Exkludera", "Visa endast"]
        widget = dcc.RadioItems(
            id="opCode_options",
            options=[{"label": opt, "value": opt} for opt in options],
            labelStyle={"display": "inline-block"},
        )
        return widget

    @staticmethod
    def _opCode_dropdown(opCodes):
        """
        Dropdown list of top hierarcy widget
        """

        widget = dcc.Dropdown(
            id="opCode_dropdown",
            searchable=False,
            placeholder="Välj operationskod",
            options=[
                {"label": code, "value": code} for code in opCodes
            ],  # list builder to create dropdown options,
        )
        return widget
