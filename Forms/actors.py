""" 
Name:         Roger Silva Santos Aguiar
Function:     This class creates a form for actors table
Initial date: November 10, 2020
Last update:  November 11, 2020 
"""

from tkinter import *

class ActorsForm():
    def __init__(self, actors_table):        
        self.actors_table = self.create_actors_form(actors_table)
        self.create_controls()
        self.put_controls_on_screen()

    def create_actors_form(self, actors_table):
        actors_table.title("Actors")
        actors_table.geometry("550x380")
        actors_table.resizable(0, 0)
        return actors_table
        
    def create_controls(self):
        self.create_labels()
        self.create_text_boxes()
        self.create_buttons()

    def create_buttons(self):
        self.add_actor = Button(self.actors_table, text = "Add actor", width = 10, command = self.add_actor_click)
        self.register = Button(self.actors_table, text = "Register", width = 10)
        self.update = Button(self.actors_table, text = "Update", width = 10)
        self.delete = Button(self.actors_table, text = "Delete", width = 10)
        self.previous = Button(self.actors_table, text = "Previous", width = 27)
        self.next = Button(self.actors_table, text = "Next", width = 27)
        self.close = Button(self.actors_table, text = "Close", width = 62)

    def create_labels(self):
        self.id_actor = Label(self.actors_table, text = "Id actor: ")
        self.actor = Label(self.actors_table, text = "Actor: ")
        self.imdb_link = Label(self.actors_table, text = "Imdb link: ")
        self.credits = Label(self.actors_table, text = "Credits: ")
        self.register_date = Label(self.actors_table, text = "Register date: ")
        self.last_update = Label(self.actors_table, text = "Last update: ")        

    def create_text_boxes(self):
        self.id_actor_entry = Entry(self.actors_table, width = 49)
        self.actor_entry = Entry(self.actors_table, width = 49)
        self.imdb_link_entry = Entry(self.actors_table, width = 49)
        self.credits_entry = Entry(self.actors_table, width = 49)
        self.register_date_entry = Entry(self.actors_table, width = 49)
        self.last_update_entry = Entry(self.actors_table, width = 49)
        
    def put_controls_on_screen(self):
        self.put_labels_on_screen()
        self.put_text_boxes_on_screen()
        self.put_buttons_on_screen()
   
    def put_buttons_on_screen(self):
        self.add_actor.grid(row = 6, column = 0, padx = 15)
        self.register.grid(row = 6, column = 1, padx = 15)
        self.update.grid(row = 6, column = 2, padx = 15)
        self.delete.grid(row = 6, column = 3, padx = 15)
        self.previous.grid(row = 7, column = 0, columnspan = 2, pady = 10)
        self.next.grid(row = 7, column = 2, columnspan = 2, pady = 10)
        self.close.grid(row = 8, column = 0, columnspan = 4)

    def put_labels_on_screen(self):
        self.id_actor.grid(row = 0, column = 0, padx = 20, pady = 10, sticky = W)
        self.actor.grid(row = 1, column = 0, padx = 20, pady = 10, sticky = W)
        self.imdb_link.grid(row = 2, column = 0, padx = 20, pady = 10, sticky = W)
        self.credits.grid(row = 3, column = 0, padx = 20, pady = 10, sticky = W)
        self.register_date.grid(row = 4, column = 0, padx = 20, pady = 10, sticky = W)
        self.last_update.grid(row = 5, column = 0, padx = 20, pady = 10, sticky = W)

    def put_text_boxes_on_screen(self):
        self.id_actor_entry.grid(row = 0, column = 1, padx = 0, pady = 10, columnspan = 3, sticky = W)
        self.actor_entry.grid(row = 1, column = 1, padx = 0, pady = 10, columnspan = 3, sticky = W)
        self.imdb_link_entry.grid(row = 2, column = 1, padx = 0, pady = 10, columnspan = 3, sticky = W)
        self.credits_entry.grid(row = 3, column = 1, padx = 0, pady = 10, columnspan = 3, sticky = W)
        self.register_date_entry.grid(row = 4, column = 1, padx = 0, pady = 10, columnspan = 3, sticky = W)
        self.last_update_entry.grid(row = 5, column = 1, padx = 0, pady = 10, columnspan = 3, sticky = W)

    # Events
    def add_actor_click(self):
        self.id_actor_entry.delete(0, END)
        self.actor_entry.delete(0, END)
        self.imdb_link_entry.delete(0, END)
        self.credits_entry.delete(0, END)
        self.register_date_entry.delete(0, END)
        self.last_update_entry.delete(0, END)
        self.actor_entry.focus()

actors_table = Tk()
ActorsForm(actors_table)
actors_table.mainloop()