# A program that tries to read a file that does not exist and handles the error with try-except.

# there is no file with this name on the disk
file_name = 'xyz.txt'

# the code that may raise an exception is in the try block
try:
    with open(file_name) as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    # this block runs only when the file does not exist, so the program does not crash
    print(f"Hey! The file {file_name} does not exist.")

print('The program is still running.')
