@app.callback(
   Output(component_id='eighty', component_property='style'),
   [Input(component_id='age_radio', component_property='value')])

def show_hide_element(visibility_state):
    if visibility_state == 'on':
        return {'display': 'block'}
    if visibility_state == 'off':
        return {'display': 'none'}
