from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# 저장 - 예시
doc = {'name':'bobby','age':21} #딕셔너리 생성 mongodb는 DB에 리스트를 쌓는 형식
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})
user = db.users.find_one({'name':'bobby'},{'_id':False})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False})) #전 중괄호 : 조건, 후 중괄호 : id는 표시X

# for person in same_ages:
#     print(person) --> list한줄씩 출력

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
#db.users.update_many: 위험

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})
#db.users.delete_many : 위험