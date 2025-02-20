from gi.repository import Gtk
from gi.repository import Adw

from ...quizzes import quizzes as Quizzes
from ...backend import lookup_table as lookup

from .quiz_entry import QuizEntry


@Gtk.Template(resource_path='/com/github/snensmens/Mercator/quiz-overview-page.ui')
class QuizOverviewPage(Adw.NavigationPage):
    __gtype_name__ = 'QuizOverviewPage'

    title: Gtk.Label = Gtk.Template.Child()
    quizzes_overview: Adw.PreferencesPage = Gtk.Template.Child("quizzes-overview")
    higher_order_quizzes = Gtk.Template.Child("higher-order-quizzes")

    def __init__(self, continent, **kwargs):
        super().__init__(**kwargs)

        continent_quizzes = Quizzes[continent]['quizzes']
        regions = Quizzes[continent]['regions']

        self.title.set_label(lookup.name(continent))

        self.higher_order_quizzes.set_title(lookup.name(continent))
        for quiz in continent_quizzes:
            self.add_quiz(quiz, self.higher_order_quizzes)

        for region in regions:
            self.quizzes_overview.add(quiz_group := Adw.PreferencesGroup(title=lookup.name(region)))

            for quiz in regions[region]:
                self.add_quiz(quiz, quiz_group)

    def add_quiz(self, quiz, quiz_group: Adw.PreferencesGroup):
        quiz_group.add(QuizEntry(quiz))
        print(quiz['items'])
