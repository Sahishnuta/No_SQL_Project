import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://sahi:sonu1234@cluster0.t8qum.mongodb.net/test?authSource=admin&replicaSet=atlas-9l9tl7-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
    db = client.test
    col = db.countries
    con = db.continents
    # 2-- Send the list of continent with there number of countries
    def continents():
        agg_pipeline = [
        {
            '$project': {
                'name': "$name",
                'countries': {'$size': "$countries"}}
        }
        ]
        cont = con.aggregate(agg_pipeline)
        for continent in cont:
            print(continent)
    continents()

if __name__ == '__main__':
    connectdb()