# A program that checks whether a user has all the required permissions.

required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}

# issubset() is True when all elements of the set are in the other set;
# the user has the permissions when the required ones are a subset of the user's ones
has_permissions = required_permissions.issubset(user_permissions)
print(has_permissions)  # False, because "execute" is missing
