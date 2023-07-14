import sqlite3
import random
from random_word import RandomWords
from string import ascii_letters


class DataStore():
    def __init__(self):
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

        self.data_import()

    def data_import(self):
        cursor = self.sqliteConnection.cursor()
        r = RandomWords()
        appointment_cursor = self.sqliteConnection.cursor()
        appointment_cursor.execute("select id from appointment")
        record = appointment_cursor.fetchall()
        appointment_cursor.close()

        # Assuming you have 40 appointments in the "Appointment" table
        for appointment_id in record:
            type_cursor = self.sqliteConnection.cursor()
            type_cursor.execute("select id from type")
            record = type_cursor.fetchall()
            type_cursor.close()
            # Assuming you have 10 types in the "Type" table
            type_id = random.choice(record)

            # Insert the random data into the "AppointmentType" table
            cursor.execute("INSERT INTO AppointmentType (appointment_id, type_id) VALUES (?, ?)",
                           (appointment_id[0], type_id[0]))
            # id_cursor = self.sqliteConnection.cursor().execute("select id from patient")
            # # Assuming 20 patients are already present in the "Patient" table
            # patient_id = random.choice(id_cursor.fetchall())
            # id_cursor.close()
            # date = "20" + str(random.randint(10, 23)) + "-" + str(random.randint(1, 12)
            #                                                       ).zfill(2) + "-" + str(random.randint(1, 28)).zfill(2)
            # # Randomly select positive or negative result
            # result = random.choice(["Positive", "Negative"])
            # # Randomly assign 0 or 1 for paid status
            # paid = random.randint(0, 1)

            # # Insert the random data into the "Appointment" table
            # cursor.execute("INSERT INTO Appointment (patientid, date, result, paid) VALUES (?, ?, ?, ?)",
            #                (patient_id[0], date, result, paid))

            # code = ''.join(random.choice(ascii_letters).capitalize()
            #                for _ in range(3))
            # name = ''.join(r.get_random_word()
            #                for _ in range(2))
            # desc = ''.join(r.get_random_word()
            #                for _ in range(5))
            # price = random.randint(10, 100)

            # # Insert the random data into the "Type" table
            # cursor.execute("INSERT INTO Type (code, name, desc, price) VALUES (?, ?, ?, ?)",
            #                (code, name, desc, price))

            self.sqliteConnection.commit()
            # name = "Patient " + str(random.randint(1, 100))
            # dob = "19" + str(random.randint(50, 99)) + "-" + str(random.randint(1, 12)
            #                                                      ).zfill(2) + "-" + str(random.randint(1, 28)).zfill(2)
            # address = "Address " + str(random.randint(1, 100))
            # post = "Post " + str(random.randint(1000, 9999))
            # height = random.randint(150, 200)
            # weight = random.randint(50, 100)

            # # Insert the random data into the "Patient" table
            # cursor.execute("INSERT INTO Type (name, dob, address, post, height, weight) VALUES (?, ?, ?, ?, ?, ?)",
            #                (name, dob, address, post, height, weight))
