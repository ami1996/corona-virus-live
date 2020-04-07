import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import matplotlib.pyplot as plt

extracts=lambda row: [x.text.replace('\n','') for x in row]
URL = 'https://www.mohfw.gov.in/'

Short_Headers=['Sn','State','Confirmed','Cured','Death']
response=requests.get(URL).content
soup=BeautifulSoup(response, 'html.parser')
header= extracts(soup.tr.find_all('th'))

stats=[]
all_rows=soup.find_all('tr')

for row in all_rows:
        stat=extracts(row.find_all('td'))
        if stat:
            if len(stat) ==5:
                    stat=['',*stat]
                    stats.append(stat)
            elif len(stat)==6:
                    stats.append(stat)
stats[-1][1]='Total cases'
stats.remove(stats[-1])

performance=[]
state=[]
for row in stats:
        performance.append(int(row[3]))
        state.append(row[2])

table= tabulate(stats, headers=Short_Headers)
print(table)

fig,ax = plt.subplots()
width = 0.75
ax.barh(state,performance,width,color=(234/256.0,128/256.0,252/256.0),
         edgecolor=(106/256.0,27/256.0,154/256.0))
ax.set_yticks(state)

for i, v in enumerate(performance):
    ax.text(v + 3, i - 0.25, str(v), color='blue')
    
plt.xlabel("Number of Active Cases")
plt.title('Corona Virus Cases')
plt.show()
