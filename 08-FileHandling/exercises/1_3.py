# A program that opens a text file in a with block and reads its whole content.

# 'with' acts as a context manager: 
#   it safely opens the file and it closes automatically (even if an error occurs)
# 'r' (read) is the default mode 
# 'file' is kind of local variable to assign .txt  
with open('countries.txt', 'r') as file:
    content = file.read()  # read() returns the whole content of the file as one string

print(content)
