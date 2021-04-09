import dash_bootstrap_components as dbc


class ResetFilterButton:
    @staticmethod
    def get_component():
        button = dbc.Button(
            "Återställ",
            id="reset_filter_button",
            color="danger",
            style={"margin-left": "50em", "height": "40px"},
        )
        return button
