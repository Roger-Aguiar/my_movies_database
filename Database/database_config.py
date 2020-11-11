""" 
Name:         Roger Silva Santos Aguiar
Function:     This is the config database file
Initial date: November 11, 2020
Last update:  November 11, 2020 
"""

import psycopg2

class DatabaseConnection:
    @staticmethod
    def my_connection():
        connection = psycopg2.connect\
            (
                user='postgres',
                password='983453069',
                host='localhost',
                port='5432',
                database='my_movies'
            )

        return connection