# Dictionary of movies
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

def is55(movie):
    return movie["imdb"] > 5.5

movie = {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"}
print(is55(movie))

def above55(movies):
    return [x for x in movies if is55(x)]

def category(movies, category):
    return [x for x in movies if x["category"] == category]

def average(movies):
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies) if movies else 0

def averagebycategory(movies, y):
    x = category(movies, y)
    return average(x)

print(above55(movies))

print(category(movies,"Thriller"))

print(average(movies))

print(averagebycategory(movies,"Thriller"))
