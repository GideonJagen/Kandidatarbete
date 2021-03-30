import dash
import dash_html_components as html


class NumberPatients:
    @staticmethod
    def number_patients():

        widget = html.Div(
            children=[
                # add icon or something
                html.H4(id="number patients"),
            ]
        )
        return widget
