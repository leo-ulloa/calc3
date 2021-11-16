"""Calculation history Class"""
from calculator.calculations.addition import Addition
from calculator.calculations.subtraction import Subtraction
from calculator.calculations.multiplication import Multiplication
from calculator.calculations.division import Division
class Calculations:
    """Calculations class manages the history of calculations"""
    history = []
    @staticmethod
    def clear_history():
        """clear history"""
        Calculations.history.clear()
        return True
    @staticmethod
    def count_history():
        """get number of items in history"""
        return len(Calculations.history)
    @staticmethod
    def get_last_calculation():
        """get last calculation"""
        return Calculations.history[-1]
    @staticmethod
    def get_last_value():
        """get last value"""
        calculation = Calculations.get_last_calculation()
        return calculation.get_result()
    @staticmethod
    def get_first_calculation():
        """get first calculation"""
        return Calculations.history[0]
    @staticmethod
    def get_first_value():
        """get first value"""
        calculation = Calculations.get_first_calculation()
        return calculation.get_result()
    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]
    @staticmethod
    def add_calculation(calculation):
        """ add a generic calculation to history"""
        return Calculations.history.append(calculation)
    @staticmethod
    def add_addition_calculation(values):
        """create an addition and add object to history"""
        Calculations.add_calculation(Addition.create(values))
        return True
    @staticmethod
    def add_subtraction_calculation(values):
        """add a subtraction object to history"""
        Calculations.add_calculation(Subtraction.create(values))
        return True
    @staticmethod
    def add_multiplication_calculation(values):
        """Add a multiplication object to history"""
        Calculations.add_calculation(Multiplication.create(values))
        return True
    @staticmethod
    def add_division_calculation(values):
        """Add a division object to history"""
        Calculations.add_calculation(Division.create(values))
        return True
