import psycopg2
from psycopg2 import errors


class BaseRepository:
    def __init__(self, connection):
        self._connection = connection
        self._cursor = self._connection.cursor()
        self._table_name = ''

    def get_all(self):
        try:
            self._cursor.execute(f"select * from {self._table_name};")
            return self._cursor.fetchall()
        except psycopg2.errors.UndefinedTable:
            raise ValueError("UndefinedTable")

    def __del__(self):
        if self._connection:
            if self._cursor:
                self._cursor.close()
            self._connection.close()
