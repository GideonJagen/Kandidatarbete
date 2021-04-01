import dash
import dash_html_components as html


class PatientCount:
    @staticmethod
    def patient_counter():
        widget = html.Div(
            children=[
                # add icon or something
                html.H4(id="number patients"),
            ]
        )
        return widget
