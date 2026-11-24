# A program that supports customer service in an office using a queue.
# A new customer gets a ticket with the next number and goes to the end of the queue.

import queue

customers = queue.Queue()
next_ticket = 1

while True:
    print()
    print('1. New customer')
    print('2. Serve the next customer')
    print('0. Quit')
    option = input('Select an option: ')

    if option == '1':
        customers.put(next_ticket)
        print(f'Your ticket number is {next_ticket}. Customers waiting: {customers.qsize()}')
        next_ticket += 1
    elif option == '2':
        if customers.empty():
            print('No customers are waiting.')
        else:
            # the customer from the beginning of the queue is served first
            print(f'Customer with ticket number {customers.get()}, please go to the desk.')
    elif option == '0':
        break
    else:
        print('Incorrect option.')
