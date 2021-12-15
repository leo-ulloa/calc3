"""Calculator"""
from calculator.history.calculations import Calculations
class Calculator:
    """Calculator class"""
    @staticmethod
    def get_last_result_value():
        """ This is the gets the result of the calculation"""
        return Calculations.get_last_value()
    @staticmethod
    def addition(values: tuple):
        """sum of tuple"""
        Calculations.add_addition_calculation(values)
        return True
    @staticmethod
    def subtraction(values: tuple):
        """subtract tuple"""
        Calculations.add_subtraction_calculation(values)
        return True
    @staticmethod
    def multiplication(values: tuple):
        """multiply tuple"""
        Calculations.add_multiplication_calculation(values)
        return True
    @staticmethod
    def division(values: tuple):
        """divide tuple sequentially"""
        Calculations.add_division_calculation(values)
        return True
