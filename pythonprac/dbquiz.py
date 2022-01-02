from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 한 개 찾기 - 예시
movie = db.movies.find_one({'title':'매트릭스'})
target_star = movie['star']

target_movies = list(db.movies.find({'star':target_star}, {'_id':False}))
for target in target_movies:
    print(target['title'])