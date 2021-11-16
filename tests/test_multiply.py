"""Testing Multiplication"""
from calculator.calculations.multiplication import Multiplication

def test_calculation_subtraction():
    """testing that our calculator has a static method for multiplication"""
    nums = (4.0,2.0)
    multiplication = Multiplication(nums)
    assert multiplication.get_result() == 8.0
