import importlib
import os
import pickle
import subprocess
import threading
import tkinter as tk
import webbrowser
from functools import partial
from itertools import zip_longest
from tkinter import *
from tkinter import ttk

from lwdia.locale import _
from lwdia.widgets.scrollbar import get_default_scrollbar


class AreaBase:
    def __init__(self, win, width=None, set_widgets=True):
        self.win = win
        self.root = self.win.root
        self._width = width or self.win.scr_widthof6
        self._height = self.win.get_height()
        self._scrollbar = None
        self.x0 = 0
        self.x1 = 0

        if set_widgets:
            self.set_widgets()

    def set_widgets(self):
        self.set_scrollbar()

    def set_scrollbar(self, sbar=None):
        if sbar:
            self._scrollbar = sbar
            return
        self._scrollbar = get_default_scrollbar(self.root)

    def get_scrollbar_width(self):
        return self._scrollbar.winfo_width()

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_x0(self):
        return self.x0

    def get_x1(self):
        return self.x1

    def place(self):
        self._scrollbar.place(
            x=self.get_x1() - self.get_scrollbar_width(),
            y=0,
            relheight=1,
        )

    def config(self):
        self.place()
