import json
from bs4 import BeautifulSoup
import requests

html_doc = requests.get('https://www.ubhara.ac.id/v3/p/fasilitas')

soup = BeautifulSoup(html_doc.text, 'html.parser')

judul = []
isi = []

a = soup.select('div.panel-body > p > strong')

for ab in a:
    judul.append(ab.get_text())


b = soup.select('div.panel-body > ul')

z = b[0].select('ul > li')

for bc in b:
    temp = []
    for bd in bc.select('ul > li'):
        temp.append(bd.get_text())
    isi.append(temp)

y = []
for x in range(3):
    y.append({
        'Judul' : judul[x],
        'Isi' : isi[x]
    })

# Serializing json 
json_object = json.dumps(y, indent = 4)
  
# Writing to sample.json
with open("hasilFasilitasUbhara.json", "a") as outfile:
    outfile.write(json_object)
