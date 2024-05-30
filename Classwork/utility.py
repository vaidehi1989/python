import math as m

# decorator
def is_int(func_obj):
    def validate(*numbers):
        if all([type(num) == int for num in numbers]):
            return func_obj(*numbers)
        else:
            return "Invalid"
    return validate

@is_int
def factorial(num):
    return m.prod(range(num, 1, -1))

@is_int
def odd_even(num):
    return "even" if num % 2 == 0 else "odd"

@is_int
def add_nos(num1, num2):
    return num1 + num2
