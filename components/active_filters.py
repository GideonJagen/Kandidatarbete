import dash_bootstrap_components as dbc
import dash_html_components as html

from components.reset_filter_button import ResetFilterButton


class ActiveFilters:
    @staticmethod
    def get_component():
        widget = dbc.Col(
            className="col-5 ml-3 mr-3",
            children=[
                html.H4("Aktiva filter"),
                dbc.Row(ActiveFilters._get_table()),
                dbc.Row(
                    ResetFilterButton.get_component(),
                    justify="end",
                ),
            ],
        )
        return widget

    @staticmethod
    def _get_table():
        table = (
            dbc.Table(
                className="table table-striped shadow-sm",
                style={
                    "background-color": "#c2e4ef",
                    "height": "100%",
                    "margin": "0px",
                },
                bordered=False,
                borderless=True,
                id="active_filters",
                children=[html.Tbody(ActiveFilters._build_rows())],
            ),
        )

        return table

    @staticmethod
    def _build_rows():
        row1 = html.Tr([html.Td(id="active_age"), html.Td(id="active_asa")])
        row2 = html.Tr(
            [html.Td(id="active_anesthesia"), html.Td(id="active_care_type")]
        )
        row3 = html.Tr([html.Td(id="active_op_code"), html.Td(id="active_op_time")])
        row4 = html.Tr(
            [html.Td(id="active_municipalities"), html.Td(id="active_statistics_code")]
        )
        row5 = html.Tr(
            [html.Td(id="active_short_notice"), html.Td(id="active_operator")]
        )
        return [row1, row2, row3, row4, row5]
