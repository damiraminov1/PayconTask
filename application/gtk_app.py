
import config   # required to check gtk version
from gi.repository import GLib, Gio, Gtk

from application.windows import AppWindow


class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            application_id="org.example.myapp",
            **kwargs
        )
        self.window = None

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        if not self.window:
            self.window = AppWindow(application=self, title="Main Window")
            self.window.show_all()

        self.window.present()
