import os,time
from datetime import datetime
from bs4 import BeautifulSoup
import json, requests

ptt_url = 'https://www.ptt.cc/bbs/index.html'


def parse_ptt(html):
    soup = BeautifulSoup(html, 'html.parser')
    boards = list()
    for div in soup.find_all('div', class_={'board-name'}):
        boards.append(div.string)
    return boards

r = requests.get(ptt_url)
if r.status_code == 200:
    boards = parse_ptt(r.text)
    with open('boards.json', 'w') as outfile:
        json.dump(boards, outfile)
