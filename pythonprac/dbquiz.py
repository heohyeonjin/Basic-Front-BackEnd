#크롤링 연습

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

#매트릭스 평점 가져오기
movie = db.movies.find_one({'title':'헬프'},{'_id':False})
target_star = movie['star']
print(target_star)

#매트릭스와 같은 평점 영화 제목들
target_movies = list(db.movies.find({'star':target_star},{'_id':False}))
for target in target_movies:
    print(target['title'])

#매트릭스 평점 0으로
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})