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
        patient_holder = []
        for id in self.cursor.fetchall():
            self.cursor.execute(f'select * from patient WHERE "id" = ?', id)
            patient_holder.append(self.cursor.fetchall()[0])
        return patient_holder

    def retrieve_patient(self, index: str):
        patients = self.retrieve_patients()
        id: int
        start_index = index.find("[")
        end_index = index.find("]")

        # Extract the number substring
        id = int(index[start_index+1:end_index])
        for patient in patients:
            if id == patient[0]:
                return patient
        return None
