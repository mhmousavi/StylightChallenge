import mysql
from mysql.connector import Error

from base_exceptions.exceptions import DB_EXCEPTION


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class RepositoryManger(metaclass=SingletonMeta):

    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='stylight_db',
                user='root',
                password=''
            )
        except Error as e:
            raise DB_EXCEPTION("Error while connecting to MySQL" + str(e))
