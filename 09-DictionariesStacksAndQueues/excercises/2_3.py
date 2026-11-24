# A program that identifies the students who are absent.

all_students = {"Alice", "John", "Sara", "Bob"}
attended_students = {"Alice", "Bob"}

# the difference of sets: elements of the first set that are not in the second one
absent_students = all_students - attended_students
print(absent_students)
