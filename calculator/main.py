""" This is the increment function"""
from calculator.calculations.addition import Addition
from calculator.calculations.subtraction import Subtraction
from calculator.calculations.multiplication import Multiplication
from calculator.calculations.division import Division

class Calculator:
    """ This is the Calculator class"""
    history = []
    @staticmethod
    def get_history_size():
        """ get the number of calculations from history"""
        return len(Calculator.history)
    @staticmethod
    def clear_history():
        """ Clear the calculation history"""
        Calculator.history.clear()
        return True
    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculator.history[num]
    @staticmethod
    def remove_calculation(num):
        """ remove a specific calculation from history"""
        for item in Calculator.history:
            if item == num:
                Calculator.history.remove(item)
        return True
    @staticmethod
    def get_calculation_last():
        """ get last calculation from history"""
        return Calculator.history[-1]
    @staticmethod
    def get_calculation_first():
        """ get first calculation from history"""
        return Calculator.history[0]
    @staticmethod
    def add_numbers(*args):
        """ adds list of numbers"""
        addition = Addition(args)
        Calculator.history.append(addition)
        return addition.get_result()
    @staticmethod
    def subtract_numbers(*args):
        """ subtract a list of numbers from result"""
        subtraction = Subtraction(args)
        Calculator.history.append(subtraction)
        return subtraction.get_result()
    @staticmethod
    def multiply_numbers(*args):
        """ multiplication number from result"""
        multiplication = Multiplication(args)
        return multiplication.get_result()
    @staticmethod
    def divide_numbers(*args):
        """ divide number from result"""
        division = Division(args)
        return division.get_result()
