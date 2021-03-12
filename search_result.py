import dash
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output


class Search_result():

    @staticmethod
    def search_result():
        cols = ['Behandlingsnr', 'Anmälningstidpunkt', 'SistaOpTidpunkt',
                'Opkategori_text', 'Prioritet_dagar', 'ASAklass', 'KravOperationstidMinuter',
                 'KravFörberedelsetidMinuter','KravtidEfterMinuter', 'De_PlaneradOpsal_FK',
                 'PlaneradStartOpsalTidpunkt', 'PatientÅlderVidOp', 'Veckodag', 'Starttimme', 'TotaltidStart']

        widget = html.Div(
                        style = {},
                        children = [
                            dash_table.DataTable(
                            id = 'search_result',
                            columns = [{'name' : col , 'id' : col } for col in cols],
                            data = None,
                            ),],
        )
        return widget

    @staticmethod
    def search_result_callback(app):
        @app.callback(
        Output(component_id='search_result', component_property='data'),
        Input(),
        Input(),
        Input()
        )
