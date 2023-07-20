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
        self.cursor.execute("select * from patient")
        return self.cursor.fetchall()

    def retrieve_types(self):
        self.cursor.execute("select * from type")
        return self.cursor.fetchall()

    def retrieve_patient(self, index: str | int):
        patients = self.retrieve_patients()
        id: int
        if type(index) == int:
            id = index
        else:
            start_index = index.find("[")
            end_index = index.find("]")

            id = int(index[start_index+1:end_index])
        for patient in patients:
            if id == patient[0]:
                return patient
        return patients[0]

    def retrieve_type(self, index: str | int):
        tests = self.retrieve_types()
        id: int
        if type(index) == int:
            id = index
        else:
            start_index = index.find("[")
            end_index = index.find("]")

            id = int(index[start_index+1:end_index])
        for test in tests:
            if id == test[0]:
                return test
        return tests[0]

    def patient_push_to_db(self, patient: list, mode: str):
        id: int
        if type(patient[0]) == int:
            id = patient[0]
        else:
            start_index = patient[0].find("[")
            end_index = patient[0].find("]")

            id = int(patient[0][start_index+1:end_index])
            print(id)

        if mode == "update":
            self.update_patient(id, patient)
        elif mode == "insert":
            self.insert_patient(patient)
        else:
            self.remove_patient(id)

    def update_patient(self, id, patient):
        self.cursor.execute("""
                    UPDATE Patient
                    SET
                        name = :name,
                        dob = :dob,
                        address = :add,
                        Post = :post,
                        height = :hei,
                        weight = :wei
                    WHERE
                        id = :id;
                                    """, {"id": id, "name": patient[1], "dob": patient[2],
                                          "add": patient[3], "post": patient[4],
                                          "hei": patient[5], "wei": patient[6]})
        self.db.commit()

    def insert_patient(self, patient):
        self.cursor.execute("""
            INSERT INTO patient (name, dob, address, post, height, weight)
            VALUES (:name, :dob, :address, :post, :height, :weight)""",
                            {"name": patient[1], "dob": patient[2],
                             "address": patient[3], "post": patient[4],
                             "height": patient[5], "weight": patient[6]})
        self.db.commit()

    def remove_patient(self, id):
        print(id)
        self.cursor.execute('''DELETE FROM patient
WHERE id = :id;''', {"id": id})
        self.db.commit()
