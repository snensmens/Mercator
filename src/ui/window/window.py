from gi.repository import Adw
from gi.repository import Gtk
from gi.repository import Gio
from gi.repository import GLib

from ...backend.quiz import Quiz, QuizStyle, QuizType

from .setup_quiz_dialog import SetupQuizDialog
from ..quiz_overview_page.quiz_overview_page import QuizOverviewPage
from ..quiz_page.quiz_page import QuizPage


@Gtk.Template(resource_path='/com/github/snensmens/Mercator/window.ui')
class MercatorApplicationWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'MercatorApplicationWindow'

    navigation = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.settings = Gio.Settings(schema_id="com.github.snensmens.Mercator")
        self.settings.bind("width", self, "default-width", Gio.SettingsBindFlags.DEFAULT)
        self.settings.bind("height", self, "default-height", Gio.SettingsBindFlags.DEFAULT)
        self.settings.bind("is-maximized", self, "maximized", Gio.SettingsBindFlags.DEFAULT)

        self.add_action(toggle_fullscreen_action := Gio.SimpleAction(name="toggle-fullscreen"))
        toggle_fullscreen_action.connect("activate", lambda *_: self.toggle_fullscreen())

        self.add_action(unfullscreen_action := Gio.SimpleAction(name="unfullscreen"))
        unfullscreen_action.connect("activate", lambda *_: self.unfullscreen())

        self.add_action(open_quiz_overview_action := Gio.SimpleAction(name="open-quiz-overview", parameter_type=GLib.VariantType.new("s")))
        open_quiz_overview_action.connect("activate", self.on_open_quiz_overview)

        # (map, quiz-type, quiz-items)
        self.add_action(setup_quiz_action := Gio.SimpleAction(name="setup-quiz", parameter_type=GLib.VariantType.new("(sias)")))
        setup_quiz_action.connect("activate", self.setup_quiz)

        # (quiz_map, quiz-type, [quiz-items], quiz-style, is_learning_mode, adjustment)
        self.add_action(open_quiz_action := Gio.SimpleAction(name="open-quiz", parameter_type=GLib.VariantType.new("(siasibi)")))
        open_quiz_action.connect("activate", self.open_quiz)

    def toggle_fullscreen(self):
        self.fullscreen() if not self.is_fullscreen() else self.unfullscreen()

    def on_open_quiz_overview(self, _action, params):
        category = params.unpack()
        self.navigation.push(QuizOverviewPage(category))

    def setup_quiz(self, _action, params):
        quiz_map, quiz_type, quiz_items = params.unpack()
        SetupQuizDialog(quiz_map, quiz_type, quiz_items).present(self)

    def open_quiz(self, _action, params):
        quiz_map, quiz_type, questions, style, learning_mode, adjustment = params.unpack()
        self.navigation.push(QuizPage(self, Quiz(quiz_map, QuizType(quiz_type), questions, QuizStyle(style), learning_mode, adjustment)))