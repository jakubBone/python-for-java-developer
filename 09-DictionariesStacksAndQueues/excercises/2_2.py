# A program that removes duplicate email addresses.

emails = ["john@example.com", "jane@example.com", "john@example.com", "alex@example.com"]

# a set keeps only unique elements, so the duplicates disappear (the order is not kept)
unique_emails = set(emails)
print(unique_emails)
