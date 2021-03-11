import dash_core_components as dcc
import dash_html_components as html


def statistics_code_widget():
    widget = html.Div(
        id='statistics_code_widget',
        children=[
            html.H4('Statistikkod'),
            statistics_code_dropdown()
        ]
    )
    return widget


def statistics_code_dropdown():
    codes = [
        {'label': '30 dagar', 'value': '30d'},
        {'label': '90 dagar', 'value': '90d'},
        {'label': '6 månader', 'value': '6m'},
        {'label': '9 månader', 'value': '9m'},
        {'label': '1 år', 'value': '1å'},
        {'label': '>1 år', 'value': '>1å'}
    ]
    dropdown = dcc.Dropdown(
        id='statistics_dropdown',
        options=codes,
        placeholder="Välj statistikkoder",
        value=[],
        multi=True
    )
    return dropdown