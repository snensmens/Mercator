import random

from gi.repository import GObject
from gi.repository import GLib

from .lookup_table import lookup
from .quiz import Quiz


class Game(GObject.Object):
    __gtype_name__ = 'Game'

    paused = GObject.Property(type=bool, default=True)
    duration = GObject.Property(type=int, default=0)

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

    def get_question(self) -> str | None:
        if len(self.questions) == 0:
            return None

        self.current_question = random.choice(list(self.questions.keys()))
        return self.current_question


    def check_answer(self, answer: str) -> tuple[bool, bool]:
        is_correct = answer.strip() == lookup[self.current_question]["name"]

        if not is_correct:
            print("We are looking for", lookup[self.current_question]["name"])
            self.questions[self.current_question] -= 1

            if self.questions[self.current_question] == 0:
                self.questions.pop(self.current_question)
                return False, False

            return False, True

        self.questions.pop(self.current_question)
        return True, True

    def __clock(self):
        if not self.paused:
            self.duration = self.duration + 1

        return True
