import concurrent.futures
import threading
import csv
import time

import requests

import config

from gi.repository import GLib, Gtk


builder = Gtk.Builder()
builder.add_from_file("ui/MyApplication.glade")


def create_thread_with_loading_window(func):
    def wrapper(*args, **kwargs):
        loading_complete_event = threading.Event()

        def show_loading_window(loading_complete_event):
            loading_window = builder.get_object("loading_window")
            while not loading_complete_event.is_set():
                GLib.idle_add(loading_window.show)
                time.sleep(0.1)
            loading_window.hide_on_delete()

        def decorator_to_add_end_functionallity(func):
            def wrapper(*args, **kwargs):
                text = func(*args, **kwargs)
                accel_label = builder.get_object("accel_label")
                accel_label.set_text(text)
                loading_complete_event.set()

            return wrapper

        thread1 = threading.Thread(
            target=show_loading_window,
            args=(loading_complete_event,),
        )
        thread1.start()

        thread2 = threading.Thread(
            target=decorator_to_add_end_functionallity(func),
            args=args,
            kwargs=kwargs,
        )
        thread2.start()

    return wrapper


class Handler:
    @create_thread_with_loading_window
    def on_click_upload_from_api(self, button) -> str:
        links: list = config.APIConfig.API_URLS

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(requests.get, link) for link in links]
            data = [f.result().json() for f in futures]

        text = str()
        for lst in data:
            for elem in lst:
                text += f"{elem.get('name')} {elem.get('price')} \n"
        return text

    @create_thread_with_loading_window
    def on_click_upload_from_file(self, button) -> str:
        path: str = button.get_uri()[7:]
        with open(file=path, newline="", mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            text = str()
            for row in csv_reader:
                text += f"{row['Title']} {row['Price']} \n"
        return text

    def on_uploaded_file(self, button):
        button.set_sensitive(True)


builder.connect_signals(Handler())
window = builder.get_object("main_window")
window.show_all()

Gtk.main()
