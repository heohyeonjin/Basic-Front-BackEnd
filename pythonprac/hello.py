#크롤링 연습

import requests #python requests 패키지
from bs4 import BeautifulSoup #크롤링 패키지, 요청한 페이지 잘 솎아내기.

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# r = requests.get('openapi주소')
# rjson = r.json()
# print(rjson) --> ajax의 파이썬 버전 : requests패키지 사용

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers) #페이지 요청

soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)

#title = soup.select_one('')
# print(title.text) --> 태그 사이 텍스트 값 가져오기
# print(title['href']) -->태그 속성 값 가져오기

trs = soup.select('#old_content > table > tbody > tr') #모든 값 가져오기 , select는 결과 값이 리스트로 나옴

# 해당 url에서 검사-> 원하는 html 부분 찾아서 copy selector버튼 눌러서 잘 솎아내기
for tr in trs:
    # print(tr)
    a_tag = tr.select_one('td.title > div > a')
    print(a_tag)
    if a_tag is not None: #null값 제거 (error 방지)
        rank = tr.select_one('td:nth-child(1) > img')['alt']
        title = a_tag.text
        star = tr.select_one('td.point').text
        #딕셔너리 생성
        doc = {
            'rank' :rank,
            'title':title,
            'star':star
        }
        db.movies.insert_one(doc)
