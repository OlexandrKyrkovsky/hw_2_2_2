from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

# Підключення до бази даних MongoDB
uri = "mongodb+srv://oleksandr:ostap0707@atlascluster.9afpddy.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['cats_database']
collection = db['cats']


# Create (створення)
def create_cat(name, age, features):
    cat = {
        "name": name,
        "age": age,
        "features": features
    }
    result = collection.insert_one(cat)
    return result.inserted_id


# Read (читання)
def get_all_cats():
    return list(collection.find())


def get_cat_by_name(name):
    return collection.find_one({"name": name})


# Update (оновлення)
def update_cat_age(name, new_age):
    collection.update_one({"name": name}, {"$set": {"age": new_age}})


def add_cat_feature(name, new_feature):
    collection.update_one({"name": name}, {"$push": {"features": new_feature}})


# Delete (видалення)
def delete_cat_by_name(name):
    collection.delete_one({"name": name})


def delete_all_cats():
    collection.delete_many({})


if __name__ == "__main__":
    # Приклад використання функцій
    create_cat("Barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    create_cat('Lama', 2, ['ходить в лоток', 'не дає себе гладити', 'сірий'])
    create_cat('Liza', 4, ['ходить в лоток', 'дає себе гладити', 'білий'])
    create_cat('Boris', 12, ['ходить в лоток', 'не дає себе гладити', 'сірий'])
    create_cat('Murzik', 1, ['ходить в лоток', 'дає себе гладити', 'чорний'])
 

    print(get_all_cats())

    print(get_cat_by_name("Barsik"))

    update_cat_age("Barsik", 4)
    add_cat_feature("Barsik", "добрий")
    print(get_cat_by_name("Barsik"))

    delete_cat_by_name("Barsik")
    print(get_all_cats())

    delete_all_cats()
    print(get_all_cats())
