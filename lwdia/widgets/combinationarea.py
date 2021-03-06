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
from lwdia.widgets.areabase import AreaBase
from lwdia.widgets.common import get_default_text, get_default_text_menu


class CombinationArea(AreaBase):
    def __init__(self, win, width=None):
        super().__init__(win, width)
        self.x0 = self._width
        self.x1 = 2 * self._width
        self.config_x1pct_str = "widgets.combinationarea.x1"

    def get_combination_text_content(self):
        return self.combination_text.get("1.0", "end")

    def combination_text_bind_tab(self, event):
        self.combination_text.insert(
            self.combination_text.index(tk.INSERT), 4 * " "
        )
        return "break"

    def select_all_text(self, event):
        self.combination_text.tag_add("sel", "1.0", "end")
        return "break"

    def combination_text_modified(self, event):
        print(self.combination_text.get("1.0", "end"))

    def get_rem_width(self):
        super_rem_w = super().get_rem_width()
        _w = super_rem_w
        return _w

    def add_widgets(self):
        self.top_btns = [
            ttk.Button(self.root, text=_("Run")),
            ttk.Button(self.root, text=_("Refresh")),
        ]
        self.combination_text = get_default_text(self.root)
        self.combination_text.bind("<Tab>", self.combination_text_bind_tab)
        self.combination_text.bind("<Control-Key-a>", self.select_all_text)
        self.combination_text.bind(
            "<<Modified>>", self.combination_text_modified
        )
        self.combination_text_menu = get_default_text_menu(
            self.root, self.combination_text
        )

    def get_x0(self):
        return self.win.examplearea.get_x1()

    def get_x1(self):
        return super().get_x1(wof3_times=2)

    def place(self):
        super().place()
        self.combination_text.place(
            x=self.get_x0(),
            y=self.top_btns_height,
            width=self.get_rem_width(),
            height=self.get_scrollbar_height(),
        )

        self.combination_text.config(yscrollcommand=self._scrollbar.set)
        self._scrollbar.config(command=self.combination_text.yview)
