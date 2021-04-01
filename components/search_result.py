import dash
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
from data_handler import DataFilterer, LoadedData
import dash_bootstrap_components as dbc

# TODO Make callback return a dictionary with inputs


class SearchResult:
    @staticmethod
    def search_result():
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
                                "filter_query": "{dagar_till_kritisk} < 30",  # Change to desired value
                            },
                            "backgroundColor": "#EE7733",
                        },
                        {
                            "if": {
                                "filter_query": "{dagar_till_kritisk} < 3",  # Change to desired value
                            },
                            "backgroundColor": "#CC3311",
                        },
                    ],
                ),
            ],
        )
        return widget

    @staticmethod
    def search_result_callback(app):
        @app.callback(
            Output(component_id="search_result", component_property="data"),
            Output(component_id="number patients", component_property="children"),
            Input(component_id="asa_checklist", component_property="value"),
            Input(component_id="opTime_slider", component_property="value"),
            Input(component_id="age", component_property="value"),
            Input(component_id="anestesi_checklist", component_property="value"),
            Input(component_id="statistics_dropdown", component_property="value"),
            Input(component_id="kommuner_radiobuttons", component_property="value"),
            Input(component_id="vardform_radiobuttons", component_property="value"),
            Input(component_id="opCode_dropdown", component_property="value"),
            Input(component_id="upload", component_property="filename"),
            Input(component_id="upload", component_property="contents"),
        )
        def update_data(
            asa,
            op_time,
            age,
            anesthesia,
            stat_code,
            area,
            vardform,
            op_code,
            filename,
            content,
        ):
            # By inputing a dictionary we allow more specific searchs to be done by creating combinations.
            # Might let the user create "shortcuts"/save filters to compare results
            context = dash.callback_context
            if context.triggered[0]["prop_id"].split(".")[0] == "upload":
                LoadedData.load_data(filename, content)

            inputs = {
                "age": {"min": age[0], "max": age[1]},
                "asa": asa,
                "op_time": {"min": op_time[0], "max": op_time[1]},
                "op_code": op_code,
                "stat_code": stat_code,
                "anesthesia": anesthesia,
                "area": area,
                "vardform": vardform,
            }
            result = DataFilterer.search_data(inputs)

            return result["data"], result["number patients"]

        return app
