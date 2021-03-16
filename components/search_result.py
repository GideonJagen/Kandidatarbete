import dash
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
from DataHandler import filter_data, dummy_data, filter_vectorized

# TODO Make callback return a dictionary with inputs


class SearchResult:
    @staticmethod
    def search_result():
        cols = [
            "Behandlingsnr",
            "Anmälningstidpunkt",
            "SistaOpTidpunkt",
            "Opkategori_text",
            "Prioritet_dagar",
            "ASAklass",
            "KravOperationstidMinuter",
            "KravFörberedelsetidMinuter",
            "KravtidEfterMinuter",
            "De_PlaneradOpsal_FK",
            "PlaneradStartOpsalTidpunkt",
            "PatientÅlderVidOp",
            "Veckodag",
            "Starttimme",
            "TotaltidStart",
        ]

        widget = html.Div(
            style={},
            children=[
                dash_table.DataTable(
                    id="search_result",
                    columns=[{"name": col, "id": col} for col in cols],
                    data=None,
                ),
            ],
        )
        return widget

    @staticmethod
    def search_result_callback(app):
        @app.callback(
            Output(component_id="search_result", component_property="data"),
            Input(component_id="search_button", component_property="n_clicks"),
            Input(component_id="asa_checklist", component_property="value"),
            Input(component_id="opTime_slider", component_property="value"),
            Input(component_id="age", component_property="value"),
            Input(component_id="anestesi_checklist", component_property="value"),
            Input(component_id="statistics_dropdown", component_property="value"),
            Input(component_id="kommuner_radiobuttons", component_property="value"),
            Input(component_id="vardtyp_radiobuttons", component_property="value"),
            Input(component_id="opCode_dropdown", component_property="value"),
            Input(component_id="search_result", component_property="data"),
        )
        def update_data(
            button,
            asa,
            op_time,
            age,
            anesthesia,
            stat_code,
            area,
            vardtyp,
            op_code,
            current_data,
        ):
            inputs = {  # Genom att ta in ett dicitonary som detta kan man skapa kombinationer som därmed kan sökas efter specifikt, kan låta användaren skapa "genvägar"/spara filtrering för att jämföra resultat
                "age": age,
                "asa": asa,
                "op_time": op_time,
                "op_code": op_code,
                "stat_code": stat_code,
                "anesthesia": anesthesia,
                "area": area,
                "vardtyp": vardtyp,
            }
            ctx = dash.callback_context
            if ctx.triggered[0]["prop_id"] == "search_button.n_clicks":
                # TODO, Baserat på inputs ska vi filtrera och returnera data i form av dictionary.
                return filter_vectorized(inputs)
            return filter_vectorized(inputs)

        return app
