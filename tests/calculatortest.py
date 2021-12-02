"""Testing Calculator"""
from calculator.calc import Calculator
from calculator.history.calculations import Calculations

def test_calculator_add_static():
    """addition"""
    Calculations.clear_history()
    my_tuple = (1.0,2.0,5.0)
    assert Calculator.add_numbers(my_tuple) == 8.0

def test_calculator_subtract_static():
    """subtract"""
    Calculations.clear_history()
    my_tuple = (1.0,2.0,3.0)
    assert Calculator.subtract_numbers(my_tuple) == -4.0

def test_calculator_multiply_static():
    """multiply"""
    Calculations.clear_history()
    my_tuple = (1.0,2.0,3.0)
    assert Calculator.multiply_numbers(my_tuple) == 6.0

def test_calculator_divide_static():
    """divide"""
    Calculations.clear_history()
    my_tuple = (20.0,2.0,5.0)
    assert Calculator.divide_numbers(my_tuple) == 2.0
