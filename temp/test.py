from bs4 import BeautifulSoup as bs
from pprint import pprint


with open('test.html', 'r') as f:
    html = f.read()

s = bs(html, 'html.parser')
trs = s.find_all('tr')

content_types = {}

for tr in trs:
    ext = tr.find_all('td')[0].text.strip('.')
    typ = tr.find_all('td')[-1].text

    content_types[ext] = typ

pprint(content_types)
