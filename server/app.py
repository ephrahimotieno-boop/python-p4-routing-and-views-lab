#!/usr/bin/env python3

from flask import Flask
import io
import sys

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string_param>')
def print_string(string_param):
    # Print to console
    print(string_param)
    # Return the string in browser
    return string_param


@app.route('/count/<int:count_param>')
def count(count_param):
    # Display all numbers from 0 to count_param-1 on separate lines
    result = '\n'.join(str(i) for i in range(count_param)) + '\n'
    return result


@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'
    
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)

