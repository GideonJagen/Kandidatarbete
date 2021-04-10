import dash_bootstrap_components as dbc
import dash_html_components as html

from components.age import Age
from components.anesthesia import Anesthesia
from components.asa import Asa
from components.care_type import CareType
from components.file_upload import FileUpload
from components.municipalities import Municipalities
from components.op_code import OpCode
from components.op_time import OpTime
from components.operator import Operator
from components.short_notice import ShortNotice
from components.statistics_code import StatisticsCode


class Sidebar:
    SEARCH_FILTER = "Sökfilter"
    OPEN_FILTER = "Öppna filter"
    REQUEST_FILL_FORM = "Var god fyll i relevanta sökfält"

    @staticmethod
    def get_component():
        component = dbc.Col(
            children=[
                html.H2(Sidebar.SEARCH_FILTER),
                FileUpload.get_component(),
                html.P(Sidebar.REQUEST_FILL_FORM),
                html.Hr(style={"border-width": 4, "border-color": "#6ea6cd"}),
                Sidebar._filter_form(),
            ],
            id="sidebar_content",
            className="col-3",
            style={
                "height": "inherit",
                "overflow": "auto",
            },
        )
        return component

    @staticmethod
    def _filter_form():
        component = dbc.Form(
            children=[
                CareType.get_component(),
                Municipalities.get_component(),
                Anesthesia.get_component(),
                Age.get_component(),
                StatisticsCode.get_component(),
                Asa.get_component(),
                OpTime.get_component(),
                OpCode.get_component(),
                Operator.get_component(),
                ShortNotice.get_component(),
            ],
        )
        return component
