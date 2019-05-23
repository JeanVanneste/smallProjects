from bs4 import BeautifulSoup
import urllib.request

print("Décennies ?")
decade = input()

with urllib.request.urlopen("https://www.supercinebattle.fr/la-liste-ultime-des-films-des-annees-"+decade+"/") as fp:
    data = fp.read().decode('utf-8')

data = data.replace("\n", "")

soup = BeautifulSoup(data, "html.parser")

datas = soup.tbody.find_all("tr")

f = open(decade+".csv", 'w')

for data in datas:
    rankRaw = data.contents[0]
    rank = rankRaw.contents[0]
    titleRaw = data.contents[1]
    title = titleRaw.contents[0]
    issueRaw = data.contents[2]
    issue = issueRaw.contents[0]

    f.write(rank+";"+title+";"+issue+"\n")