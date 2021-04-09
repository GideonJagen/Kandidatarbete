import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


class Municipalities:
    STANDARD_VALUE = "Hela VGR"

    @staticmethod
    def get_component():
        widget = dbc.FormGroup(
            children=[
                dbc.Label(
                    html.Span(
                        [
                            "Kommuner ",
                            html.I(
                                className="fas fa-info-circle", id="municipalities_info"
                            ),
                        ]
                    ),
                    className="label col-form-label-lg font-weight-bold mb-n4 pd-n4",
                ),
                Municipalities._municipalities_tooltip(),
                html.Hr(style={"margin-top": 0, "margin-bottom": 10}),
                Municipalities._municipalities_radioitems(),
            ],
        )
        return widget

    @staticmethod
    def _municipalities_radioitems():
        options = [
            {"label": "Hela VGR", "value": "Hela VGR"},
            {"label": "Kranskommuner", "value": "Kranskommuner"},
        ]

        widget = dbc.RadioItems(
            id="municipalities_radioitems",
            options=options,
            value=Municipalities.STANDARD_VALUE,
        )
        return widget

    @staticmethod
    def _municipalities_tooltip():
        tooltip = dbc.Tooltip(
            "”Kranskommuner” inkluderar: Härryda, Partille, Öckerö, "
            "Stenungsund, Tjörn, Orust, Färgelanda, Ale, Lerum, "
            "Vårgårda, Bollebygd, Tranemo, Lilla Edet, Mark, Svenljunga, "
            "Herrljunga, Göteborg, Mölndal, Kungälv, Lysekil, Uddevalla, "
            "Vänersborg, Trollhättan, Alingsås, Borås, Ulricehamn",
            target="municipalities_info",
            placement="auto",
            style={
                "text-transform": "none",
            },
        )
        return tooltip

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(
                component_id="municipalities_radioitems", component_property="value"
            ),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_component(n_clicks):
            return Municipalities.STANDARD_VALUE

        return app

    @staticmethod
    def add_str_callback(app):
        @app.callback(
            Output(component_id="active_municipalities", component_property="children"),
            Input(component_id="municipalities_radioitems", component_property="value"),
        )
        def update_str(value):
            return Municipalities.value_to_string(value)

        return app

    @staticmethod
    def value_to_string(value):
        return f"Kommuner: {value}"
