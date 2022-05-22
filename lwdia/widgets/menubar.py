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


class MenuBar:
    def __init__(self, win):
        self.win = win
        self.root = self.win.root

        self.menu = tk.Menu(self.root)
        self.helpmenu = Menu(self.menu, tearoff=0)
        self.helpmenu.add_separator()
        self.helpmenu.add_command(label=_("about"), command=self.about_command)

        self.menu.add_cascade(label=_("Help"), menu=self.helpmenu)

    def about_command(self):
        print(_("about"))
