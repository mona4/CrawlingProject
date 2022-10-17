import pymongo

def get_db():
    from pymongo import MongoClient
    client = MongoClient('ds153735.mlab.com:53735')
    db = client.mongo1db
    db.authenticate('mounikajamalla','mounika',source='mongodb')
    return db

def get_data(db):
    str = raw_input ( "Enter the word to search : ")
    return db.guardiannews.find({'$text':{'$search':str}})


if __name__ == "__main__":
    db = get_db()
    print
    for data1 in get_data(db):
	print(data1)
