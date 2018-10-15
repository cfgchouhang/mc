import os,time
from datetime import datetime
from bs4 import BeautifulSoup

ptt_url = 'https://www.ptt.cc/bbs/index.html'
board_url = 'https://www.ptt.cc/bbs/{board}/index{index}.html'

html = '{name}_{time}.html'

def parse_board(html, board):
    soup = BeautifulSoup(html, 'html.parser')
    articles = list()
    for link in soup.find_all('a'):
        if board in link.get('href'):
            print link.get('href'), link.string

def parse_ptt(html):
    soup = BeautifulSoup(html, 'html.parser')
    boards = list()
    for div in soup.find_all('div', class_={'board-name'}):
        print div
        boards.append(div.string)
    return boards

ptt_index_file = html.format(name='index', time=datetime.now().strftime("%Y%m%d_%H%M%S"))
os.system("wget "+ptt_url+" -O "+ptt_index_file)

with open(ptt_index_file, 'r') as index_file:
    ptt_index = index_file.read()

boards = parse_ptt(ptt_index)
for b in boards[:2]:
    print 'download index '+b
    board_index_file = html.format(name=b, time=datetime.now().strftime("%Y%m%d_%H%M%S"))
    os.system(
        "wget " +
        board_url.format(board=b, index='') +
        " -O " +
        board_index_file
    )
    with open(board_index_file, 'r') as index_file:
        board_index = index_file.read()
    
    parse_board(board_index, b)
    time.sleep(5)
