import importlib
import os
import pickle
import subprocess
import threading
import tkinter as tk
import webbrowser
from enum import Enum
from functools import partial
from itertools import zip_longest
from tkinter import *
from tkinter import ttk

from lwdia.locale import _
from lwdia.widgets.areabase import AreaBase


class ExampleType(Enum):
    EVENT = 0
    CONTROL = 1
    ACTION = 2
    LOOK = 3
    SOUND = 4
    LISTEN = 5
    CALCULATION = 6
    DRAW = 7
    VARIABLE = 8
    FUNCTION = 9
    MUSIC = 10
    READ = 11
    TRANSLATION = 12


class ExampleArea(AreaBase):
    def __init__(self, win, width=None):
        super().__init__(win, width)
        self.x0 = None
        self.x1 = None
        self.example_btns = []

    def update_example_text(self, _type):
        pass

    def add_widgets(self):
        self.event_btn = ttk.Button(
            self.root,
            text=_("Event"),
            command=lambda: self.update_example_text(ExampleType.EVENT),
        )
        self.control_btn = ttk.Button(
            self.root,
            text=_("Control"),
            command=lambda: self.update_example_text(ExampleType.CONTROL),
        )
        self.action_btn = ttk.Button(
            self.root,
            text=_("Action"),
            command=lambda: self.update_example_text(ExampleType.ACTION),
        )
        self.look_btn = ttk.Button(
            self.root,
            text=_("Look"),
            command=lambda: self.update_example_text(ExampleType.LOOK),
        )
        self.sound_btn = ttk.Button(
            self.root,
            text=_("Sound"),
            command=lambda: self.update_example_text(ExampleType.SOUND),
        )
        self.listen_btn = ttk.Button(
            self.root,
            text=_("Listen"),
            command=lambda: self.update_example_text(ExampleType.LISTEN),
        )
        self.calc_btn = ttk.Button(
            self.root,
            text=_("Calc"),
            command=lambda: self.update_example_text(ExampleType.CALCULATION),
        )
        self.draw_btn = ttk.Button(
            self.root,
            text=_("Draw"),
            command=lambda: self.update_example_text(ExampleType.DRAW),
        )
        self.var_btn = ttk.Button(
            self.root,
            text=_("Variable"),
            command=lambda: self.update_example_text(ExampleType.VARIABLE),
        )
        self.func_btn = ttk.Button(
            self.root,
            text=_("Func"),
            command=lambda: self.update_example_text(ExampleType.FUNCTION),
        )
        self.music_btn = ttk.Button(
            self.root,
            text=_("Music"),
            command=lambda: self.update_example_text(ExampleType.MUSIC),
        )
        self.read_btn = ttk.Button(
            self.root,
            text=_("Read"),
            command=lambda: self.update_example_text(ExampleType.READ),
        )
        self.trans_btn = ttk.Button(
            self.root,
            text=_("Trans"),
            command=lambda: self.update_example_text(ExampleType.TRANSLATION),
        )

        self.example_btns = [
            self.event_btn,
            self.control_btn,
            self.look_btn,
            self.action_btn,
            self.sound_btn,
            self.listen_btn,
            self.calc_btn,
            self.draw_btn,
            self.var_btn,
            self.func_btn,
            self.music_btn,
            self.read_btn,
            self.trans_btn
        ]

    def get_x0(self):
        return 0

    def get_x1(self):
        return self.win.get_w_width(of=3)

    def place(self):
        super().place()

        btn_x = self.get_x0()
        btn_y = 0
        for btn in self.example_btns:
            btn_width = btn.winfo_width()
            if self.get_width() > (btn_x + btn_width):
                btn.place(x=btn_x, y=btn_y)
            else:
                btn_x = 0
                btn_y += btn.winfo_height()
                btn.place(x=btn_x, y=btn_y)
            btn_x += btn_width
