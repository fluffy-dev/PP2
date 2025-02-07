 # Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


def is_good(movie_name: str):
    if movie.get(movie_name, 1) < 5.5:
        return False
    return True


def find_good_movies():
    return list(filter(is_good, [movie["name"] for movie in movies]))


def find_by_category(category_name: str):
    return list(filter(lambda x: True if x else False, [movie["name"] if movie["category"] is category_name else None for movie in movies]))


def find_avg(movie_names: list):
    score_sum = 0
    for movie in movies:
        if movie["name"] in movie_names:
            score_sum += movie["imdb"]

    return score_sum/len(movie_name)

def find_avg_of_category(category_name: str):
    movie_names = find_avg_of_category(category_name)
    return find_avg(movie_name)


