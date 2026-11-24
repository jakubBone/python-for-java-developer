# A program that combines two contact lists and removes duplicates.

contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}
contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}

# the union of sets: all elements from both sets, each only once
merged_contacts = contacts_A | contacts_B
print("Merged contacts:", merged_contacts)
