"""Testing Division"""
from calculator.calculations.division import Division

def test_calculation_subtraction():
    """testing that our calculator has a static method for multiplication"""
    #Arrange
    nums = (8.0,2.0)
    division = Division(nums)
    #Act
    #Assert
    assert division.get_result() == 4.0
