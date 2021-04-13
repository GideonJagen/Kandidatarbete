import dash_bootstrap_components as dbc
import dash_html_components as html

from components.age import Age
from components.anesthesia import Anesthesia
from components.asa import Asa
from components.care_type import CareType
from components.file_upload import FileUpload
from components.free_text_search import FreeTextSearch
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
                html.Hr(className="sidebar-Hr"),
                Sidebar._filter_form(),
            ],
            id="sidebar_content",
            className="col-3 pt-2 sidebar-bg-color scrollable",
        )
        return component

    # Requested order of filters:
    # Optime, Operator, Opcode, Age, Asa, Anesth., Stat.Code, ShortNotice, CareType, Municip., FreeText

    @staticmethod
    def _filter_form():
        component = dbc.Form(
            children=[
                OpTime.get_component(),
                Operator.get_component(),
                OpCode.get_component(),
                Age.get_component(),
                Asa.get_component(),
                Anesthesia.get_component(),
                StatisticsCode.get_component(),
                ShortNotice.get_component(),
                CareType.get_component(),
                Municipalities.get_component(),
                FreeTextSearch.get_component(),
            ],
        )
        return component
