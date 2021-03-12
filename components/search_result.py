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

        Input(component_id='search_button', component_property='n_clicks'),

        Input(component_id='asa_checklist', component_property='value'),

        Input(component_id='opTime_slider', component_property='value'),

        Input(component_id='age', component_property='value'),

        Input(component_id='anestesi_checklist', component_property='value'),

        Input(component_id='statistics_dropdown', component_property='value'),

        Input(component_id='kommuner_radiobuttons', component_property='value'),

        Input(component_id='vardtyp_radiobuttons', component_property='value'),

        Input(component_id='opCode_options', component_property='value')





        )
        def update_data(button, asa, opTime, age, anesthesia, statCode, area, vardtyp, opCode_option):
            ctx = dash.callback_context
            if(ctx.triggered[0]['prop_id'] == 'search_button.n_clicks'):
                print("ASA-klass: {} , Operationstid: {} , Ålder: {} ,\
                Anestesi: {} , Statistikkod: {} , Kommun: {} , Vårdtyp: {} ,\
                        Operationskod-val: {}".format(
                        asa,opTime,age,anesthesia,statCode,area, vardtyp, opCode_option
                        ))

            #TODO, Baserat på inputs ska vi filtrera och returnera data i form av dictionary. 
            return None

        return app
