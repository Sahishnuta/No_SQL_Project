import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://sahi:sonu1234@cluster0.t8qum.mongodb.net/test?authSource=admin&replicaSet=atlas-9l9tl7-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
    db = client.test
    col = db.countries
    con = db.continents
    # 7-- Get countries which have a ‘u’ in their name and more 100 000 people inside
    def query7():
        for continents in col.find({
                    'Name':
                        {'$regex': 'u', '$options': 'i'}, 'Population': {'$gt': 100000}
                }
        ).sort("population"):
            print( continents['Name'], continents['Population'])
    query7()

if __name__ == '__main__':
    connectdb()
