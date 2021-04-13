import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


class FreeTextSearch:
    @staticmethod
    def get_component():
        widget = dbc.FormGroup(
            id="free_text_search",
            children=[
                dbc.Label(
                    html.Span(
                        [
                            "Nyckelord ",
                            html.I(
                                className="fas fa-info-circle",
                                id="free_text_search_info",
                            ),
                        ]
                    ),
                    className="label col-form-label-lg font-weight-bold mb-n4 pd-n4",
                ),
                FreeTextSearch._free_text_search_tooltip(),
                html.Hr(style={"margin-top": 0, "margin-bottom": 10}),
                dbc.Input(
                    id="free_text_search_input",
                    placeholder="Sök...",
                    type="text",
                    value="",
                    disabled=True,
                ),
            ],
        )
        return widget

    @staticmethod
    def _free_text_search_tooltip():
        tooltip = dbc.Tooltip(
            "Söker efter nyckelord i ”Information till planerare”. "
            "Separera nyckelorden med komma.",
            target="free_text_search_info",
            placement="auto",
            style={
                "text-transform": "none",
            },
        )
        return tooltip

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(component_id="free_text_search_input", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_component(n_clicks):
            return ""

        return app
