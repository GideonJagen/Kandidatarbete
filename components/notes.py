import dash_bootstrap_components as dbc


class Notes:
    current_notes = None

    @staticmethod
    def get_component():
        widget = dbc.Col(
            className="col-3 ml-3 mr-3",
            children=[
                dbc.Row(
                    justify="end",
                    children=[
                        dbc.Button(
                            color="link",
                            children="Återställ",
                            style={"height": "2.5em"},
                        )
                    ],
                ),
                dbc.Row(
                    dbc.Textarea(
                        placeholder="Anteckningar...",
                        bs_size="md",
                    )
                ),
            ],
        )
        return widget

    @staticmethod
    def add_callback():
        pass
