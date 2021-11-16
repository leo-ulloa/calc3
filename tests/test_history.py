"""Testing History Functions"""
from calculator.history.calculations import Calculations
from calculator.calculations.subtraction import Subtraction
from calculator.calculations.multiplication import Multiplication


def test_add_calculation_to_history():
    """adding example values to history"""
    nums = (4.0,2.0)
    assert Calculations.add_subtraction_calculation(nums) is True
    assert Calculations.add_addition_calculation(nums) is True
    assert Calculations.add_division_calculation(nums) is True
    assert Calculations.add_multiplication_calculation(nums) is True
def test_history_count():
    """test history count"""
    assert Calculations.count_history() == 4
def test_get_calculation():
    """test get specific calculation"""
    assert Calculations.get_calculation(1).get_result() == 6.0
def test_get_calc_last_result_value():
    """test get last value"""
    assert Calculations.get_last_value() == 8.0
def test_get_calc_last_result_object():
    """test get last object"""
    assert isinstance(Calculations.get_last_calculation(), Multiplication)
def test_get_calc_first_result_value():
    """test get first value"""
    assert Calculations.get_first_value() == 2.0
def test_get_calc_first_result_object():
    """test get first object"""
    assert isinstance(Calculations.get_first_calculation(), Subtraction)
def test_clear_calculation_history():
    """test clear history"""
    assert Calculations.clear_history() is True
    assert Calculations.count_history() == 0
