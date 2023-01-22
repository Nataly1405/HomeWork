import psycopg2
from psycopg2 import errors

from Auto_Lessons.HomeWork.NatalyBondarenko.sql_driver.repositories.base_repository import BaseRepository


class OrdersRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)
        self._table_name = 'orders'

    def insert_values_into_orders(self, values):
        args = ','.join(self._cursor.mogrify("(%s,%s)", value).decode('utf-8') for value in values)
        self._cursor.execute(f"insert into {self._table_name} (product_id, quantity) values" + args)

    def drop_table_orders(self):
        try:
            self._cursor.execute(f"drop table {self._table_name} cascade;")
            self._connection.commit()
        except psycopg2.errors.UndefinedTable:
            raise ValueError("UndefinedTable")
