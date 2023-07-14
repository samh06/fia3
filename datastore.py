import os
import sqlite3


class DataStore:
    def __init__(self):
        self.db_file = os.path.join(os.getcwd(), "fia3.db")
        self.db = sqlite3.connect(self.db_file)
        self.cursor = self.db.cursor()
        self.retrieve_patients()

    def __del__(self):
        self.db.close()

    def retrieve_patients(self):
        self.cursor.execute("select id from patient")

        for id in self.cursor.fetchall():
            self.cursor.execute(f'select * from patient WHERE "id" = ?', id)
            return self.cursor.fetchall()
