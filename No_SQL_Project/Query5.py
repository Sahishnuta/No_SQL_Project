import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://sahi:sonu1234@cluster0.t8qum.mongodb.net/test?authSource=admin&replicaSet=atlas-9l9tl7-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
    db = client.test
    col = db.countries
    con = db.continents

    # 6-- Get all the countries order by number of people first the less populated and last the most populated
    def orderbypopulation():
        for countries in col.find({}).sort("Population"):
            print(countries['Name'], countries['Population'])
    orderbypopulation()

if __name__ == '__main__':
    connectdb()