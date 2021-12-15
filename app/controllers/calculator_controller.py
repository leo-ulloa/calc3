from flask import render_template, request, flash, redirect, url_for, session
from app.controllers.controller import ControllerBase
from calculator.main import Calculator




class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'You must enter a value for value 1 and or value 2'
        else:
            flash('You successfully calculated')
            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
            # Hey if you copy this it will not work you need to think about it
            data = {
                'value1': [value1],
                'value2': [value2],
                'operation': [operation]
            }
            return render_template('result.html', data=Calculator.getHistory(), value1=value1, value2=value2, operation=operation, result=result)
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
