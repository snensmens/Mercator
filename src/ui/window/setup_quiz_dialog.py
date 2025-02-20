from gi.repository import Adw
from gi.repository import Gtk
from gi.repository import GLib
from gi.repository import GObject

from ...backend.lookup_table import lookup
from ...backend.quiz import QuizType


@Gtk.Template(resource_path='/com/github/snensmens/Mercator/setup-quiz-dialog.ui')
class SetupQuizDialog(Adw.AlertDialog):
    __gtype_name__ = 'SetupQuizDialog'

    play_style_row: Adw.ExpanderRow = Gtk.Template.Child()
    play_style_toggle = Gtk.Template.Child()

    learning_mode_row = Gtk.Template.Child()
    adjustment_row = Gtk.Template.Child()

    def __init__(self, quiz_map:str, quiz_type: int, quiz_items: list[str], **kwargs):
        super().__init__(**kwargs)
        self.quiz_map = quiz_map
        self.quiz_type = quiz_type
        self.quiz_items = quiz_items

        self.play_style_toggle.bind_property("active-name", self.play_style_row, "title",
                                             GObject.BindingFlags.SYNC_CREATE,
                                             lambda _, name: self.__set_play_style_title_from_active_name(name))

        self.play_style_toggle.bind_property("active-name", self.play_style_row, "subtitle",
                                             GObject.BindingFlags.SYNC_CREATE,
                                             lambda _, name: self.__set_play_style_subtitle_from_active_name(name))

        self.play_style_toggle.bind_property("active-name", self.learning_mode_row, "visible",
                                             GObject.BindingFlags.SYNC_CREATE,
                                             lambda _, name: name != "explore")

        self.play_style_toggle.bind_property("active-name", self.adjustment_row, "visible",
                                             GObject.BindingFlags.SYNC_CREATE,
                                             lambda _, name: name != "explore")

        self.learning_mode_row.bind_property("active", self.adjustment_row, "title",
                                             GObject.BindingFlags.SYNC_CREATE,
                                             lambda _, active: "Allowed guesses" if not active else "Required correct answers")

        self.connect("response", self.__on_response)

    def __set_play_style_title_from_active_name(self, active_name):
        match active_name:
            case "type-in":
                return "Quiz style: Type in"
            case "point-at":
                return "Quiz style: Point at"
            case "explore":
                return "Quiz style: Explore"

    def __set_play_style_subtitle_from_active_name(self, active_name):
        match active_name:
            case "type-in":
                return "Type in the answer"
            case "point-at":
                return "Show the answer on the map"
            case "explore":
                return "Just explore the map"

    def __on_response(self, _dialog, response):
        print(response)
        if response == "start":
            builder = GLib.VariantBuilder.new(GLib.VariantType.new("(siasibi)"))
            builder.add_value(GLib.Variant.new_string(self.quiz_map))
            builder.add_value(GLib.Variant.new_int32(self.quiz_type))
            builder.add_value(GLib.Variant.new_strv(self.quiz_items))
            builder.add_value(GLib.Variant.new_int32(self.play_style_toggle.get_active()))
            builder.add_value(GLib.Variant.new_boolean(self.learning_mode_row.get_active()))
            builder.add_value(GLib.Variant.new_int32(int(self.adjustment_row.get_value())))

            self.activate_action("win.open-quiz", builder.end())