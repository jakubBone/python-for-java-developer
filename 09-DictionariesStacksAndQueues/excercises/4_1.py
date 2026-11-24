# A program that shows a queue: the first element put is the first one taken (FIFO).

import queue

# creates a queue
people = queue.Queue()

# adds items to the end of the queue
people.put('Michael')
people.put('Charlotte')
people.put('Olivia')

# prints the number of elements of the queue
print('Number of queue elements:', people.qsize())

# gets and prints items from the beginning of the queue
while not people.empty():
    person = people.get()
    print(person)
