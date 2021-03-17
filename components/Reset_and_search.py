import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


class ResetAndSearch:
    @staticmethod
    def reset_and_search():
        widget = html.Div(
            id="reset_and_search",
            children=[
                dbc.Row(
                    children=[
                        html.H4("*Uppdateras utan filter knappen för tillfället*"),
                        dbc.Col(children=[ResetAndSearch._reset_filter_button()]),
                        dbc.Col(children=[ResetAndSearch._search_button()]),
                    ]
                )
            ],
            style={"width": "800px"},
        )
        return widget

    @staticmethod
    def _reset_filter_button():
        widget = html.Button(
            "Nollställ filter",
            id="reset_filter_button",
            style={
                "width": "200px",
                "height": "75px",
                "font-size": "16px",
                "background-color": "#CC3311",
            },
        )
        return widget

    @staticmethod
    def _search_button():
        widget = html.Button(
            "Filtrera",
            id="search_button",
            style={
                "width": "200px",
                "height": "75px",
                "font-size": "16px",
                "background-color": "#009988",
            },
        )
        return widget
