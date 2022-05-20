import os
import sys

import toml
from benedict import benedict

from lwdia.dirs import *

app_config_path = os.path.join(user_config_dir_path, "app_config.toml")
if not os.path.exists(app_config_path):
    with open(app_config_path, "w") as f:
        f.write("")

app_config = toml.load(app_config_path)
app_config = benedict.from_toml(app_config)


def set_config(keys, value, save_now=True):  # key.key
    app_config[keys] = value
    _app_config = app_config.to_toml()
    if save_now:
        with open(app_config_path, "w") as f:
            f.write(_app_config)


def get_config(key):
    if not key in app_config.keypaths():
        return None
    return app_config[key]
