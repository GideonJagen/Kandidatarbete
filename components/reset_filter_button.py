import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


class ResetFilterButton:
    @staticmethod
    def reset_filter_button():
        button = dbc.Button("Återställ", id="reset_filter_button", color="danger")
        return button
