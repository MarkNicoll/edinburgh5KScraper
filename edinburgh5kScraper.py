import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen

userName = sys.argv[1] + ' ' + sys.argv[2]
url = "https://virtual.edinburghmarathon.com/finishers/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
finishers = soup.find("table", id="finisher_table_837").findAll("tr")

finishersList = []
for finisher in finishers:
    raceData = finisher.findAll("td")[0::2]
    if len(raceData) > 0:
        name = raceData[0].get_text()
        time = float(raceData[1].get_text().replace('1h', '60').replace(
            '2h', '120').replace('m', '.').replace('s', '').replace(' ', ''))
        parsedFinisherData = {'name': name, 'time': time}
        finishersList.append(parsedFinisherData)

sortedFinishers = sorted(finishersList, key=lambda i: i['time'], reverse=False)
finalPosition = next((index for (index, d) in enumerate(
    sortedFinishers) if d["name"] == userName), None)

print(userName + ' finished ' + str(finalPosition) +
      ' out of ' + str(len(sortedFinishers)))
