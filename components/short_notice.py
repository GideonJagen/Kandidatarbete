import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


class ShortNotice:
    @staticmethod
    def get_component():
        widget = dbc.FormGroup(
            children=[
                dbc.Label(
                    html.Span(
                        [
                            "Kort varsel ",
                            html.I(
                                className="fas fa-info-circle", id="short_notice_info"
                            ),
                        ]
                    ),
                    className="label col-form-label-lg font-weight-bold mb-n4 pd-n4",
                ),
                ShortNotice._short_notice_tooltip(),
                html.Hr(style={"margin-top": 0, "margin-bottom": 10}),
                dbc.RadioItems(
                    id="short_notice_items",
                    options=[
                        {"label": "Inkludera alla", "value": "all"},
                        {
                            "label": "Visa endast kort varsel",
                            "value": "interval",
                            "disabled": True,
                        },
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
    def _short_notice_tooltip():
        tooltip = dbc.Tooltip(
            "För att visa patienter noterade med ”Angelägen” eller "
            "liknande ord i ”Information till planerare/koordinator”, "
            "välj ”Inkludera alla” och sök sedan på ordet i kategorin ”Nyckelord”",
            target="short_notice_info",
            placement="auto",
            style={"text-transform": "none"},
        )
        return tooltip

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

    @staticmethod
    def add_str_callback(app):
        @app.callback(
            Output(component_id="active_short_notice", component_property="children"),
            Input(component_id="short_notice_min", component_property="value"),
            Input(component_id="short_notice_max", component_property="value"),
        )
        def update_str(value_min, value_max):
            return ShortNotice.value_to_string(value_min, value_max)

        return app

    @staticmethod
    def value_to_string(value_min, value_max):
        return f"Kort varsel: {value_min if value_min else 'Min'} - {value_max if value_max else 'Max' } dagar"
