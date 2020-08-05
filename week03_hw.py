import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')


music = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for songs in music:
    rank = songs.select_one('td.number').text.strip()
    title = songs.select_one('td.info > a.title.ellipsis').text.strip()
    singer = songs.select_one('td.info > a.artist.ellipsis').text.strip()
    print(rank, title, singer)

    doc = {
            'rank': rank,
            'title': title,
            'singer': singer
        }

    db.music.insert_one(doc)
#
# #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
# for songs in music:
#     a_song = songs.select_one('td.number')
#     if a_song is not None:
#
#         print(a_song.text)
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
        # body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis