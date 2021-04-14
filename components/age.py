import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from data_handling import LoadedData
import dash


class Age:
    MIN_AGE = 0
    MAX_AGE = 150  # Not the actual value, this has to be fixed, magic number

    @staticmethod
    def get_component():
        widget = dbc.FormGroup(
            [
                dbc.Label(
                    "Ålder",
                    className="label col-form-label-lg font-weight-bold mb-n4 pd-n4",
                ),
                html.Hr(style={"margin-top": 0, "margin-bottom": 10}),
                dcc.RangeSlider(
                    id="age",
                    min=Age.MIN_AGE,
                    max=Age.MAX_AGE,
                    step=None,
                    marks={
                        Age.MIN_AGE: "0",
                        16: "16",
                        80: "80",
                        Age.MAX_AGE: "max",
                    },
                    value=[Age.MIN_AGE, Age.MAX_AGE],
                ),
            ]
        )
        return widget

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(component_id="age", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
            Input(component_id="upload", component_property="filename"),
            Input(component_id="upload", component_property="contents"),
        )
        def reset_component(n_clicks, filename, contents):
            context = dash.callback_context
            if context.triggered[0]["prop_id"].split(".")[0] == "upload":
                LoadedData.load_data(filename, contents)
            return [Age.MIN_AGE, Age.MAX_AGE]

        return app

    @staticmethod
    def add_str_callback(app):
        @app.callback(
            Output(component_id="active_age", component_property="children"),
            Input(component_id="age", component_property="value"),
        )
        def update_str(value):
            return Age.value_to_string(value)

        return app

    @staticmethod
    def value_to_string(value):
        return f"Ålder: {value[0]} - {value[1]} år"
