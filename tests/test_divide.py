"""Testing Division"""

from calculator.calculations.division import Division


def test_calculation_division():
    """testing that calculator has a static method for division"""

    nums = (8.0,2.0)
    division = Division(nums)
    assert division.get_result() == 4.0

def test_division_throws_exception():
    """test divide by 0 raises error"""
    nums = (10.0, 0.0)
    err_test = Division(nums)
    assert err_test.get_result() == "ZeroDivisionError"
