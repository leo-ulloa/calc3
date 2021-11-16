"""Calculator"""
from calculator.history.calculations import Calculations
class Calculator:
    """Calculator class"""
    @staticmethod
    def add_numbers(values: tuple):
        """sum of tuple"""
        Calculations.add_addition_calculation(values)
        return Calculations.get_last_value()
    @staticmethod
    def subtract_numbers(values: tuple):
        """subtract tuple"""
        Calculations.add_subtraction_calculation(values)
        return Calculations.get_last_value()
    @staticmethod
    def multiply_numbers(values: tuple):
        """multiply tuple"""
        Calculations.add_multiplication_calculation(values)
        return Calculations.get_last_value()
    @staticmethod
    def divide_numbers(values: tuple):
        """divide tuple sequentially"""
        Calculations.add_division_calculation(values)
        return Calculations.get_last_value()
