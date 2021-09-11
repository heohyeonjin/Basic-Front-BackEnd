# meta 태그 (og태그) 크롤링 연습 html내 head에 존재

import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=171539'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# title = soup.select_one('head > meta:nth-child(9)') 이 경우 meta태그 순서와 파이썬 코드 순서가 다를때 데이터가 안나올 수 도있음
title = soup.select_one('meta[property="og:title]')['content'] # 메타 태그 중에서 속성이 일치한 애들 가져와라. ['content']: 그중 내용만
image = soup.select_one('meta[property="og:image]')['content']
desc = soup.select_one('meta[property="og:description]')['content']

# print(title['content']) # 그중 text만 가져와라
# 여기에 코딩을 해서 meta tag를 먼저 가져와보겠습니다.