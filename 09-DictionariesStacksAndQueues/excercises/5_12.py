# A program with a function that reverses a text using a stack.

import queue


def reverse_text(text):
    stack = queue.LifoQueue()
    # push each character onto the stack
    for char in text:
        stack.put(char)

    # pop the characters: the last one pushed is the first one popped
    reversed_text = ''
    while not stack.empty():
        reversed_text = reversed_text + stack.get()
    return reversed_text


text = input('Enter text: ')
print('Reversed text:', reverse_text(text))
