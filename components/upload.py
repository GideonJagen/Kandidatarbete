import dash_core_components as dcc
import dash_html_components as html


class UploadWidget:
    @staticmethod
    def upload_widget():
        upload = dcc.Upload(
            id="upload", children=[html.Button("Ladda upp patientlista")]
        )
        return upload
