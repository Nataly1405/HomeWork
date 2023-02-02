from Auto_Lessons.HomeWork.NatalyBondarenko.mongo_db.objects.base_db import BaseDb


class PieShopDb(BaseDb):
    def __init__(self):
        super().__init__("pie", "pie_characteristic")

    def insert_value(self, new_pie_name, new_filling, new_price):
        """
            A method to insert value in collection.
            dict format is {'name': new_name, 'filling': new_filling, 'price': new_price}
        """
        return self.collection.insert_one({'name': new_pie_name, 'filling': new_filling, 'price': new_price})
