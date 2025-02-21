import random

from gi.repository import GObject
from gi.repository import GLib

from .lookup_table import lookup, name
from .quiz import Quiz, QuizStyle


class Game(GObject.Object):
    __gtype_name__ = 'Game'

    paused = GObject.Property(type=bool, default=True)
    duration = GObject.Property(type=int, default=0)

    @GObject.Signal(name="new-question", arg_types=(str,))
    def new_question(self, question):
        pass

    @GObject.Signal()
    def finished(self):
        pass

    def __init__(self, quiz: Quiz, **kwargs):
        super().__init__(**kwargs)
        GLib.timeout_add_seconds(1, self.__clock)

        self.quiz = quiz
        self.questions = dict()
        self.current_question = None

    def begin(self):
        self.paused = False

        for question in self.quiz.questions:
            self.questions[question] = 3

        self.__emit_new_question()

    def check_answer(self, answer) -> [bool, bool]:
        GLib.timeout_add(1200, self.__emit_new_question)

        if self.quiz.quiz_style == QuizStyle.TYPE_IN:
            is_correct = answer.strip() == name(self.current_question)
        else:
            is_correct = answer == self.current_question

        if is_correct:
            if self.quiz.is_learning_mode:
                self.questions[self.current_question] -= 1
            else:
                self.questions.pop(self.current_question)
            return True, False

        if self.questions.get(self.current_question):
            print(f"answer was incorrect (got {answer})")
            if not self.quiz.is_learning_mode:
                self.questions[self.current_question] -= 1

            if self.questions[self.current_question] == 0:
                self.questions.pop(self.current_question)

                if self.quiz.is_learning_mode:
                    return False, False

                return False, True

        return False, False

    def __emit_new_question(self):
        if len(self.questions) == 0:
            self.emit("finished")
        else:
            if (self.current_question is None
                    or self.questions.get(self.current_question) is None
                    or self.quiz.is_learning_mode):
                self.current_question = random.choice(list(self.questions.keys()))

            if self.quiz.quiz_style == QuizStyle.TYPE_IN:
                self.emit("new-question", self.current_question)
            else:
                self.emit("new-question", name(self.current_question))

    def __clock(self):
        if not self.paused:
            self.duration = self.duration + 1

        return True
