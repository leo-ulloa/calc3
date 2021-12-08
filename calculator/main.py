"""Calculator"""
from calculator.history.calculations import Calculations
class Calculator:
    """Calculator class"""
    @staticmethod
    def get_last_result_value():
        """ This is the gets the result of the calculation"""
        return Calculations.get_last_calculation()
    @staticmethod
    def add_numbers(values: tuple):
        """sum of tuple"""
        Calculations.add_addition_calculation(values)
        return True
    @staticmethod
    def subtract_numbers(values: tuple):
        """subtract tuple"""
        Calculations.add_subtraction_calculation(values)
        return True
    @staticmethod
    def multiply_numbers(values: tuple):
        """multiply tuple"""
        Calculations.add_multiplication_calculation(values)
        return True
    @staticmethod
    def divide_numbers(values: tuple):
        """divide tuple sequentially"""
        Calculations.add_division_calculation(values)
        return True
