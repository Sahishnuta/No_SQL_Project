import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient("mongodb+srv://sahi:sonu1234@cluster0.t8qum.mongodb.net/test?authSource=admin&replicaSet=atlas-9l9tl7-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
    db = client.test
    con = db.continents
    #  3-- Send back the fourth countries of a continent by alphabetic order
    continents = con.find({},{'Name':1, 'countries':{'$slice':4}}).sort("Name")
    for FourCountry in continents:
        print(FourCountry)


if __name__ == '__main__':
        connectdb()