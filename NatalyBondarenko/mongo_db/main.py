from Auto_Lessons.HomeWork.NatalyBondarenko.mongo_db.objects.pie_shop_db import PieShopDb

pie = PieShopDb()

pie.insert_many_values(
    (["RedBomb", "cherry", 25],
     ["BlackFriday", "Blueberry", 37],
     ["Classic", "Apple", 20],))
print(f'1.\t{pie.find_value()}')
print(f'2.\t{pie.find_all_values()}')
new_pie = pie.insert_value("Yellow_submarine", "Apricot", 25)
print(f'3.\t{pie.find_all_values()}')
pie.update_one({"pie_name": "Classic"}, {"filling": "Chiken&Mushrooms"})
print(f'4.\t{pie.find_all_values()}')
print(pie.find_value(filter_db={"pie_name": "RedBomb"}).get('_id'))
find_id = pie.find_value(filter_db={"pie_name": "RedBomb"}).get('_id')
pie.delete_item_by_id(find_id)
print(f'5.\t{pie.find_all_values()}')
pie.delete_all_objects()
print(f'6.\t{pie.find_all_values()}')
