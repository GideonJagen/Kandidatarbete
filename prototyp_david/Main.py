from Widgets import *
from DataHandler import *
import dash_bootstrap_components as dbc

DATA_PATH = "data/skas_data.csv"

app = dash.Dash(external_stylesheets=[dbc.themes.GRID])


app.layout = html.Div(
id='main',
children = [
html.H1(
id='h1',
children='Plando-prototype'),
dbc.Row([
dbc.Col(selectDate_widget(), width=1),
dbc.Col(upload_widget(), width = 2),
]),
html.H3(id = "loaded-file", children = " "),
html.Div(
id = 'booked',
children = dbc.Row(
[dbc.Col(booked_operations_widget()),
dbc.Col(similar_patients_widget())]
)
)
]
)


@app.callback(
    Output("booked-operations" , "data"),
    [
    Input("upload-file" , "filename"),
    Input("date-picker" , "date")
    ]
)
def upload_data(filename, date):

    trigger = dash.callback_context.triggered[0].get('prop_id')
    print(trigger)
    if(trigger == "upload-file.filename"):
        if(filename != None):
            return CURRENT_FILE.to_dict("records")
    elif(trigger == "date-picker.date"):
        if(date != None):
            print(date)
            return filter_data(CURRENT_FILE, "Operationsdatum", date)
        return CURRENT_FILE.to_dict()



@app.callback(
    Output("similar-patients", "data"),
    Input("booked-operations", "active_cell")
)
def show_similar(active_cell):
    if(active_cell != None):
        return find_similar(active_cell).to_dict("records")






if __name__ == '__main__':
    app.run_server(debug=True)
