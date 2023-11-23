#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import json

class Movie:
    def __init__(self, title, year, director, quote = ""):
        self.title = title
        self.year = year
        self.director = director
        self.quote = quote


movie_list = []
current_page = 1

while current_page <= 10:

    URL = "https://www.imdb.com/list/ls006266261/?sort=list_order,asc&st_dt=&mode=detail&page=" + str(current_page)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="main")

    movies = results.find_all("div", class_="lister-item mode-detail")

    for movie in movies:
        movie_header = movie.find("h3", class_="lister-item-header")
        movie_quote = movie.find("div", class_="list-description")
        movie_info = movie.find_all("p", class_="text-muted text-small")[1]
        movie_title = movie_header.text.strip().split("\n")[1]
        movie_year = movie_header.text.strip().split("\n")[2]
        movie_director = movie_info.text.strip().split("\n")[1]

        if movie_quote != None:
            m_quote_stripped = movie_quote.text.strip()
            if '"' in m_quote_stripped:
                m_quote_stripped = m_quote_stripped.split('"')[1]
            movie_list.append(Movie(movie_title, movie_year, movie_director, m_quote_stripped))

    current_page = current_page + 1

movie_json = json.dumps([{'title': m.title, 'year': m.year, 'director': m.director, 'quote': m.quote} for m in movie_list], indent=4)

print(movie_json)
with open("movie_list.json", "w") as outfile:
    outfile.write(movie_json)

# print(movie_list[0].title)
# print(movie_list[0].year)
# print(movie_list[0].quote)