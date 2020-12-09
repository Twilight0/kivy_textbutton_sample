# -*- coding: utf-8 -*-

import os

from kivy.core.window import Window
from kaki.app import App
from kivymd.app import MDApp
from manager_screens import ManagerScreens


class AliveGR(MDApp, App):

    KV_FILES = {
        os.path.join(os.getcwd(), "manager_screens.kv"),
        os.path.join(os.getcwd(), "login_screen.kv")
    }

    CLASSES = {
        "<ManagerScreens>": "manager_screens",
        "<LoginScreen>": "login_screen"
    }

    AUTORELOADER_PATHS = [(os.getcwd(), {"recursive": True})]

    def __init__(self):
        self.title = "KivyMD Button hot test with kaki"
        super().__init__()

    def build_app(self, **kwargs):

        Window.bind(on_keyboard=self._rebuild)
        self.manager_screens = ManagerScreens()
        return self.manager_screens

    def _rebuild(self, *args):
        if args[1] == 32:
            self.rebuild()


AliveGR().run()
