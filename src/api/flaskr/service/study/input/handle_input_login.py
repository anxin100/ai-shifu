from trace import Trace
from flask import Flask
from flaskr.service.study.input_funcs import BreakException
from flaskr.service.user.models import User
from flaskr.service.lesson.models import AILessonScript
from flaskr.service.order.models import AICourseLessonAttend
from flaskr.service.study.const import INPUT_TYPE_LOGIN
from flaskr.service.study.plugin import register_input_handler
from flaskr.service.study.utils import make_script_dto


@register_input_handler(input_type=INPUT_TYPE_LOGIN)
def handle_input_login(
    app: Flask,
    user_id: str,
    attend: AICourseLessonAttend,
    script_info: AILessonScript,
    input: str,
    trace: Trace,
    trace_args,
):
    user_info = User.query.filter(User.user_id == user_id).first()
    if user_info.user_state != 0:
        yield make_script_dto(
            "text",
            "",
            script_info.script_id,
        )
    else:
        raise BreakException