import sqlite3
import random
from random_word import RandomWords
from string import ascii_letters


class DataStore():
    def __init__(self):
        self.patients = {}
        try:
            self.sqliteConnection = sqlite3.connect('fia3.db')
            cursor = self.sqliteConnection.cursor()
            print("Database created and Successfully Connected to SQLite")

            sqlite_select_Query = "select * from type"
            cursor.execute(sqlite_select_Query)
            record = cursor.fetchall()
            print("SQLite Database Version is: ", record)
            cursor.close()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)

        self.retrieve_patients()

    def retrieve_patients(self):
        cursor = self.sqliteConnection.cursor()
        cursor.execute("select id from patient")

        for id in cursor.fetchall():
            print(f"id: {id[0]}")

            cursor.execute(f'select * from patient WHERE "id" = ?', id)
            for person in cursor.fetchall():
                self.patients[person[0]] = {
                    'name': person[1], 'dob': person[2], 'add': person[3], 'hei': person[4], 'wei': person[5]}
        print(self.patients)


class Patient():
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
