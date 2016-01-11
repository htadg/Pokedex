from lxml import html
from funcs import *
import requests
import pandas as pd

page = requests.get('http://pokemondb.net/pokedex/all')
tree = html.fromstring(page.content)

tr_elements = tree.xpath('//tr')

pok = []

for c in range(1, len(tr_elements)):
    temp = []
    temp_t = []
    for x in tr_elements[c].iterchildren():
        tt = x.text_content().lstrip(' ')
        temp.append(tt)
    # print temp
    temp_t.append(temp[0])
    temp.pop(0)
    temp_t.append(temp)
    pok.append(temp_t)

# print pok

for a in range(len(pok)):
    # print pok[a][1][0],"------",pok[a][1][1]
    pok[a][1][0] = format_name(pok[a][1][0])
    pok[a][1][1] = format_type(pok[a][1][1])

print pok

Dict = {title: column for (title, column) in pok}
df = pd.DataFrame(Dict)

df.to_json('PokemonData.json')

