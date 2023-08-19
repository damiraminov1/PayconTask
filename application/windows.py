import requests

import config   # required to check gtk version
from gi.repository import GLib, Gio, Gtk
import concurrent.futures


class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.set_size_request(800, 600)
        self.set_default_size(800, 600)

        self.set_border_width(100)

        grid = Gtk.Grid()
        grid.set_border_width(20)
        grid.set_column_spacing(50)
        grid.set_row_spacing(100)

        label = Gtk.Label.new("Программа загрузки данных")
        grid.attach(label, 2, 1, 2, 4)

        button = Gtk.Button.new_with_label("Загрузить из API")
        button.connect("clicked", self.on_click_upload_from_api)
        grid.attach(button, 1, 4, 1, 1)

        button = Gtk.Button.new_with_label("Загрузить из файла")
        button.connect("clicked", self.on_click_upload_from_file)
        grid.attach(button, 7, 4, 1, 1)

        self.add(grid)

    def on_click_upload_from_api(self, button):
        links = config.APIConfig.API_URLS

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(requests.get, link) for link in links]
            data = [f.result().json() for f in futures]

        print(data)

    def on_click_upload_from_file(self, button):
        print("Я загружаю из файла")
