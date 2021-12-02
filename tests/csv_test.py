"""Testing CSV"""
import pytest
from main import csv_add
from main import csv_divide
from main import csv_log_init
from main import absolute_path

def test_csv_add():
    """testing csv add"""
    csv_log_init()
    assert csv_add('csv_files/small1') == True
