import pymongo
from bson import ObjectId


class BaseDb:
    def __init__(self, database, collection):
        self.connection = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = self.connection[database]
        self.collection = self.database[collection]

    def insert_many_values(self, new_tuple: tuple):
        """
            A method to insert values in collection.
                list should be filled with dicts, with such format {'name': new_name, 'filling: new_filling, 'price':
            price}
        """
        self.collection.insert_many([{'pie_name': insert_i[0], 'filling': insert_i[1], 'price': insert_i[2]}
                                     for insert_i in new_tuple])

    def find_value(self, filter_db=None):
        """
            A method to find value in collection.
        """
        return self.collection.find_one(filter=filter_db)

    def find_all_values(self):
        """
            A method to find all values in collection.
        """
        return [x for x in self.collection.find()]

    def update_one(self, subject: dict, values: dict):
        """
            A method to update one value in collection.
        """
        self.collection.update_one(subject, {"$set": values})

    def delete_item_by_id(self, del_id: str):
        """
            A method to delete one value in collection by id.
        """
        if not isinstance(del_id, ObjectId):
            del_id = ObjectId(del_id)
        return self.collection.delete_one({'_id': del_id})

    def delete_all_objects(self):
        """
            A method to delete all the values in collection.
        """
        return self.collection.delete_many({})
