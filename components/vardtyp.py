import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


class VardtypWidget:
    STANDARD_VALUE = "all"

    @staticmethod
    def vardtyp_widget():
        widget = html.Div(
            id="vardtyp",
            children=[
                html.H4("Vårdtyp"),
                VardtypWidget._vardtyp_radiobuttons(),
                # Vardtyp_widget._varvardtyp_dropdown(),
            ],
        )
        return widget

    @staticmethod
    def _vardtyp_radiobuttons():
        options = [
            {"label": "Öppenvård", "value": "open"},
            {"label": "Slutenvård", "value": "closed"},
            {"label": "Visa alla", "value": "all"},
        ]
        widget = dcc.RadioItems(
            id="vardtyp_radiobuttons",
            options=options,
            labelStyle={"display": "block"},
            value="all",
        )
        return widget

    @staticmethod
    def _vardtyp_dropdown(self):
        options = [
            {"label": "Öppenvård", "value": "open"},
            {"label": "Slutenvård", "value": "closed"},
            {"label": "Visa alla", "value": "all"},
        ]
        widget = dcc.Dropdown(
            id="vardtyp_dropdown",
            options=options,
            placeholder="Välj Vårdtyp",
        )
        return widget

    @staticmethod
    def reset_vardtyp_callback(app):
        @app.callback(
            Output(component_id="vardtyp_radiobuttons", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_opTime(n_clicks):
            return VardtypWidget.STANDARD_VALUE

        return app
