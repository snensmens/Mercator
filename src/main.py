# main.py
#
# Copyright 2024 Clemens Weglau
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the CC BY-NC 4.0
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# License: CC BY-NC 4.0

import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Adw
from gi.repository import Gio

from .ui.window.window import MercatorApplicationWindow


class MercatorApplication(Adw.Application):
    """The main application singleton class."""

    def __init__(self):
        super().__init__(application_id='com.github.snensmens.Mercator',
                         flags=Gio.ApplicationFlags.DEFAULT_FLAGS)
        self.create_action('quit', lambda *_: self.quit(), shortcuts=['<primary>q'])
        self.create_action('about', self.on_about_action)

    def do_activate(self):
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """
        win = self.props.active_window
        if not win:
            win = MercatorApplicationWindow(application=self)
        win.present()

    def on_about_action(self, widget, _):
        """Callback for the app.about action."""
        about = Adw.AboutWindow(transient_for=self.props.active_window,
                                application_name='Mercator',
                                application_icon='com.github.snensmens.Mercator',
                                developer_name='Clemens Weglau',
                                version='2025.01',
                                developers=['Clemens Weglau'],
                                copyright='© 2025 Clemens Weglau',)
        about.present()

    def create_action(self, name, callback, param_type=None, shortcuts=None):
        """Add an application action.

        Args:
            name: the name of the action
            callback: the function to be called when the action is
              activated
            param_type: the type of the parameter
            shortcuts: an optional list of accelerators
        """
        action = Gio.SimpleAction.new(name, param_type)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)


def main(version):
    """The application's entry point."""
    app = MercatorApplication()
    return app.run(sys.argv)
