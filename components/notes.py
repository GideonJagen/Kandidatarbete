import dash_bootstrap_components as dbc


class Notes:
    current_notes = None

    @staticmethod
    def get_component():
        widget = dbc.Col(
            style={
                "width": "40%",
            },
            className="col m-3",
            children=[
                dbc.Row(
                    justify="end",
                    children=[dbc.Button(color="link", children="Återställ")],
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
