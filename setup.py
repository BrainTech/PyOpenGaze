# Copyright (c) 2016-2018 Braintech Sp. z o.o. [Ltd.] <http://www.braintech.pl>
# All rights reserved.
from setuptools import setup

setup(
    name='pyopengaze',
    description='OpenGaze python wrapper',
    author='Edwin Dalmaijer',
    keywords='opengaze',
    version="0.1",
    py_modules=['opengaze'],
    install_requires=['lxml']
)
