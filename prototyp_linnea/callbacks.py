from dash.dependencies import Input, Output, State
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from DataHandler import filter_data, CURRENT_FILE, find_similar



def add_callbacks(app):
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
    return app
