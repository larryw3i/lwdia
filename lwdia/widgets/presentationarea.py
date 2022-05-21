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


class PresentationArea(AreaBase):
    def __init__(self, win, width=None):
        super().__init__(win, width)
        self.x0 = 2 * self._width
        self.x1 = 3 * self._width
        self.config_x1pct_str = "widgets.presentationarea.x1"

    def get_x0(self):
        return self.win.combinationarea.get_x1()

    def get_x1(self):
        return super().get_x1(wof3_times=3)

    def place(self):
        super().place()
