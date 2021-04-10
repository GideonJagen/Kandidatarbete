import dash_bootstrap_components as dbc
import dash_html_components as html


class PatientCount:
    @staticmethod
    def get_component():
        widget = dbc.Col(
            children=[
                # add icon or something
                html.H4(id="number_of_patients"),
                dbc.Collapse(
                    id="load_collapse",
                    # TODO gör typ grön när datan visas, dvs när knappen klickas
                    children=[
                        dbc.Button(
                            id="load_button",
                            children=["Visa data"],
                            className="btn btn-success",
                        )
                    ],
                ),
            ]
        )
        return widget
