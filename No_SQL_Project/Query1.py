import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://sahi:sonu1234@cluster0.t8qum.mongodb.net/test?authSource=admin&replicaSet=atlas-9l9tl7-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
    db = client.test
    col = db.countries
    con = db.continents

    # 1-- Get all the country where a letter or word given is in the name=> for example: FR Fran...
    def find_country():
        word=str(input("Enter the word"))
        for country in col.find({"Name":{'$regex':word,'$options':'i'}}):
            print(country['Name'])
    find_country()

if __name__ == '__main__':
    connectdb()
