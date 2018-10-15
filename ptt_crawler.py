import os,time
from datetime import datetime
from bs4 import BeautifulSoup

ptt_url = 'https://www.ptt.cc/bbs/index.html'
board_url = 'https://www.ptt.cc/bbs/{board}/index{index}.html'

def parse_article(html)

def parse_board(html):
	soup = BeautifulSoup(html, 'html.parser')
	boards = list()
	for div in soup.find_all('div', class_={'board-name'}):
		print div
		boards.append(div.string)
	return boards

output = 'bindex_'+datetime.now().strftime("%Y%m%d_%H%M%S")+'.html'
os.system("wget "+ptt_url+" -O "+output)

with open(output, 'r') as index_file:
	board_index = index_file.read()

boards = parse_board(board_index)
print len(boards), boards
