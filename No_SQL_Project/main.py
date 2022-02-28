import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://sahi:sonu1234@cluster0.t8qum.mongodb.net/test?authSource=admin&replicaSet=atlas-9l9tl7-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
    db = client.test
    col = db.countries
    con = db.continents
    print(db.list_collection_names())


    cursor= col.find({})
    for i in cursor:
        print(i)
    cont=con.find({})
    for a in cont:
        print(a)


if __name__ == '__main__':
    connectdb()
