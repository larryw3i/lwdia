import getopt
import os
import re
import sys

from lwdia.settings import *

requirements = [
    # ('requirement_name','version','project_url','License','license_url')
    [  # dev
        (
            "nose2",
            "",
            "https://github.com/nose-devs/nose2",
            "BSD License",
            "https://github.com/nose-devs/nose2/blob/main/setup.py#L57",
        ),
        (
            "twine",
            "",
            "https://github.com/pypa/twine/",
            "Apache License 2.0",
            "https://github.com/pypa/twine/blob/main/LICENSE",
        ),
        (
            "black",
            "",
            "https://github.com/psf/black",
            "MIT License",
            "https://github.com/psf/black/blob/main/LICENSE",
        ),
    ]
] + requirements


def get_requirements_dev():
    install_requires = ""
    for r in requirements:
        for _r in r:
            install_requires += " " + _r[0] + _r[1]
    return install_requires


def install_requirements_dev():
    requirements_dev = get_requirements_dev()
    os.system(install_prefix + requirements_dev)


def get_requirements_dev_u():
    install_requires = "-U"
    for r in requirements:
        for _r in r:
            install_requires += " " + _r[0]
    return install_requires


def install_requirements_dev_u():
    requirements_dev_u = get_requirements_dev_u()
    os.system(install_prefix + requirements_dev_u)


argv = sys.argv[1:]

for arg in argv:
    if arg == "req_dev":
        install_requirements_dev()

    if arg == "req_dev_u":
        install_requirements_dev_u()

    if arg == "test":
        break

if len(argv) == 0:

    from lwdia import spend

    sys.argv[0] = re.sub(r"(-script\.pyw|\.exe)?$", "", sys.argv[0])
    sys.exit(spend())
