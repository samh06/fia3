import sys
from datetime import date
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QCoreApplication

from datastore import DataStore
from Ui_Generated import Ui_MainWindow


class MainWindow():
    def __init__(self):
        self.data_store = DataStore()
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.home_button.pressed.connect(self.moved_page)

        self.pg2_combobox()

    def pg2_combobox(self):
        try:
            self.ui.pg2_combo.currentIndexChanged.disconnect(
                self.pg2_combobox)  # Disconnect the signal temporarily
        except TypeError:
            # This occurs cause it isnt connected on first run, not something to worry about
            self.display_patient(self.data_store.retrieve_patient(0))

        patients = self.data_store.retrieve_patients()

        # Store the currently selected item
        current_text = self.ui.pg2_combo.currentText()

        self.ui.pg2_combo.clear()

        for patient in patients:
            self.ui.pg2_combo.addItem(f"[{patient[0]}] {patient[1]}")

        # Set the previously selected item if it still exists in the new items
        index = self.ui.pg2_combo.findText(current_text)
        if index != -1:
            self.ui.pg2_combo.setCurrentIndex(index)
            self.display_patient(self.data_store.retrieve_patient(
                self.ui.pg2_combo.currentText()))
        else:
            self.ui.pg2_combo.setCurrentIndex(0)

        self.ui.pg2_combo.currentIndexChanged.connect(self.pg2_combobox)

    def moved_page(self):
        match self.ui.stackedWidget.currentWidget():
            case self.ui.page:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
                self.ui.pg2_combo.addItem("Items")
                self.ui.pg2_combo.addItem("Items2")

    def display_patient(self, patient):
        if not patient == None:
            self.ui.pg2_name_edit.setText(patient[1])
            self.ui.pg2_dob_edit.setText(patient[2])
            self.ui.pg2_add_edit.setText(patient[3])
            self.ui.pg2_post_edit.setText(patient[4])
            self.ui.pg2_hei_edit.setText(str(patient[5]))
            self.ui.pg2_wei_edit.setText(str(patient[6]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.main_win.show()
    sys.exit(app.exec_())
