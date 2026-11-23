# A program that writes the details of a movie to a text file.

# Variables containing movie details
movie_title = "Inception"
director = "Christopher Nolan"
lead_actor = "Leonardo DiCaprio"

# Name of the file to write to
file_name = 'movie_details.txt'

# 'w' (write) creates the file or overwrites it; \n moves the cursor to the next line
with open(file_name, 'w') as file:
    file.write(f"Movie Title: {movie_title}\n")
    file.write(f"Director: {director}\n")
    file.write(f"Lead Actor: {lead_actor}\n")

print(f"Movie details have been written to {file_name}.")
