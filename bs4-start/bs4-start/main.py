from bs4 import BeautifulSoup

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title.string)
# # print(soup.prettify())
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))


import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

hacker = BeautifulSoup(response.text, "html.parser")

contents = hacker.find_all(name="a", class_="storylink")

scores = hacker.find_all(name="span", class_="score")

article_title = []
article_link = []
article_score = []

for story in contents:
    article_title.append(story.text)
    article_link.append(story.get("href"))

for score in scores:
    score_points = int(score.text.split(" ")[0])
    article_score.append(score_points)

index = article_score.index(max(article_score))

print(article_title[index])
print(article_link[index])