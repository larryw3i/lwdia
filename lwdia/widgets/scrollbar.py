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
from lwdia.settings import *


def get_default_scrollbar(root):
    return Scrollbar(
        root,
        orient=VERTICAL,
    )
