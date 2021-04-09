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
            "Anmälningstidpunkt",
            "Prioritet_dagar",
            "ASAklass",
            "KravOperationstidMinuter",
            "KravFörberedelsetidMinuter",
            "KravtidEfterMinuter",
            "PatientÅlderVidOp",
            "dagar_till_kritisk",  # change name of column
        ]

        widget = html.Div(
            style={"height": "800px"},
            children=[
                dash_table.DataTable(
                    id="search_result",
                    page_size=15,
                    style_table={"height": "500px", "overflowY": "auto"},
                    columns=[{"name": col, "id": col} for col in cols],
                    data=None,
                    sort_action="native",
                    style_data_conditional=[
                        {
                            "backgroundColor": "#FFFFFF",
                        },
                        {
                            "if": {
                                "filter_query": "{dagar_till_kritisk} <= 180",
                                "column_id": "dagar_till_kritisk",  # Change to desired value
                            },
                            "backgroundColor": "#228833",
                        },
                        {
                            "if": {
                                "filter_query": "{dagar_till_kritisk} <= 60",
                                "column_id": "dagar_till_kritisk",  # Change to desired value
                            },
                            "backgroundColor": "#CCBB44",
                        },
                        {
                            "if": {
                                "filter_query": "{dagar_till_kritisk} <= 30",
                                "column_id": "dagar_till_kritisk",  # Change to desired value
                            },
                            "backgroundColor": "#EE6677",
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
            Output(component_id="opCode_dropdown", component_property="options"),
            Input(component_id="asa_checklist", component_property="value"),
            Input(component_id="opTime_slider", component_property="value"),
            Input(component_id="age", component_property="value"),
            Input(component_id="anaesthesia_checklist", component_property="value"),
            Input(component_id="statistics_dropdown", component_property="value"),
            Input(component_id="municipalities_radioitems", component_property="value"),
            Input(component_id="care_type_radioitems", component_property="value"),
            Input(component_id="opCode_dropdown", component_property="value"),
            Input(component_id="load_button", component_property="n_clicks"),
        )
        def update_data(
            asa,
            op_time,
            age,
            anesthesia,
            stat_code,
            area,
            care_type,
            op_code,
            load_button,
        ):
            # By inputing a dictionary we allow more specific searchs to be done by creating combinations.
            # Might let the user create "shortcuts"/save filters to compare results
            unique = [
                {"label": code, "value": code}
                for code in LoadedData.get_unique_values("OpkortText")
            ]
            inputs = {
                "age": {"min": age[0], "max": age[1]},
                "asa": asa,
                "op_time": {"min": op_time[0], "max": op_time[1]},
                "op_code": op_code,
                "stat_code": stat_code,
                "anesthesia": anesthesia,
                "area": area,
                "caretype": care_type,
            }
            result = DataFilterer.search_data(inputs)

            return result["data"], result["number_of_patients"], unique

        return app
