import requests
from bs4 import BeautifulSoup

#지니 뮤직의 1~50의 곡 스크래핑 하기
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200801',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')


for tr in trs:
    a_tag = tr.select_one('td.info > a.title.ellipsis')
    if a_tag is not None:
        rank = tr.select_one('td.number').text[0:2].strip() #파이썬 문자열자르기, 공백제거 함수 사용
        title =a_tag.text.strip();
        person = tr.select_one('td.info > a.artist.ellipsis').text.strip()
        print(rank, title, person)

