from Auto_Lessons.HomeWork.NatalyBondarenko.sql_driver.repositories.database_repository import DatabaseRepository
from Auto_Lessons.HomeWork.NatalyBondarenko.sql_driver.repositories.orders_repository import OrdersRepository
from Auto_Lessons.HomeWork.NatalyBondarenko.sql_driver.repositories.products_repository import ProductsRepository
import pytest


def test_drop_table_products(create_connection):
    products_repository = ProductsRepository(create_connection)
    with pytest.raises(Exception) as exc:
        products_repository.drop_table()
        products_repository.get_all()
    assert str(exc.value) == 'UndefinedTable'


def test_create_products_table(create_connection):
    products_repository = ProductsRepository(create_connection)
    products_repository.create_product_table()
    assert type(products_repository.get_all()) is list


def test_create_second_products_table(create_connection):
    products_repository = ProductsRepository(create_connection)
    with pytest.raises(Exception) as exc:
        products_repository.create_product_table()
    assert str(exc.value) == 'DuplicateTable'


def test_insert_values_into_products_table(create_connection):
    products_repository = ProductsRepository(create_connection)
    products = [('apple_pie', 15.80), ('cherry_pie', 28.50), ('cranberry_pie', 19.60), ('eclair', 8.90),
                ('lemon_pie', 20)]
    products_repository.insert_values_into_products(products)
    assert type(products_repository.get_all()) is list


def test_get_all_products(create_connection):
    products_repository = ProductsRepository(create_connection)
    print(products_repository.get_all())
    assert type(products_repository.get_all()) is list


def test_insert_new_product(create_connection):
    products_repository = ProductsRepository(create_connection)
    products_repository.insert_product('cookie', 9)
    values = products_repository.get_all()
    assert (6, 'cookie', 9.0) in values


def test_delete_product_by_price(create_connection, env1):
    products_repository = ProductsRepository(create_connection)
    products_repository.delete_product_by_price(env1.price_to_delete)
    values = products_repository.get_all()
    assert (6, 'cookie', 9.0) not in values


def test_drop_table_orders(create_connection):
    orders_repository = OrdersRepository(create_connection)
    with pytest.raises(Exception) as exc:
        orders_repository.drop_table_orders()
        orders_repository.get_all()
    assert str(exc.value) == 'UndefinedTable'


def test_create_orders_table(create_connection):
    database_repository = DatabaseRepository(create_connection)
    database_repository.create_orders_table()
    assert type(database_repository.get_all_orders()) is list


def test_create_second_orders_table(create_connection):
    database_repository = DatabaseRepository(create_connection)
    with pytest.raises(Exception) as exc:
        database_repository.create_orders_table()
    assert str(exc.value) == "DuplicateTable"


def test_insert_values_into_orders_table(create_connection):
    orders_repository = OrdersRepository(create_connection)
    orders = [(1, 1), (2, 3), (3, 2), (4, 8), (5, 2)]
    orders_repository.insert_values_into_orders(orders)
    assert type(orders_repository.get_all()) is list


def test_get_product_by_name(create_connection):
    products_repository = ProductsRepository(create_connection)
    product_name = products_repository.get_product_by_name('lemon_pie')
    assert product_name == (5, 'lemon_pie', 20.0)
