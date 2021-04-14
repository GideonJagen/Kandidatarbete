import dash
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output

from data_handling import DataFilterer, LoadedData


# TODO Make callback return a dictionary with inputs


class SearchResult:
    @staticmethod
    def get_component():
        cols = [
            "Behandlingsnr",
            "dagar_till_kritisk",
            "Anmälningstidpunkt",
            "Prioritet_dagar",
            "ASAklass",
            "KravtidEfterMinuter",
            "PatientÅlderVidOp",
            # change name of column
        ]

        widget = html.Div(
            children=[
                dash_table.DataTable(
                    id="search_result",
                    page_size=50,
                    style_table={
                        "background-color": "var(--c-very-light-blue)",
                        "height": "50vh",
                        "overflowY": "auto",
                        "width": "100%",
                    },
                    columns=[{"name": col, "id": col} for col in cols],
                    data=None,
                    sort_action="native",
                    fixed_rows={"headers": True},
                    style_data={
                        "border": "0.2em solid grey",
                        "height": "2.8em",
                        "width": "7em",
                        "textAlign": "center",
                    },
                    style_header={
                        "background-color": "#6ea6cd",
                        "fontWeight": "bold",
                        "textAlign": "center",
                    },
                    style_as_list_view=True,
                    style_data_conditional=[
                        {
                            "backgroundColor": "var(--c-very-light-blue)",
                        },
                        {
                            "if": {
                                "filter_query": "{dagar_till_kritisk} <= 180",
                                "column_id": "dagar_till_kritisk",  # Change to desired value
                            },
                            "backgroundColor": "var(--c-yellow)",
                        },
                        {
                            "if": {
                                "filter_query": "{dagar_till_kritisk} <= 60",
                                "column_id": "dagar_till_kritisk",  # Change to desired value
                            },
                            "backgroundColor": "var(--c-orange)",
                        },
                        {
                            "if": {
                                "filter_query": "{dagar_till_kritisk} <= 30",
                                "column_id": "dagar_till_kritisk",  # Change to desired value
                            },
                            "backgroundColor": "var(--c-red)",
                        },
                    ],
                ),
            ],
        )
        return widget

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(component_id="search_result", component_property="data"),
            Output(component_id="number_of_patients", component_property="children"),
            Input(component_id="asa_checklist", component_property="value"),
            Input(component_id="asa_radio_items", component_property="value"),
            Input(component_id="opTime_slider", component_property="value"),
            Input(component_id="age", component_property="value"),
            Input(component_id="anaesthesia_checklist", component_property="value"),
            Input(component_id="statistics_checklist", component_property="value"),
            Input(component_id="statistics_radio_items", component_property="value"),
            Input(component_id="municipalities_radioitems", component_property="value"),
            Input(component_id="care_type_radioitems", component_property="value"),
            Input(component_id="opCode_dropdown", component_property="value"),
        )
        def update_data(
            asa,
            asa_radio,
            op_time,
            age,
            anesthesia,
            stat_code,
            stat_code_radio,
            area,
            care_type,
            op_code,
        ):
            # By inputting a dictionary we allow more specific searches to be done by creating combinations.
            # Might let the user create "shortcuts"/save filters to compare results
            inputs = {
                "age": {"min": age[0], "max": age[1]},
                "asa": asa,
                "asa_radio": asa_radio,
                "op_time": {"min": op_time[0], "max": op_time[1]},
                "op_code": op_code,
                "stat_code": stat_code,
                "stat_code_radio": stat_code_radio,
                "anesthesia": anesthesia,
                "area": area,
                "caretype": care_type,
            }
            result = DataFilterer.search_data(inputs)
            return result["data"], result["number_of_patients"]

        return app
