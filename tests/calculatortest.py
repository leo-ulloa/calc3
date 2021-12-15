"""Testing Calculator"""
from calculator.main import Calculator
from calculator.history.calculations import Calculations

def test_calculator_add_static():
    """addition"""
    Calculations.clear_history()
    my_tuple = (1.0,2.0,5.0)
    Calculator.addition(my_tuple)
    assert Calculator.get_last_result_value() == 8.0

def test_calculator_subtract_static():
    """subtract"""
    Calculations.clear_history()
    my_tuple = (1.0,2.0,3.0)
    Calculator.subtraction(my_tuple)
    assert Calculator.get_last_result_value() == -4.0

def test_calculator_multiply_static():
    """multiply"""
    Calculations.clear_history()
    my_tuple = (1.0,2.0,3.0)
    Calculator.multiplication(my_tuple)
    assert Calculator.get_last_result_value() == 6.0

def test_calculator_divide_static():
    """divide"""
    Calculations.clear_history()
    my_tuple = (20.0,2.0,5.0)
    Calculator.division(my_tuple)
    assert Calculator.get_last_result_value() == 8.0
