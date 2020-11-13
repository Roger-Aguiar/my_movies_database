""" 
Name:         Roger Silva Santos Aguiar
Function:     This module implements all the database operations for actors table
Initial date: November 12, 2020
Last update:  November 12, 2020 
"""

import database_config

class ActorsTable():
    def __init__(self):
        self.mydb = database_config.DatabaseConnection.my_connection()
        self.database = self.mydb.cursor()
    
    def insert_row(self, sql, values):
        self.database.execute(sql, values)
        self.mydb.commit()

    def delete_row(self):
        pass

    def update_row(self):
        pass