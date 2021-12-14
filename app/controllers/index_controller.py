"""A simple flask web app"""
from flask import render_template
from controller import ControllerBase
# pylint: disable=(too-few-public-methods)
class IndexController(ControllerBase):
    """A simple flask web app"""
    @staticmethod
    def get():
        """A simple flask web app"""
        return render_template('index.html')
