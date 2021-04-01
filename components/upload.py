import dash_core_components as dcc
import dash_html_components as html


class FileUpload:
    UPLOAD_PATIENTS = "Ladda upp patientlista"

    @staticmethod
    def upload_widget():
        upload = dcc.Upload(html.Button(FileUpload.UPLOAD_PATIENTS))
        return upload
