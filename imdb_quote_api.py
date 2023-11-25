from fastapi import FastAPI
from pydantic import BaseModel
import json
import random

app = FastAPI()

movie_list = []

class Movie:
    def __init__(self, title, year, director, stars, quote = ""):
        self.title = title
        self.year = year
        self.director = director
        self.stars = stars
        self.quote = quote

# change this path to that of the included movie_list.json file
with open('/home/timbo/src/Uvicorn/Pico_QuoteGame_and_API/movie_list.json', 'r') as infile:
    movie_json = json.load(infile)

for movie in movie_json:
    star_list = []
    for star in movie['stars']:
        star_list.append(star)
    movie_list.append(Movie(movie['title'], movie['year'], movie['director'], star_list, movie['quote']))

@app.get("/movie/{movie_num}")
def get_movie(movie_num: int = 0):
    return {movie_list[movie_num]}

@app.get("/random_movie")
def get_random_movie():
    random_movie = random.choice(movie_list)
    print(random_movie.title)
    return {random_movie}
