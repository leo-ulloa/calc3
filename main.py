"""main"""
from pathlib import Path
import time
from datetime import datetime
import pandas as pd
from calculator.calc import Calculator

def csv_log_init():
    """create log file"""
    thing = []
    data_f = pd.DataFrame(thing, columns = ['Operation', 'Result', 'Unix', 'File Name'])
    data_f.to_csv('csv_logs/logfile.csv', mode='a',index=False, header=False)
    return True

def absolute_path(filepath):
    """absolute path"""
    relative = Path(filepath)
    return relative.absolute()

def csv_add(filename):
    """add"""
    file = absolute_path(filename)
    dataframe = pd.read_csv(file)
    tup = tuple(list(dataframe[1]))
    calculator = Calculator()
    result = calculator.add_numbers(tup)
    timestamp = time.time()
    unix = datetime.fromtimestamp(timestamp)
    data = ['Addition', result, unix, file.name]
    data_f = pd.DataFrame(data, columns=['Operation', 'Result', 'Unix', 'File Name'])
    data_f.to_csv('csv_logs/logfile.csv', mode='a',index=False, header=False)
    return True

def csv_subtract(filename):
    """subtract"""
    file = absolute_path(filename)
    dataframe = pd.read_csv(file)
    tup = tuple(list(dataframe[1]))
    calculator = Calculator()
    result = calculator.subtract_numbers(tup)
    timestamp = time.time()
    unix = datetime.fromtimestamp(timestamp)
    data = ['Subtraction', result, unix, file.name]
    data_f = pd.DataFrame(data, columns=['Operation', 'Result', 'Unix', 'File Name'])
    data_f.to_csv('csv_logs/logfile.csv', mode='a',index=False, header=False)
    return True


def csv_multiply(filename):
    """multiply"""
    file = absolute_path(filename)
    dataframe = pd.read_csv(file)
    tup = tuple(list(dataframe[1]))
    calculator = Calculator()
    result = calculator.multiply_numbers(tup)
    timestamp = time.time()
    unix = datetime.fromtimestamp(timestamp)
    data = ['Multiplication', result, unix, file.name]
    data_f = pd.DataFrame(data, columns=['Operation', 'Result', 'Unix', 'File Name'])
    data_f.to_csv('csv_logs/logfile.csv', mode='a',index=False, header=False)
    return True

def csv_divide(filename):
    """divide"""
    file = absolute_path(filename)
    dataframe = pd.read_csv(file)
    tup = tuple(list(dataframe[1]))
    calculator = Calculator()
    result = calculator.divide_numbers(tup)
    timestamp = time.time()
    unix = datetime.fromtimestamp(timestamp)
    data = ['Division', result, unix, file.name]
    data_f = pd.DataFrame(data, columns=['Operation', 'Result', 'Unix', 'File Name'])
    data_f.to_csv('csv_logs/logfile.csv', mode='a',index=False, header=False)
    return True
