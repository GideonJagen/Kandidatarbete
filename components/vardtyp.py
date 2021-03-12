import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html


class VardtypWidget:
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
