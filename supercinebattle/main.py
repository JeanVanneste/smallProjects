from bs4 import BeautifulSoup

with open("2000.html") as fp:
    data = fp.read()

data = data.replace("\n", "")

soup = BeautifulSoup(data, "html.parser")

datas = soup.tbody.find_all("tr")

f = open("2000.csv", 'w')

for data in datas:
    rankRaw = data.contents[0]
    rank = rankRaw.contents[0]
    titleRaw = data.contents[1]
    title = titleRaw.contents[0]
    issueRaw = data.contents[2]
    issue = issueRaw.contents[0]

    f.write(rank+";"+title+";"+issue+"\n")