from gi.repository import Adw
from gi.repository import Gtk
from gi.repository import GLib
from gi.repository import GObject

from ...backend.quiz import Quiz, QuizStyle
from ...backend.game import Game
from ...backend.utils import seconds_to_str

from .svg_surface import SvgSurface


@Gtk.Template(resource_path='/com/github/snensmens/Mercator/quiz-page.ui')
class QuizPage(Adw.NavigationPage):
    __gtype_name__ = 'QuizPage'

    toggle_fullscreen_button = Gtk.Template.Child()

    svg_surface: SvgSurface = Gtk.Template.Child()

    answer_field: Gtk.Entry = Gtk.Template.Child()
    bottom_bar_label: Gtk.Label = Gtk.Template.Child()
    skip_button: Gtk.Button = Gtk.Template.Child()

    pause_button: Gtk.ToggleButton = Gtk.Template.Child()
    pause_button_content: Adw.ButtonContent = Gtk.Template.Child()

    def __init__(self, window, quiz: Quiz, **kwargs):
        super().__init__(**kwargs)

        self.quiz = quiz
        self.game = Game(self.quiz)
        self.game.bind_property("duration", self.pause_button_content, "label",
                                GObject.BindingFlags.DEFAULT,
                                lambda _, sec: seconds_to_str(sec))

        self.game.bind_property("paused", self.pause_button, "active",
                                GObject.BindingFlags.BIDIRECTIONAL)

        self.pause_button.bind_property("active", self.pause_button_content, "icon-name",
                                        GObject.BindingFlags.DEFAULT,
                                        lambda _, active: "cafe-symbolic" if active else "clock-alt-symbolic")

        window.bind_property("fullscreened", self.toggle_fullscreen_button, "icon-name",
                             GObject.BindingFlags.SYNC_CREATE,
                             self.on_fullscreened_notification)

        self.answer_field.set_visible(quiz.quiz_style == QuizStyle.TYPE_IN)
        self.skip_button.set_visible(quiz.quiz_style != QuizStyle.EXPLORE)
        self.pause_button.set_sensitive(quiz.quiz_style != QuizStyle.EXPLORE)

        self.svg_surface.set_svg(self.quiz.quiz_map)

    @Gtk.Template.Callback()
    def on_shown(self, _page):
        if self.quiz.quiz_style != QuizStyle.EXPLORE:
            self.start_new_game()

    @Gtk.Template.Callback()
    def on_hiding(self, _page):
        self.activate_action("win.unfullscreen")

    @Gtk.Template.Callback()
    def on_region_clicked(self, _svg_surface, region_id):
        pass

    @Gtk.Template.Callback()
    def on_region_hovered(self, _svg_surface, region_id):
        match self.quiz.quiz_style:
            case QuizStyle.EXPLORE:
                self.bottom_bar_label.set_text(self.quiz.lookup(region_id))

    @Gtk.Template.Callback()
    def on_nothing_hovered(self, _svg_surface):
        self.bottom_bar_label.set_text("")

    @Gtk.Template.Callback()
    def on_answer_field_activated(self, answer_field: Gtk.Entry):
        is_correct, has_retries_left = self.game.check_answer(answer_field.get_text())

        if is_correct:
            self.answer_field.add_css_class("success")
            self.answer_field.set_icon_from_icon_name(Gtk.EntryIconPosition.SECONDARY, "check-plain-symbolic")
        else:
            self.answer_field.add_css_class("error")

        GLib.timeout_add(1200, self.reset_answer_field)

        if is_correct or not has_retries_left:
            GLib.timeout_add(1200, self.next_question)

    def on_fullscreened_notification(self, _binding, is_fullscreen):
        return "view-restore-symbolic" if is_fullscreen else "view-fullscreen-symbolic"

    def start_new_game(self):
        self.game.begin()
        self.next_question()

    def next_question(self):
        self.svg_surface.unselect_all()
        self.svg_surface.set_region_selected(self.game.get_question(), True)
        #self.answer_field.grab_focus()

    def reset_answer_field(self):
        self.answer_field.remove_css_class("success")
        self.answer_field.remove_css_class("error")

        self.answer_field.set_icon_from_icon_name(Gtk.EntryIconPosition.SECONDARY, None)
        self.answer_field.set_text("")