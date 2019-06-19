#!/usr/bin/python3

from bs4 import BeautifulSoup
import urllib.request

with urllib.request.urlopen("https://mjee.fr/classement-du-meilleur-jeu-ever/") as fp:
    data = fp.read().decode('utf-8')

data = data.replace('\n', '')

soup = BeautifulSoup(data, "html.parser")

datas = soup.tbody.find_all("tr")

f = open("mjee.csv", 'w')

for data in datas:
    rankRaw = data.contents[0]
    rank = rankRaw.contents[0]
    titleRaw = data.contents[1]
    title = titleRaw.contents[0]
    genreRaw = data.contents[2]
    genre = genreRaw.contents[0]
    issueRaw = data.contents[3]
    issue = issueRaw.contents[0]

    f.write(rank + ";" + title + ";" + genre + ";" +issue+ "\n")
