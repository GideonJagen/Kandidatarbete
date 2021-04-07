import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from components.age import Age
from components.asa import Asa
from components.op_code import OpCode
from components.op_time import OpTime
from components.municipalities import Municipalities
from components.statistics_code import StatisticsCode
from components.care_type import CareType
from components.short_notice import ShortNotice
from components.anesthesia import Anesthesia
from components.operator import Operator


class ActiveFilters:
    @staticmethod
    def get_component():
        widget = dbc.Table(
            style={"width": "40em"},
            bordered=False,
            id="active_filters",
            children=[html.Tbody(ActiveFilters._build_rows())],
        )
        return widget

    @staticmethod
    def _build_rows():
        row1 = html.Tr([html.Td(id="active_age"), html.Td(id="active_asa")])
        row2 = html.Tr(
            [html.Td(id="active_anesthesia"), html.Td(id="active_care_type")]
        )
        row3 = html.Tr([html.Td(id="active_op_code"), html.Td(id="active_op_time")])
        row4 = html.Tr(
            [html.Td(id="active_municipalities"), html.Td(id="active_statistics_code")]
        )
        row5 = html.Tr(
            [html.Td(id="active_short_notice"), html.Td(id="active_operator")]
        )
        return [row1, row2, row3, row4, row5]

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(component_id="active_age", component_property="children"),
            Output(component_id="active_asa", component_property="children"),
            Output(component_id="active_op_code", component_property="children"),
            Output(component_id="active_op_time", component_property="children"),
            Output(component_id="active_municipalities", component_property="children"),
            Output(
                component_id="active_statistics_code", component_property="children"
            ),
            Output(component_id="active_care_type", component_property="children"),
            Output(component_id="active_short_notice", component_property="children"),
            Output(component_id="active_anesthesia", component_property="children"),
            Output(component_id="active_operator", component_property="children"),
            Input(component_id="age", component_property="value"),
            Input(component_id="asa_checklist", component_property="value"),
            Input(component_id="opCode_dropdown", component_property="value"),
            Input(component_id="opTime_slider", component_property="value"),
            Input(component_id="statistics_dropdown", component_property="value"),
            Input(component_id="municipalities_radioitems", component_property="value"),
            Input(component_id="care_type_radioitems", component_property="value"),
            Input(component_id="short_notice_min", component_property="value"),
            Input(component_id="short_notice_max", component_property="value"),
            Input(component_id="anaesthesia_checklist", component_property="value"),
            Input(component_id="operator_dropdown", component_property="value"),
            prevent_initial_call=True,
        )
        def set_str(
            age,
            asa,
            op_code,
            op_time,
            statistics_code,
            municipalities,
            care_type,
            short_notice_min,
            short_notice_max,
            anesthesia,
            operator,
        ):
            return (
                Age.value_to_string(age),
                Asa.value_to_string(asa),
                OpCode.value_to_string(op_code),
                OpTime.value_to_string(op_time),
                Municipalities.value_to_string(municipalities),
                StatisticsCode.value_to_string(statistics_code),
                CareType.value_to_string(care_type),
                ShortNotice.value_to_string(short_notice_min, short_notice_max),
                Anesthesia.value_to_string(anesthesia),
                Operator.value_to_string(operator),
            )

        return app
