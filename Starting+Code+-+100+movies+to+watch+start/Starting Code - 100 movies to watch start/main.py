import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)

data = response.text

soup = BeautifulSoup(data, "html.parser")

titles = []

movie_titles = soup.find_all(name="h3", class_="title")

for title in movie_titles:
    titles.append(title.text)

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for title in range(len(movie_titles)-1, -1, -1):
        file.write(titles[title]+"\n")

