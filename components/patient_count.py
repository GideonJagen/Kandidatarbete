import dash_html_components as html


class PatientCount:
    @staticmethod
    def get_component():
        widget = html.Div(
            children=[
                # add icon or something
                html.H4(id="number_of_patients"),
            ]
        )
        return widget
