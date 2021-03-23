import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


class ResetAndSearch:
    @staticmethod
    def reset_and_search():
        widget = html.Div(
            [
                ResetAndSearch._search_button(),
                ResetAndSearch._reset_filter_button(),
            ],
            id="reset_and_search",
        )
        return widget

    @staticmethod
    def _search_button():
        widget = dbc.Button("Filtrera", id="search_button", color="primary")
        return widget

    @staticmethod
    def _reset_filter_button():
        button = dbc.Button("Återställ", id="reset_filter_button", color="danger")
        return button
