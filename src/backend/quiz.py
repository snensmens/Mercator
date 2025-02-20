from enum import Enum

from gi.repository import GObject

from .lookup_table import lookup, name


class QuizStyle(Enum):
    TYPE_IN = 0
    POINT_AT = 1
    EXPLORE = 2


class QuizType(Enum):
    REGIONS = 0
    CAPITALS = 1


class Quiz(GObject.Object):
    __gtype_name__ = 'Quiz'

    def __init__(self, quiz_map, quiz_type: QuizType, questions: list[str], quiz_style: QuizStyle, is_learning_mode, adjustment):
        super().__init__()

        self.quiz_map = quiz_map
        self.quiz_type = quiz_type
        self.questions = questions
        self.quiz_style = quiz_style
        self.is_learning_mode = is_learning_mode
        self.adjustment = adjustment

    def lookup(self, question: str) -> str:
        match self.quiz_type:
            case QuizType.REGIONS:
                return name(question)
            case QuizType.CAPITALS:
                return lookup[question]["capital"]

    def check_answer(self, question, answer) -> bool:
        pass