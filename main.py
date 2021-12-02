"""main"""
from pathlib import Path
import time
from datetime import datetime
import pandas as pd
from calculator.calc import Calculator


thing = []
data_f = pd.DataFrame(thing, columns = ['Operation', 'Result', 'Unix', 'File Name'])
calculator = Calculator()

def absolute_path(filepath):
    """absolute path"""
    relative = Path(filepath)
    return relative.absolute()

def csv_add(filename):
    """add"""
    file = absolute_path(filename)
    dataframe = pd.read_csv(file)
    tup = tuple(list(dataframe[1]))
    result = calculator.add_numbers(tup)
    timestamp = time.time()
    unix = datetime.fromtimestamp(timestamp)
    data = ['Addition', result, unix, file.name]
    data_f.loc[len(data_f.index)] = data
    data_f.to_csv('logfile.csv', mode='a',index=False, header=False)

def csv_subtract(filename):
    """sub"""
    file = absolute_path(filename)
    dataframe = pd.read_csv(file)
    tup = tuple(list(dataframe[1]))
    result = calculator.subtract_numbers(tup)
    timestamp = time.time()
    unix = datetime.fromtimestamp(timestamp)
    data = ['Subtraction', result, unix, file.name]
    data_f.loc[len(data_f.index)] = data
    data_f.to_csv('logfile.csv', mode='a',index=False, header=False)


def csv_multiply(filename):
    """multiply"""
    file = absolute_path(filename)
    dataframe = pd.read_csv(file)
    tup = tuple(list(dataframe[1]))
    result = calculator.multiply_numbers(tup)
    timestamp = time.time()
    unix = datetime.fromtimestamp(timestamp)
    data = ['Multiplication', result, unix, file.name]
    data_f.loc[len(data_f.index)] = data
    data_f.to_csv('logfile.csv', mode='a',index=False, header=False)

def csv_divide(filename):
    """divide"""
    file = absolute_path(filename)
    dataframe = pd.read_csv(file)
    tup = tuple(list(dataframe[1]))
    result = calculator.divide_numbers(tup)
    if result == ZeroDivisionError:
        timestamp = time.time()
        unix = datetime.fromtimestamp(timestamp)
        data = ['Division', result, unix, file.name]
        data_f.loc[len(data_f.index)] = data
        data_f.to_csv('logfile.csv', mode='a', index=False, header=False)
    else:
        timestamp = time.time()
        unix = datetime.fromtimestamp(timestamp)
        data = ['Division', result, unix, file.name]
        data_f.loc[len(data_f.index)] = data
        data_f.to_csv('logfile.csv', mode='a',index=False, header=False)
