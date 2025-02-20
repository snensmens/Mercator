from gi.repository import Adw
from gi.repository import Gtk
from gi.repository import GLib


@Gtk.Template(resource_path='/com/github/snensmens/Mercator/quiz-entry.ui')
class QuizEntry(Adw.ActionRow):
    __gtype_name__ = 'QuizEntry'

    def __init__(self, quiz, **kwargs):
        super().__init__(**kwargs)
        self.quiz = quiz

        self.set_title(quiz['quiz-name'])

    @Gtk.Template.Callback()
    def on_activated(self, _row):
        builder = GLib.VariantBuilder.new(GLib.VariantType.new("(sias)"))
        builder.add_value(GLib.Variant.new_string(self.quiz["map"]))
        builder.add_value(GLib.Variant.new_int32(self.quiz["quiz-type"].value))
        builder.add_value(GLib.Variant.new_strv(self.quiz["items"]))

        self.activate_action("win.setup-quiz", builder.end())

