import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


class ShortNotice:
    @staticmethod
    def get_component():
        widget = dbc.FormGroup(
            children=[
                dbc.Label("Kort varsel"),
                dbc.RadioItems(
                    id="short_notice_items",
                    options=[
                        {"label": "Inkludera alla", "value": "all"},
                        {"label": "Visa endast kort varsel", "value": "interval"},
                    ],
                    value="all",
                ),
                dbc.Collapse(
                    id="collapse",
                    # TODO REMOVE WHEN IMPLEMENTING CSS
                    style={"width": "300px"},
                    children=[
                        dbc.InputGroup(
                            [
                                dbc.Input(
                                    id="short_notice_min",
                                    placeholder="Min dagar",
                                    invalid=True,
                                ),
                                dbc.Input(
                                    id="short_notice_max",
                                    placeholder="Max dagar",
                                    invalid=True,
                                    style={},
                                ),
                            ]
                        )
                    ],
                ),
            ]
        )
        return widget

    @staticmethod
    def add_collapse_callback(app):
        @app.callback(
            Output(component_id="collapse", component_property="is_open"),
            Output(component_id="short_notice_min", component_property="value"),
            Output(component_id="short_notice_max", component_property="value"),
            Output(component_id="short_notice_items", component_property="value"),
            Input(component_id="short_notice_items", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def collapse(value, reset):
            context = dash.callback_context
            if context.triggered[0]["prop_id"].split(".")[0] == "reset_filter_button":
                return False, None, None, "all"
            elif value == "interval":
                return True, None, None, "interval"
            return (
                False,
                None,
                None,
                "all",
            )  # Just to be sure one item is always selected, looks better

        return app

    @staticmethod
    def add_input_callback(app):
        @app.callback(
            Output(component_id="short_notice_min", component_property="valid"),
            Output(component_id="short_notice_min", component_property="invalid"),
            Output(component_id="short_notice_max", component_property="valid"),
            Output(component_id="short_notice_max", component_property="invalid"),
            Input(component_id="short_notice_min", component_property="value"),
            Input(component_id="short_notice_max", component_property="value"),
        )
        def is_valid_input(min_val, max_val):
            """
            This is not a joke, valid and invalid are actually two different properties....... lol
            But other than looking good, we can use the bool of valid input in filtering.
            Let user put in max in wrong box? and just give filter by taking max and min of both?
            """
            min_valid = False
            min_invalid = True
            max_valid = False
            max_invalid = True
            if isinstance(min_val, str):
                min_valid = min_val.isnumeric()
                min_invalid = not min_valid
            if isinstance(max_val, str):
                max_valid = max_val.isnumeric()
                max_invalid = not max_valid
            return min_valid, min_invalid, max_valid, max_invalid

        return app
