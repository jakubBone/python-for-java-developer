# A module with functions that fetch parts of an email from the file email.txt using regular expressions.

import re


def read_email():
    with open('email.txt', 'r', encoding='utf-8') as file:
        return file.read()


def email_sender():
    # the line "From: Name <address>": the address is between < and >
    # re.MULTILINE makes ^ match at the beginning of every line
    match = re.search(r'^From: .*<(.+?)>', read_email(), re.MULTILINE)
    return match.group(1)


def email_recipient():
    match = re.search(r'^To: .*<(.+?)>', read_email(), re.MULTILINE)
    return match.group(1)


def email_subject():
    match = re.search(r'^Subject: (.*)$', read_email(), re.MULTILINE)
    return match.group(1)


def email_body():
    # the body starts after the first empty line (the headers end there)
    match = re.search(r'\n\n(.*)', read_email(), re.DOTALL)
    return match.group(1).strip()
