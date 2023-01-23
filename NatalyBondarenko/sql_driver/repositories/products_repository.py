import psycopg2
from psycopg2 import errors

from Auto_Lessons.HomeWork.NatalyBondarenko.sql_driver.repositories.base_repository import BaseRepository


class ProductsRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)
        self._table_name = 'products'

    def get_product_by_name(self, name):
        self._cursor.execute(f"select * from products where products.name = '{name}';")
        return self._cursor.fetchone()

    def insert_product(self, name, price):
        self._cursor.execute(f"insert into products (name, price) values ('{name}', {price});")
        self._connection.commit()

    def delete_product_by_price(self, price):
        self._cursor.execute(f"delete from products where products.price = '{price}';")
        self._connection.commit()

    def create_product_table(self):
        try:
            self._cursor.execute(
                f"create table {self._table_name}(id serial primary key, name varchar(30), price float);")
            self._connection.commit()
        except psycopg2.errors.DuplicateTable:
            raise ValueError("DuplicateTable")

    def drop_table(self):
        try:
            self._cursor.execute(f"drop table {self._table_name} cascade;")
            self._connection.commit()
        except psycopg2.errors.UndefinedTable:
            raise ValueError("UndefinedTable")

    def insert_values_into_products(self, values):
        args = ','.join(self._cursor.mogrify("(%s,%s)", value).decode('utf-8') for value in values)
        self._cursor.execute(f"insert into {self._table_name} (name, price) values" + args)
        self._connection.commit()