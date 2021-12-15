"""A simple flask web app"""
# pylint: disable=(too-few-public-methods)
# pylint: disable=(no-name-in-module)
# pylint: disable=(import-error)
from flask import render_template
from app.controllers.controller import ControllerBase

class IndexController(ControllerBase):
    """A simple flask web app"""
    @staticmethod
    def get():
        """A simple flask web app"""
        return render_template('index.html')
