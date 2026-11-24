# A program with a function that uses a stack to check whether the brackets (), {}, [] are used correctly.

import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # brackets ok
expression2 = "[(2+3]/4)"                  # brackets not correct
expression3 = "(2-3*4+(5/6)"               # brackets not correct


def brackets_ok(expression):
    # every closing bracket and the opening bracket that has to be on the top of the stack
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = queue.LifoQueue()

    for char in expression:
        if char in '([{':
            # an opening bracket goes on the stack
            stack.put(char)
        elif char in ')]}':
            # a closing bracket needs an opening one on the top of the stack
            if stack.empty():
                return False
            opening = stack.get()
            if opening != pairs[char]:
                return False
        # all other characters are skipped

    # if something is left on the stack, there are brackets that were not closed
    return stack.empty()


for expression in (expression1, expression2, expression3):
    if brackets_ok(expression):
        print(f'{expression} -> brackets are ok')
    else:
        print(f'{expression} -> brackets are not correct')
