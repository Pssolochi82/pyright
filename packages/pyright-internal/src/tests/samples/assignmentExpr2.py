# This sample tests the Python 3.8 assignment expressions. This sample
# is taken from PEP 257.

# pyright: reportUnusedExpression=false

import re

def foo(x: float):
    ...

def pep572_examples():
    if (match := re.search('123', '252')) is not None:
        print(match)
    print(match)

    file = open('hello')
    while chunk := file.read(8192):
        print(chunk)
    print(chunk)

    def f(x: float):
        return x
    mylist = [y := f(25), y**2, y**3]

    data = [1, 2, 3]
    filtered_data = [y for x in data if (y := f(x)) is not None]
    print(filtered_data)
    
    # This should generate an error.
    y := f(25)  # INVALID
    (y := f(25))  # Valid, though not recommended

    y1 = 1

    # This should generate an error.
    y0 = y1 := f(25)  # INVALID
    y0 = (y1 := f(25))  # Valid, though discouraged

    # This should generate an error.
    foo(x = y := f(25))  # INVALID
    foo(x=(y := f(25)))  # Valid, though probably confusing

    # This should generate an error.
    [y for x in [0, 1] if y := x - 1]

    [y for x in [0, 1] if (y := x - 1)]
