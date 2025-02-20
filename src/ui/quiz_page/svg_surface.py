import xml.etree.ElementTree as ET

from gi.repository import Gtk
from gi.repository import Adw
from gi.repository import GObject
from gi.repository import Gsk
from gi.repository import Gdk
from gi.repository import Graphene


BG_COLOR_DARK = "#1a5fb4"
BG_COLOR_LIGHT = "#99c1f1"

FILL_COLOR_DARK = "#26a269"
FILL_COLOR_LIGHT = "#8ff0a4"

FILL_COLOR_SELECTED_DARK = "#c64600"
FILL_COLOR_SELECTED_LIGHT = "#ffbe6f"

FILL_COLOR_HOVERED_DARK = "#e5a50a"
FILL_COLOR_HOVERED_LIGHT = "#f9f06b"

STROKE_COLOR_DARK = "#deddda"
STROKE_COLOR_LIGHT = "#3d3846"

STROKE_COLOR_DARK_HIGH_CONTRAST = "#ffffff"
STROKE_COLOR_LIGHT_HIGH_CONTRAST = "#000000"


class Region:
    def __init__(self, region_id, path):
        self.id = region_id
        self.path = Gsk.Path.parse(path)
        self.is_selected = False
        self.is_hovered = False


class Bounds:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None

    def get_height(self):
        return self.bottom - self.top

    def get_width(self):
        return self.right - self.left

    def add(self, top, bottom, left, right):
        if self.top is None or top < self.top:
            self.top = top

        if self.bottom is None or bottom > self.bottom:
            self.bottom = bottom

        if self.left is None or  left < self.left:
            self.left = left

        if self.right is None or right > self.right:
            self.right = right


class SvgSurface(Gtk.Widget):
    __gtype_name__ = 'SvgSurface'

    @GObject.Signal(name="region-clicked", arg_types=(str,))
    def region_clicked(self, region_id):
        pass

    @GObject.Signal(name="region-hovered", arg_types=(str,))
    def region_hovered(self, region_id):
        pass

    @GObject.Signal(name="nothing-hovered")
    def nothing_hovered(self):
        pass

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.regions = []
        self.bounds: Bounds = Bounds()
        self._last_hovered_region = None

        self.style_manager = Adw.StyleManager.get_default()
        self.style_manager.connect("notify::dark", self.__on_style_manager_notification)
        self.style_manager.connect("notify::high-contrast", self.__on_style_manager_notification)

        self.click_gesture = Gtk.GestureClick()
        self.click_gesture.connect("pressed", self.__on_click)
        self.add_controller(self.click_gesture)

        self.motion_controller = Gtk.EventControllerMotion()
        self.motion_controller.connect("motion", self.__on_motion)
        self.add_controller(self.motion_controller)

        self.drag_offset_x = 0.0
        self.drag_offset_y = 0.0
        self._last_drag_position_x = 0.0
        self._last_drag_position_y = 0.0

        self.drag_controller = Gtk.GestureDrag()
        self.drag_controller.connect("drag-begin", lambda *_: self.__reset_drag_positions())
        self.drag_controller.connect("drag-end", lambda *_: self.__reset_drag_positions())
        self.drag_controller.connect("drag-update", self.__on_drag_update)
        self.add_controller(self.drag_controller)

        self.scroll_controller = Gtk.EventControllerScroll()
        self.scroll_controller.set_flags(Gtk.EventControllerScrollFlags.VERTICAL)
        self.scroll_controller.connect("scroll", self.__on_scroll)
        self.add_controller(self.scroll_controller)

        self.scale_offset = 0.0

        self.scale = 1.0
        self.offset_width = 0.0
        self.offset_height = 0.0

        self.stroke: Gsk.Stroke = Gsk.Stroke(line_width=2.0)
        self.stroke_color = Gdk.RGBA()
        self.fill_color = Gdk.RGBA()
        self.fill_color_selected = Gdk.RGBA()
        self.fill_color_hovered = Gdk.RGBA()
        self.bg_color = Gdk.RGBA()
        self.__set_colors()

    def __on_scroll(self, _event, _dx, dy):
        self.scale_offset -= dy * 0.08
        self.queue_draw()

        return True

    def __reset_drag_positions(self):
        self._last_drag_position_x = 0.0
        self._last_drag_position_y = 0.0

    def __on_drag_update(self, _event, x, y):
        self.drag_offset_x += x - self._last_drag_position_x
        self.drag_offset_y += y - self._last_drag_position_y

        self._last_drag_position_x = x
        self._last_drag_position_y = y

        self.queue_draw()

        return True

    def set_svg(self, file):
        svg_root = ET.parse(f"/app/share/mercator/mercator/maps/{file}.svg").getroot()
        for child in svg_root.iter("{http://www.w3.org/2000/svg}path"):
            self.regions.append( Region(region_id=child.attrib["id"], path=child.attrib["d"]) )

        self.bounds = Bounds()

        for region in self.regions:
            _, bounds = region.path.get_stroke_bounds(self.stroke)
            self.bounds.add(bounds.get_top_left().y, bounds.get_bottom_right().y, bounds.get_top_left().x, bounds.get_bottom_right().x)

        print(self.bounds.top, self.bounds.left, self.bounds.bottom, self.bounds.right)

        match file:
            case "africa":
                self.stroke.set_line_width(1.2)
            case "south-america":
                self.stroke.set_line_width(1.5)


    def __on_style_manager_notification(self, *args):
        self.__set_colors()
        self.queue_draw()# is this necessary?

    def __set_colors(self, *args):
        is_dark = self.style_manager.get_dark()
        is_high_contrast = self.style_manager.get_high_contrast()

        self.bg_color.parse(BG_COLOR_DARK if is_dark else BG_COLOR_LIGHT)
        self.fill_color.parse(FILL_COLOR_DARK if is_dark else FILL_COLOR_LIGHT)
        self.fill_color_selected.parse(FILL_COLOR_SELECTED_DARK if is_dark else FILL_COLOR_SELECTED_LIGHT)
        self.fill_color_hovered.parse(FILL_COLOR_HOVERED_DARK if is_dark else FILL_COLOR_HOVERED_LIGHT)

        if is_high_contrast:
            self.stroke_color.parse(STROKE_COLOR_DARK_HIGH_CONTRAST if is_dark else STROKE_COLOR_LIGHT_HIGH_CONTRAST)
        else:
            self.stroke_color.parse(STROKE_COLOR_DARK if is_dark else STROKE_COLOR_LIGHT)

    def __on_motion(self, _event_controller, x, y):
        position = Graphene.Point().init((x - self.offset_width) / self.scale, (y - self.offset_height) / self.scale)

        for region in self.regions:
            region.is_hovered = False

        for region in self.regions:
            if region.path.in_fill(position, Gsk.FillRule.WINDING):
                region.is_hovered = True

                if self._last_hovered_region != region.id:
                    self._last_hovered_region = region.id
                    self.emit("region-hovered", region.id)

                    self.queue_draw()

                return

        self._last_hovered_region = None
        self.emit("nothing-hovered")
        self.queue_draw()

    def __on_click(self, _gesture, clicks, x, y):
        if clicks > 1:
            return

        position = Graphene.Point().init((x - self.offset_width) / self.scale, y / self.scale)

        for region in self.regions:
            if region.path.in_fill(position, Gsk.FillRule.WINDING):
                self.emit("region-clicked", region.id)

                self.queue_draw()
                return

    def do_snapshot(self, snapshot):
        snapshot.append_color(self.bg_color, Graphene.Rect().init(0, 0, self.get_width(), self.get_height()))

        self.scale = (self.get_height() / self.bounds.get_height()) + self.scale_offset

        self.offset_width = (-self.bounds.left*self.scale + (self.get_width() - self.bounds.get_width()*self.scale) / 2) + self.drag_offset_x
        self.offset_height = (-self.bounds.top*self.scale + (self.get_height() - self.bounds.get_height()*self.scale) / 2) + self.drag_offset_y

        snapshot.transform(Gsk.Transform()
                          .translate(Graphene.Point().init(self.offset_width, self.offset_height))
                          .scale(self.scale, self.scale))

        for region in self.regions:
            snapshot.append_stroke(region.path, self.stroke, self.stroke_color)

            if region.is_selected:
                snapshot.append_fill(region.path, Gsk.FillRule.WINDING, self.fill_color_selected)

            elif region.is_hovered:
                snapshot.append_fill(region.path, Gsk.FillRule.WINDING, self.fill_color_hovered)

            else:
                snapshot.append_fill(region.path, Gsk.FillRule.WINDING, self.fill_color)

    def set_region_selected(self, region_id, selected):
        for region in self.regions:
            if region.id == region_id:
                region.is_selected = selected

                self.queue_draw()
                return

    def unselect_all(self):
        for region in self.regions:
            region.is_selected = False

        self.queue_draw()