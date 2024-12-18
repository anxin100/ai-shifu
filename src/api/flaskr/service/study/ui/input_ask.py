from flask import Flask

from flaskr.service.order.models import AICourseLessonAttend
from flaskr.service.lesson.models import AILessonScript
from flaskr.service.lesson.const import (
    ASK_MODE_ENABLE,
)
from flaskr.service.study.utils import get_follow_up_info, make_script_dto


def handle_ask_mode(
    app: Flask,
    user_id: str,
    attend: AICourseLessonAttend,
    script_info: AILessonScript,
    input: str,
    trace,
    trace_args,
):
    follow_up_info = get_follow_up_info(app, script_info)
    ask_mode = follow_up_info.ask_mode
    yield make_script_dto(
        "ask_mode",
        {"ask_mode": True if ask_mode == ASK_MODE_ENABLE else False},
        script_info.script_id,
    )
