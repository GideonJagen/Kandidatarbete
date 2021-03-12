import dash
import dash_table
import dash_html_components as html

def search_result():
    cols = [
    'Behandlingsnr', 'Anmälningstidpunkt', 'SistaOpTidpunkt', 'Opkategori_text',
    'Prioritet_dagar', 'ASAklass', 'KravOperationstidMinuter', 'KravFörberedelsetidMinuter',
     'KravtidEfterMinuter', 'De_PlaneradOpsal_FK', 'PlaneradStartOpsalTidpunkt',
      'PatientÅlderVidOp', 'Veckodag', 'Starttimme', 'TotaltidStart'
      ]
    widget = html.Div(
    style = {
        'height' : 500,
    },
    children = [
        dash_table.Datatable(
        id = 'search_result',
        columns = [{'name' : col , 'id' : col} for col in cols],
        data = None
        )],
    )
    return widget
