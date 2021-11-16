"""Subtraction Class"""
from calculator.calculations.calculation import Calculation

class Subtraction(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """get the subtraction results"""
        value_list = []
        for value in self.values:
            value_list.append(value)
        result = value_list[0]
        for num in range(1, len(value_list)):
            result = result - value_list[num]
        return result
