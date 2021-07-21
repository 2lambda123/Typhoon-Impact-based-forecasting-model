# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 16:01:00 2020

@author: ATeklesadik
"""
from setuptools import setup
PROJECT_NAME = "typhoon_model"

setup(
    name=PROJECT_NAME,
    version="0.1",
    author="Aklilu Teklesadik",
    author_email="ateklesadik@redcross.nl",
    description="Typhoon impact forecasting model",
    package_dir={"": "scr"},
    packages=setuptools.find_packages(where="scr"),
    entry_points={
        'console_scripts': [
            f"run-typhoon-model = {PROJECT_NAME}.pipeline:main",
        ]
    }
)