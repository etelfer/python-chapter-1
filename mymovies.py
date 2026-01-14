# Initialize an empty movie list
favorite_movies = []

# Function to add a movie
def add_movie(movie):

    favorite_movies.append(movie)
    print(f"Movie '{movie}' added.")

# Function to remove a movie
def remove_movie(movie):

    if movie in favorite_movies:
        favorite_movies.remove(movie)
        print(f"Movie '{movie}' removed.")
    else:
        print(f"Movie '{movie}' not found.")

# Function to display all movies
def display_movies():

    print("Movie List:")
    for movie in favorite_movies:
        print(f"- {movie}")

def count_movies():
        print(f"Total number of movies: {len(favorite_movies)}")

def find_movie(movie):
     if movie in favorite_movies:
        print (f"Movie `{movie}` found in list.")

def clear_movies():
    favorite_movies.clear()
    print("All movies have been cleared from list.")
# Adding movies
add_movie("Inception")
add_movie("Harry Potter")
add_movie("Ella Enchanted")

# Displaying movies
display_movies()

# Removing a movie
remove_movie("Inception")

# Displaying movies again
display_movies()

count_movies()

find_movie("Ella Enchanted")

clear_movies()

display_movies()
