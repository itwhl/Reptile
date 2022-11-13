import pymongo

client = pymongo.MongoClient('120.55.193.180', 9099)
# print(client)

db = client.spider
# for data in db.douban_movie.find():
#     print(data)
print(db.douban_movie.find_one({'rank': 9.9}))
result = db.douban_movie.insert_one
