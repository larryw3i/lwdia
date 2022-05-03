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


def get_default_text_menu(root, text_w):
    _menu = tk.Menu(
        root,
        tearoff=False,
    )
    text_w.bind(
        "<Button-3>",
        lambda event: _menu.post(event.x_root, event.y_root),
    )
    _menu.add_command(
        label=_("Cut"), command=lambda: text_w.event_generate("<<Cut>>")
    )
    _menu.add_command(
        label=_("Copy"), command=lambda: text_w.event_generate("<<Copy>>")
    )
    _menu.add_command(
        label=_("Paste"), command=lambda: text_w.event_generate("<<Paste>>")
    )
    return _menu
