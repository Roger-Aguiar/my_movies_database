""" 
Name:         Roger Silva Santos Aguiar
Function:     This module implements all the functionalities for the actors table
Initial date: November 12, 2020
Last update:  November 12, 2020 
"""

import database_service_for_actors

class Actors():
    database = database_service_for_actors.ActorsTable()

    def insert(self, values):
        sql = "INSERT INTO actors (actor, imdb_link, credits, register_date, last_update) " \
              "VALUES (%s, %s, %s, %s, %s)"
        self.database.insert_row(sql, values)