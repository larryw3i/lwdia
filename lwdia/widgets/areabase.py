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

from lwdia.config import *
from lwdia.locale import _
from lwdia.widgets.scrollbar import get_default_scrollbar


class AreaBase:
    def __init__(
        self,
        win,
        width=None,
        set_widgets=True,
        show_scrollbar=True,
        show_separator=True,
        scrollbar_width=12,
        separator_width=2,
    ):
        self.win = win
        self.root = self.win.root
        self._width = width or self.win.scr_widthof6
        self._height = self.win.get_height()
        self._scrollbar = None
        self.x0 = 0
        self.x1 = 0
        self.config_x1_str = "areabase.x1"
        self.top_btns = []
        self.top_btns_height = 0
        self.show_scrollbar = show_scrollbar
        self.show_separator = show_separator
        self.separator_width = self.show_separator and separator_width or 0
        self.scrollbar_width = self.show_scrollbar and scrollbar_width or 0

        if set_widgets:
            self.set_widgets()
        if self.show_separator:
            self.set_separator()

    def set_separator(self):
        self.separator = ttk.Separator(
            self.root, orient="vertical", cursor="sizing"
        )
        self.separator.bind("<ButtonRelease-1>", self.separator_key1_release)
        self.separator.bind("<Button-3>", self.separator_key2_release)

    def separator_key1_release(self, event):
        self.set_x1()
        self.win.place()

    def separator_key2_release(self, event):
        self.set_x1(reset=True)
        self.win.place()

    def place_btns_top_default(self):
        btn_x = self.get_x0()
        btn_y = 0
        all_btns_height = 0
        oneline = True
        for btn in self.top_btns:
            btn_width = btn.winfo_width()
            btn_height = btn.winfo_height()
            if (self.get_x1() - self.get_scrollbar_width()) > (
                btn_x + btn_width
            ):
                btn.place(x=btn_x, y=btn_y)
            else:
                oneline = False
                btn_x = self.get_x0()
                btn_y += btn_height
                btn.place(x=btn_x, y=btn_y)
                all_btns_height = btn_y + btn_height
            btn_x += btn_width
        if oneline:
            first_btn = self.top_btns[0]
            all_btns_height = first_btn.winfo_height()
        self.top_btns_height = all_btns_height

    def set_x1(self, event=None, reset=False):
        if reset:
            set_config(self.config_x1_str, None)
            return
        set_config(
            self.config_x1_str,
            self.root.winfo_pointerx() - self.root.winfo_rootx(),
        )

    def set_widgets(self):
        self.set_scrollbar()

    def set_scrollbar(self, sbar=None):
        if sbar:
            self._scrollbar = sbar
            return
        self._scrollbar = get_default_scrollbar(self.root)

    def get_scrollbar_width(self):
        return self.scrollbar_width

    def get_width(self):
        return self.get_x1() - self.get_x0()

    def get_rem_width(self):
        return (
            self.get_width()
            - self.separator_width
            - self.get_scrollbar_width()
        )

    def get_height(self):
        return self.win.get_w_height()

    def get_x0(self):
        return self.x0

    def get_x1(self, wof3_times=1):
        x1_value = get_config(self.config_x1_str)
        return x1_value or wof3_times * self.win.get_w_width(of=3)

    def add_widgets(self):
        pass

    def get_scrollbar_x(self):
        return (
            self.get_x1() - self.separator_width - self.get_scrollbar_width()
        )

    def get_scrollbar_y(self):
        return self.top_btns_height

    def get_scrollbar_height(self):
        return self.get_height() - self.top_btns_height

    def get_separator_x(self):
        return self.get_x1() - self.separator_width

    def place(self, show_scrollbar=True, show_separator=True):
        if len(self.top_btns) > 0:
            self.place_btns_top_default()
        if show_separator:
            self.separator.place(
                x=self.get_separator_x(),
                y=0,
                height=self.get_height(),
                width=self.separator_width,
            )
        if show_scrollbar:
            self._scrollbar.place(
                x=self.get_scrollbar_x(),
                y=self.get_scrollbar_y(),
                height=self.get_scrollbar_height(),
                width=self.scrollbar_width,
            )

    def config(self):
        self.place()
