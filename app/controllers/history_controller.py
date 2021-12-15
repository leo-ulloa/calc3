from flask import render_template
from app.controllers.controller import ControllerBase
from csvmanager.manager import CSVManager


class HistoryController(ControllerBase):
    @staticmethod
    def get():
        """csv"""
        return render_template("history.html", titles=CSVManager.column_values(), row_data=CSVManager.read(), zip=zip)