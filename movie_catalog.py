movie_collection = [
    ("Inception", "Christopher Nolan", 2010),
    ("The Godfather", "Francis Ford Coppola", 1972),
    ("The Matrix", "Lana and Lilly Wachowski", 1999),
    ("Parasite", "Bong Joon-ho", 2019),
    ("Interstellar", "Christopher Nolan", 2014)
]

def add_movie(title, director, year):
    new_movie = (title, director, year)
    movie_collection.append(new_movie)
    print(f"Movie '{title}' by {director} added to the catalog.")

add_movie("Ella Enchanted", "Tommy O'Haver", "2004")

def display_movies():
    print(f"Movie List:")
    for title, director, year in movie_collection:
        print(f"Title: '{title}, Director: {director}, Year: {year}")

display_movies()

def search_by_director(director):
    movies_by_director = []
    for movie in movie_collection:
        title, movie_director, year = movie
        if movie_director.lower() == director.lower():
            movies_by_director.append(movie)
    return movies_by_director

movies_by_ohaver = search_by_director("Tommy O'Haver")
print("Movies by Tommy O'Haver:")
for title, director, year in movies_by_ohaver:
    print(f"Title: {title}, Year: {year}")

