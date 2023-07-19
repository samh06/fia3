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
        self.connect_bar()

        self.pg2_combobox()

    def connect_bar(self):
        buttons = [self.ui.home_title_button, self.ui.patients_title_button,
                   self.ui.type_title_button, self.ui.taken_title_button,
                   self.ui.taken_sidebar_1, self.ui.taken_sidebar_2,
                   self.ui.patients_sidebar_1, self.ui.patients_sidebar_2,
                   self.ui.types_sidebar_1, self.ui.types_sidebar_2]

        for button in buttons:
            button.pressed.connect(lambda *args, b=button: self.menu_select(b))

    def pg2_combobox(self):
        try:
            self.display_patient(self.data_store.retrieve_patient(0))
        except TypeError:
            # This occurs because it isn't connected on the first run, not something to worry about
            pass

        patients = self.data_store.retrieve_patients()
        current_text = self.ui.patient_1_combo_autofill.currentText()

        # Block signals during the update process
        self.ui.patient_1_combo_autofill.blockSignals(True)

        self.ui.patient_1_combo_autofill.clear()

        # Construct a list of patient items
        patient_items = [
            f"[{patient[0]}] {patient[1]}" for patient in patients]

        # Add the items to the combo box all at once
        self.ui.patient_1_combo_autofill.addItems(patient_items)

        # Set the previously selected item if it still exists in the new items
        index = self.ui.patient_1_combo_autofill.findText(current_text)
        if index != -1:
            self.ui.patient_1_combo_autofill.setCurrentIndex(index)
            self.display_patient(
                self.data_store.retrieve_patient(current_text))
        else:
            self.ui.patient_1_combo_autofill.setCurrentIndex(0)

        # Re-enable the signal
        self.ui.patient_1_combo_autofill.blockSignals(False)

        self.ui.patient_1_combo_autofill.currentIndexChanged.connect(
            self.pg2_combobox)

    def menu_select(self, button: QPushButton):
        self.ui.content.setCurrentWidget(getattr(
            self.ui, str(button.property(button.dynamicPropertyNames()[
                0].data().decode("utf-8")))))

    def display_patient(self, patient):
        if not patient == None:
            self.ui.patient_1_name_edit.setText(patient[1])
            self.ui.patient_1_DOB_edit.setText(patient[2])
            self.ui.patient_1_add_edit.setText(patient[3])
            self.ui.patient_1_post_edit.setText(patient[4])
            self.ui.patient_1_hei_edit.setText(str(patient[5]))
            self.ui.patient_1_wei_edit.setText(str(patient[6]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.main_win.show()
    sys.exit(app.exec_())
