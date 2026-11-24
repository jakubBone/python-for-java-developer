# A program that simulates the Back key in a web browser using a stack.

import queue

# a stack of the previously visited websites
visited_websites = queue.LifoQueue()

# some previously visited websites
visited_websites.put('instagram.com')
visited_websites.put('uek.krakow.pl')
visited_websites.put('microsoft.com')

# the website that is viewed now (nothing at the start)
current = None

while True:
    website = input('Enter website name (0 for back): ')

    if website == '0':
        if visited_websites.empty():
            break
        else:
            print('<-- Going back to a previously visited website')
            # the previous website is taken from the top of the stack
            current = visited_websites.get()
    elif website != "":
        # the website viewed so far goes to the stack, so that Back can return to it
        if current is not None:
            visited_websites.put(current)
        current = website

    # print name of website you are currently viewing
    print('You are currently viewing:', current)
    print()
