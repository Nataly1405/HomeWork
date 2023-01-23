import psycopg2

from psycopg2 import errors

from Auto_Lessons.HomeWork.NatalyBondarenko.sql_driver.repositories.base_repository import BaseRepository


class DatabaseRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)
        self._products_table_name = "products"
        self._orders_table_name = "orders"

    def create_orders_table(self):
        try:
            self._cursor.execute(
                f"create table {self._orders_table_name}(id serial primary key, product_id int,quantity int, "
                f"constraint fk_product_id foreign key (product_id) references {self._products_table_name}(id));")
            self._connection.commit()
        except psycopg2.errors.DuplicateTable:
            raise ValueError("DuplicateTable")

    def get_all_orders(self):
        try:
            self._cursor.execute(f'select * from {self._orders_table_name};')
            return self._cursor.fetchall()
        except psycopg2.errors.UndefinedTable:
            raise ValueError("UndefinedTable")
