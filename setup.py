# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
        name = "djangomako" ,
        version = "0.0.1" ,
        description = "a simple django-mako connector for both py2 and py2." ,
        author = "kK" ,
        url = "http://kkblog.org" ,
        license = "MIT" ,
        packages = find_packages(),
        scripts = [ " scripts/test.py " ],
        )
