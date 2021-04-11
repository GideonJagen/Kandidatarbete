import dash_bootstrap_components as dbc


class ResetFilterButton:
    @staticmethod
    def get_component():
        button = dbc.Button(
            "Återställ",
            id="reset_filter_button",
            color="link",
            style={"height": "2.5em"},
        )
        return button
