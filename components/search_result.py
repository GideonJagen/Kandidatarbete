import dash_html_components as html
import dash_table
import pandas as pd
from dash.dependencies import Input, Output

from data_filterer import DataFilterer
from data_loader import DataLoader
from resources.constants import Constants


# TODO Make callback return a dictionary with inputs


class SearchResult:
    PAGE_SIZE = 50

    @staticmethod
    def get_component():
        cols = [
            Constants.BEHANDLINGS_NUMMER,
            Constants.KVAR_PRIO_TID,
            Constants.ANM_TIDPUNKT,
            Constants.PRIORITET,
            Constants.ASA_KLASS,
            Constants.OP_TID,
            Constants.PATIENT_ALDER,
            Constants.BENAMNING
            # change name of column
        ]

        widget = html.Div(
            children=[
                dash_table.DataTable(
                    cell_selectable=True,
                    id="search_result",
                    page_size=SearchResult.PAGE_SIZE,
                    page_current=0,
                    style_table={
                        "background-color": "var(--c-very-light-blue)",
                        "height": "50vh",
                        "overflowY": "auto",
                        "width": "100%",
                    },
                    columns=[{"name": col, "id": col} for col in cols],
                    data=None,
                    sort_action=None,
                    fixed_rows={"headers": True},
                    style_data={
                        "border": "0.2em solid grey",
                        "height": "2.8em",
                        "width": "7em",
                        "textAlign": "center",
                    },
                    style_header={
                        "background-color": "var(--c-dark-blue)",
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
                                "filter_query": "{Kvar på prio-tid} <= 180",
                                "column_id": "Kvar på prio-tid",  # Change to desired value
                            },
                            "backgroundColor": "var(--c-yellow)",
                        },
                        {
                            "if": {
                                "filter_query": "{Kvar på prio-tid} <= 60",
                                "column_id": "Kvar på prio-tid",  # Change to desired value
                            },
                            "backgroundColor": "var(--c-orange)",
                        },
                        {
                            "if": {
                                "filter_query": "{Kvar på prio-tid} <= 30",
                                "column_id": "Kvar på prio-tid",  # Change to desired value
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
            Input(component_id="asa_radio_items", component_property="value"),
            Input(component_id="asa_checklist", component_property="value"),
            Input(component_id="op_time_radio_items", component_property="value"),
            Input(component_id="op_time_min", component_property="value"),
            Input(component_id="op_time_max", component_property="value"),
            Input(component_id="age", component_property="value"),
            Input(component_id="anaesthesia_checklist", component_property="value"),
            Input(component_id="priority_checklist", component_property="value"),
            Input(component_id="priority_radio_items", component_property="value"),
            Input(component_id="municipalities_radioitems", component_property="value"),
            Input(component_id="care_type_radioitems", component_property="value"),
            Input(component_id="opCode_dropdown", component_property="value"),
            Input(component_id="filetype-warning", component_property="is_open"),
            Input(component_id="operator_radioitems", component_property="value"),
            Input(component_id="operator_dropdown", component_property="value"),
            Input(
                component_id="operator_include_unassigned_checkbox",
                component_property="checked",
            ),
        )
        def update_data(
            asa_radio,
            asa_class,
            op_time_radio,
            op_time_min,
            op_time_max,
            age,
            anesthesia,
            priority,
            priority_radio,
            area,
            care_type,
            op_code,
            warning_is_open,
            operator_radio,
            assigned_to_operator,
            operator_include_unassigned,
        ):

            inputs = {
                "age": {"min": age[0], "max": age[1]},
                "asa_class": asa_class,
                "asa_radio": asa_radio,
                "op_time": {"min": op_time_min, "max": op_time_max},
                "op_time_radio": op_time_radio,
                "op_code": op_code,
                "priority": priority,
                "priority_radio": priority_radio,
                "anesthesia": anesthesia,
                "area": area,
                "caretype": care_type,
                "operator_radio": operator_radio,
                "assigned_to_operator": assigned_to_operator,
                "operator_include_unassigned": operator_include_unassigned,
            }
            result = DataFilterer.search_data(inputs)
            data = result["data"]
            patient_count = result["number_of_patients"]

            return data, patient_count

        return app
