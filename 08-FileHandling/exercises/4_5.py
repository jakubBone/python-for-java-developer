# A program that prints the sender, the recipient, the subject and the body of the email from email.txt
# (the functions are in the module emails).

import emails

print('Sender:', emails.email_sender())
print('Recipient:', emails.email_recipient())
print('Subject:', emails.email_subject())
print('Body:')
print(emails.email_body())
