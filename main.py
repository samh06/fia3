import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from datastore import DataStore
from Ui_Generated import Ui_MainWindow


class MainWindow():
    def __init__(self):
        self.data_store = DataStore()
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.home_button.pressed.connect(
            lambda *args, b=self.ui.home_button: self.menu_select(b))

        self.pg2_combobox()

    def pg2_combobox(self):
        # Disconnect the signal temporarily
        self.ui.pg2_combo.currentIndexChanged.disconnect(self.pg2_combobox)

        try:
            self.display_patient(self.data_store.retrieve_patient(0))
        except TypeError:
            # This occurs because it isn't connected on the first run, not something to worry about
            pass

        patients = self.data_store.retrieve_patients()
        current_text = self.ui.pg2_combo.currentText()

        # Block signals during the update process
        self.ui.pg2_combo.blockSignals(True)

        self.ui.pg2_combo.clear()

        # Construct a list of patient items
        patient_items = [
            f"[{patient[0]}] {patient[1]}" for patient in patients]

        # Add the items to the combo box all at once
        self.ui.pg2_combo.addItems(patient_items)

        # Set the previously selected item if it still exists in the new items
        index = self.ui.pg2_combo.findText(current_text)
        if index != -1:
            self.ui.pg2_combo.setCurrentIndex(index)
            self.display_patient(
                self.data_store.retrieve_patient(current_text))
        else:
            self.ui.pg2_combo.setCurrentIndex(0)

        # Re-enable the signal
        self.ui.pg2_combo.blockSignals(False)

        self.ui.pg2_combo.currentIndexChanged.connect(self.pg2_combobox)

    def menu_select(self, button: QPushButton):
        self.ui.stackedWidget.setCurrentWidget(getattr(
            self.ui, str(button.property(button.dynamicPropertyNames()[
                0].data().decode("utf-8")))))

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
