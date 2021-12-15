from flask import render_template, request, flash, redirect, url_for, session
from app.controllers.controller import ControllerBase
from calculator.main import Calculator
from csvmanager.manager import CSVManager

class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'You must enter a value for value 1 and or value 2'
        else:
            flash('You successfully calculated')
            # get the values out of the form
            value1 = int(request.form['value1'])
            value2 = int(request.form['value2'])
            operation = request.form['operation']
            my_tuple = (value1, value2)
            check = getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
            if check:
                CSVManager.write(value1, value2, operation, result)
            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result)
        return render_template('calculator.html', error=error)
    @staticmethod
    def get():
        return render_template('calculator.html')


    """
    The easy calculator solution
    1.  fix your calculator to read and write calculations to the csv
    2.  fix the controller to read the the csv to history first
    3.  Fix the controller to write the history to csv after you add the calculation to history
    4.  Make a method on the calculator to return the history in the format you want to print in the template
    """
