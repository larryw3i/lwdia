import importlib
import os
import pickle
import subprocess
import threading
import webbrowser
from functools import partial
from itertools import zip_longest
import importlib
import os
import pickle
import subprocess
import threading
import webbrowser
from functools import partial
from itertools import zip_longest
from lwdia.locale import _
from tkinter import *
from tkinter import ttk
import tkinter as tk
from lwdia.widgets.areabase import AreaBase


class WidgetArea(AreaBase):
    def __init__(self, win, width=None):
        super().__init__(win, width)
        self.x0 = 0
        self.x1 = self._width
    
    def place(self):
        super().place()

        self.separator.place(
            x=self.win.get_w_width(of=3), y=0, relwidth=0.2, relheight=1
        )
