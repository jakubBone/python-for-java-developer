# A program that calculates RPN (Reverse Polish Notation) expressions using a stack.
# Enter numbers, operators (+ - * /) and the equal sign (=), each in a separate line.

import queue

stack = queue.LifoQueue()

while True:
    token = input('Enter a number, an operator or =: ')

    if token == '=':
        # the equal sign: the final result is the last element on the stack
        print('Result:', f'{stack.get():g}')
        break
    elif token in ('+', '-', '*', '/'):
        # an operator: take two numbers from the stack (the second number is on the top)
        second = stack.get()
        first = stack.get()
        if token == '+':
            result = first + second
        elif token == '-':
            result = first - second
        elif token == '*':
            result = first * second
        else:
            result = first / second
        stack.put(result)
    else:
        # a number goes on the stack
        stack.put(float(token))
