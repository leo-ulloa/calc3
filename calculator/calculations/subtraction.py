"""Subtraction Class"""
from calculator.calculations.calculation import Calculation

class Subtraction(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """get the subtraction results"""
        sub_list = []
        for value in self.values:
            sub_list.append(value)
        result = sub_list[0]
        for num in range(1, len(sub_list)):
            result = result - sub_list[num]
        return result
