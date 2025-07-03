class Movie:
    def __init__(self, name, rating, genre):
        self.name = name
        self.rating = rating
        self.genre = genre

def filter_movies(movies, genre):
    print(f"Movies in the genre '{genre}':")
    for movie in movies:
        if movie.genre.lower() == genre.lower():
            print(movie.name)

movies = [
    Movie("Inception", 8.8, "Sci-Fi"),
    Movie("The Godfather", 9.2, "Crime"),
    Movie("The Dark Knight", 9.0, "Action"),
    Movie("Pulp Fiction", 8.9, "Crime"),
    Movie("Interstellar", 8.6, "Sci-Fi"),
    Movie("The Matrix", 8.7, "Sci-Fi"),
]

filter_movies(movies, "Sci-Fi")
