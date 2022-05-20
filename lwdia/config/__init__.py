
import os, sys, toml
from lwdia.dirs import *

app_config_path = os.path.join(user_config_dir_path,"app_config.toml")

app_config = toml.load(app_config_path)

def set_config(key,value):
    app_config[key] = value

def get_config(key):
    return app_config[key]