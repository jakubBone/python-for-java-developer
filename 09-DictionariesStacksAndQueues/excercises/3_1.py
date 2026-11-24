# A program that puts numbers on a stack, sums the last two numbers and then the remaining ones.

import queue

# a stack: the last element put is the first one taken (LIFO)
stack = queue.LifoQueue()

for number in (2, 3, 7, 4, 1, 9, 8):
    stack.put(number)

# take the last two numbers from the top of the stack (8 and 9) and sum them
last = stack.get()
last_but_one = stack.get()
print('Sum of the last two numbers:', last + last_but_one)

# sum the remaining elements of the stack with a while loop
total = 0
while not stack.empty():
    total += stack.get()
print('Sum of the remaining elements:', total)
