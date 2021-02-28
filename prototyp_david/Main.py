from Widgets import *
from DataHandler import *



#TODO Funktion som filtrerar ut vad vill. filter(col att filtrera, värden vill ha)
#TODO Kunna se detaljerad information om utvalda operationer
#TODO Välj hur många värden som ska visas


DATA_PATH = "data/skas_data.csv"

app = dash.Dash(external_stylesheets=[dbc.themes.GRID])


app.layout = html.Div(
id='main',
children = [
html.H1(id='h1',children='Plando-prototype'),

upload_widget(),
selectDate_widget(),
html.H3(id = "loaded-file", children = " "),

html.Div(
id = 'tables',
children = tables_widget(),
)

],
style={
'backgroundColor': 'rgb(255, 255, 227)'}
)


@app.callback(
    Output("booked-operations" , "data"),
    [
    Input("upload-file" , "filename"),
    Input("date-picker" , "value")
    ]
)
def upload_data(filename, date):

    trigger = dash.callback_context.triggered[0].get('prop_id')
    if(trigger == "upload-file.filename"):
        if(filename != None):
            return CURRENT_FILE.to_dict("records")

    elif(trigger == "date-picker.value"):
        if(len(date) == 10):
            return filter_data(CURRENT_FILE, "Operationsdatum", date)
        elif(len(date) == 0):
            return CURRENT_FILE.to_dict("records")




@app.callback(
    Output("similar-patients", "data"),
    Input("booked-operations", "selected_rows"),
    Input("booked-operations", 'page_current'),
    Input("booked-operations", 'active_cell')
)
def show_similar(selected_rows, page_current, active_cell):
    trigger = dash.callback_context.triggered[0].get('prop_id')
    print(active_cell)
    if(active_cell != None):
        true_row = active_cell.get('row')+(page_current*250) #250 = PAGE_SIZE
        print(true_row)
        if(true_row != None):
            return find_similar(true_row).to_dict("records")




if __name__ == '__main__':
    app.run_server(debug=True)
