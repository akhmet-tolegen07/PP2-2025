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
}]

def func1(movie):
    return movie["imdb"] > 5.5

def func2(movies_list):
    return [movie for movie in movies_list if movie["imdb"] > 5.5]

def func3(movies_list, category):
    return [movie for movie in movies_list if movie["category"] == category]

def func4(movies_list):
    total_imdb = sum(movie["imdb"] for movie in movies_list)
    return total_imdb / len(movies_list)

def func5(movies_list, category):
    category_movies = [movie for movie in movies_list if movie["category"] == category]
    if category_movies:
        total_imdb = sum(movie["imdb"] for movie in category_movies)
        return total_imdb / len(category_movies)
    return 0

print(func1(movies[0]))

print(func2(movies))

print(func3(movies, "Crime"))

print(func4(movies)) 

print(func5(movies, "Crime")) 