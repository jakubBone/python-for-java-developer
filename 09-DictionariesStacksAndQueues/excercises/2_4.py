# A program that finds spam in the received emails.

emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}
spam_list = {"spam1@example.com", "spam2@example.com"}

# the intersection of sets: elements that are in both sets
spam_emails = emails_received & spam_list
print("Spam emails:", spam_emails)
