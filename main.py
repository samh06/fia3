import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

from datastore import DataStore
from Ui_Generated import Ui_MainWindow


class MainWindow():
    def __init__(self):
        self.data_store = DataStore()
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.menu_select(self.ui.home_title_button)

        self.ui.patient_1_combo_autofill.currentIndexChanged.connect(
            self.patient_1_combobox)
        self.ui.comboBox.currentIndexChanged.connect(
            self.patient_2_combobox)
        self.ui.types_1_combo_autofill.currentIndexChanged.connect(
            self.types_1_combobox)
        self.ui.types_2_code_combobox.currentIndexChanged.connect(
            self.types_2_combobox)

        self.ui.types_1_insert_radio.clicked.connect(
            self.types_1_radio_clicked)
        self.ui.types_1_remove_radio.clicked.connect(
            self.types_1_radio_clicked)
        self.ui.types_1_update_radio.clicked.connect(
            self.types_1_radio_clicked)

        self.ui.patient_1_insert_radio.clicked.connect(
            self.patient_1_radio_clicked)
        self.ui.patient_1_remove_radio.clicked.connect(
            self.patient_1_radio_clicked)
        self.ui.patient_1_update_radio.clicked.connect(
            self.patient_1_radio_clicked)

        self.ui.patient_1_update_button.pressed.connect(
            self.update_patient_1_data)

        self.connect_menu()
        self.connect_side()

        self.patient_1_radio_clicked()
        self.patient_1_combobox()
        self.patient_2_combobox()
        self.types_1_radio_clicked()
        self.types_1_combobox()
        self.types_2_combobox()

    #############################################
    ########## MENUBAR ##########################
    #############################################

    def connect_menu(self):
        buttons = [self.ui.home_title_button, self.ui.patients_title_button,
                   self.ui.type_title_button, self.ui.taken_title_button]

        for button in buttons:
            button.pressed.connect(lambda *args, b=button: self.menu_select(b))

    def menu_select(self, button: QPushButton):
        pg = str(button.property(
            button.dynamicPropertyNames()[0].data().decode("utf-8")))

        self.ui.sideBar.setCurrentWidget(
            getattr(self.ui, f"{pg.split('_')[0]}_side"))
        self.ui.content.setCurrentWidget(getattr(self.ui, pg))

        self.side_select(getattr(self.ui, f"{pg.split('_')[0]}_sidebar_1"))

    #############################################
    ########## SIDEBAR ##########################
    #############################################

    def connect_side(self):
        buttons = []
        for view in self.ui.sideBar.children():
            if not view == self.ui.home_side:
                for button in view.children():
                    buttons.append(button)

        for button in buttons:
            button.pressed.connect(lambda *args, b=button: self.side_select(b))

    def side_select(self, sender: QPushButton):
        for button in self.ui.sideBar.currentWidget().children():
            button.setEnabled(True)

        sender.setEnabled(False)

        buttonName = sender.objectName().split("_")
        try:
            self.ui.content.setCurrentWidget(
                getattr(self.ui, f"{buttonName[0]}_{buttonName[2]}_content"))
        except AttributeError:
            # This occurs when going to the home screen because it has 1 section, this is fine.
            self.ui.content.setCurrentWidget(self.ui.home_content)

    #############################################
    ########## PATIENT 1 ########################
    #############################################

    def patient_1_radio_clicked(self):
        patient_insert_enabled = self.ui.patient_1_insert_radio.isChecked()
        patient_remove_enabled = self.ui.patient_1_remove_radio.isChecked()

        self.ui.patient_1_combo_autofill.setDisabled(patient_insert_enabled)
        self.ui.patient_1_name_edit.setDisabled(patient_remove_enabled)
        self.ui.patient_1_studnum_edit.setDisabled(patient_remove_enabled)
        self.ui.patient_1_DOB_edit.setDisabled(patient_remove_enabled)
        self.ui.patient_1_add_edit.setDisabled(patient_remove_enabled)
        self.ui.patient_1_post_edit.setDisabled(patient_remove_enabled)
        self.ui.patient_1_hei_edit.setDisabled(patient_remove_enabled)
        self.ui.patient_1_wei_edit.setDisabled(patient_remove_enabled)

        self.change_patient_1_edits([], True) if patient_insert_enabled else self.change_patient_1_edits(
            self.data_store.retrieve_patient(self.ui.patient_1_combo_autofill.currentText()))

    def patient_1_combobox(self):
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
            self.change_patient_1_edits(
                self.data_store.retrieve_patient(current_text))
        else:
            if self.ui.content.currentWidget() != self.ui.home_content:
                if self.ui.patient_1_remove_radio.isChecked():
                    self.show_error_popup("Successfully deleted patient")
                else:
                    self.show_error_popup(
                        "Selected value no longer in database, please try again.")
                self.ui.patient_1_combo_autofill.setCurrentIndex(0)

        # Re-enable the signal
        self.ui.patient_1_combo_autofill.blockSignals(False)

    def change_patient_1_edits(self, patient, clear=False):
        if clear:
            patient = ["", "", "", "", "", "", "",]
        self.ui.patient_1_name_edit.setText(patient[1])
        self.ui.patient_1_DOB_edit.setText(patient[2])
        self.ui.patient_1_add_edit.setText(patient[3])
        self.ui.patient_1_post_edit.setText(patient[4])
        self.ui.patient_1_hei_edit.setText(str(patient[5]))
        self.ui.patient_1_wei_edit.setText(str(patient[6]))

    def update_patient_1_data(self):
        patient = [self.ui.patient_1_combo_autofill.currentText(),
                   self.ui.patient_1_name_edit.text(),
                   self.ui.patient_1_DOB_edit.text(),
                   self.ui.patient_1_add_edit.text(),
                   self.ui.patient_1_post_edit.text(),
                   int(self.ui.patient_1_hei_edit.text()),
                   int(self.ui.patient_1_wei_edit.text())]

        radio_button_modes = {
            self.ui.patient_1_insert_radio: "insert",
            self.ui.patient_1_update_radio: "update",
            self.ui.patient_1_remove_radio: "remove"
        }

        # Check which radio button is checked
        for radio_button, mode in radio_button_modes.items():
            if radio_button.isChecked():
                self.data_store.patient_push_to_db(patient=patient, mode=mode)
                self.patient_1_combobox()

    #############################################
    ########## PATIENT 2 ########################
    #############################################

    def patient_2_combobox(self):
        patients = self.data_store.retrieve_patients()
        current_text = self.ui.comboBox.currentText()

        # Block signals during the update process
        self.ui.comboBox.blockSignals(True)

        self.ui.comboBox.clear()

        # Construct a list of patient items
        patient_items = [
            f"[{patient[0]}] {patient[1]}" for patient in patients]

        # Add the items to the combo box all at once
        self.ui.comboBox.addItems(patient_items)

        # Set the previously selected item if it still exists in the new items
        index = self.ui.comboBox.findText(current_text)
        if index != -1:
            self.ui.comboBox.setCurrentIndex(index)
            self.change_patient_2_text(
                self.data_store.retrieve_patient(current_text))
        else:
            if self.ui.content.currentWidget() != self.ui.home_content:
                self.show_error_popup(
                    "Selected value no longer in database, please try again.")
            self.ui.comboBox.setCurrentIndex(0)
            self.change_patient_2_text(self.data_store.retrieve_patient(0))

        # Re-enable the signal
        self.ui.comboBox.blockSignals(False)

    def change_patient_2_text(self, patient):
        self.ui.patients_2_SNO_recieving.setText(patient[1])
        self.ui.patients_2_DOB_title_recieving.setText(patient[2])
        self.ui.patients_2_address_recieving.setText(patient[3])
        self.ui.patients_2_POST_recieving.setText(patient[4])
        self.ui.patients_2_height_recieving.setText(str(patient[5]))
        self.ui.patients_2_weight_recieving.setText(str(patient[6]))

    #############################################
    ########## TAKEN 1 ###########(New App)######
    #############################################

    #############################################
    ########## TAKEN 2 ##########(View App)######
    #############################################

    #############################################
    ########## TAKEN 3 ######(New Test)##########
    #############################################

    #############################################
    ########## TYPES 1 ##########################
    #############################################
    def types_1_radio_clicked(self):
        types_insert_enabled = self.ui.types_1_insert_radio.isChecked()
        types_remove_enabled = self.ui.types_1_remove_radio.isChecked()

        self.ui.types_1_combo_autofill.setDisabled(types_insert_enabled)
        self.ui.types_1_name_edit.setDisabled(types_remove_enabled)
        self.ui.types_1_code_edit.setDisabled(types_remove_enabled)
        self.ui.types_1_description_edit.setDisabled(types_remove_enabled)
        self.ui.types_1_price_edit.setDisabled(types_remove_enabled)

        self.change_types_1_edits([], True) if types_insert_enabled else self.change_types_1_edits(
            self.data_store.retrieve_type(self.ui.types_1_combo_autofill.currentText()))

    def types_1_combobox(self):
        types = self.data_store.retrieve_types()
        current_text = self.ui.types_1_combo_autofill.currentText()

        # Block signals during the update process
        self.ui.types_1_combo_autofill.blockSignals(True)

        self.ui.types_1_combo_autofill.clear()

        # Construct a list of patient items
        patient_items = [
            f"[{type[0]}] {type[1]}" for type in types]

        # Add the items to the combo box all at once
        self.ui.types_1_combo_autofill.addItems(patient_items)

        # Set the previously selected item if it still exists in the new items
        index = self.ui.types_1_combo_autofill.findText(current_text)
        if index != -1:
            self.ui.types_1_combo_autofill.setCurrentIndex(index)
            self.change_types_1_edits(
                self.data_store.retrieve_type(current_text))
        else:
            if self.ui.content.currentWidget() != self.ui.home_content:
                if self.ui.types_1_remove_radio.isChecked():
                    self.show_error_popup("Successfully deleted patient")
                else:
                    self.show_error_popup(
                        "Selected value no longer in database, please try again.")
                self.ui.types_1_combo_autofill.setCurrentIndex(0)

        # Re-enable the signal
        self.ui.types_1_combo_autofill.blockSignals(False)

    def change_types_1_edits(self, patient, clear=False):
        if clear:
            patient = ["", "", "", "", ""]
        self.ui.types_1_name_edit.setText(patient[2])
        self.ui.types_1_code_edit.setText(patient[1])
        self.ui.types_1_description_edit.setPlainText(patient[3])
        self.ui.types_1_price_edit.setText(str(patient[4]))

    def update_types_1_data(self):
        type = [self.ui.patient_1_combo_autofill.currentText(),
                self.ui.types_1_name_edit.text(),
                self.ui.types_1_code_edit.text(),
                self.ui.types_1_description_edit.toPlainText(),
                self.ui.types_1_price_edit.text()]

        radio_button_modes = {
            self.ui.types_1_insert_radio: "insert",
            self.ui.types_1_update_radio: "update",
            self.ui.types_1_remove_radio: "remove"
        }

        # Check which radio button is checked
        for radio_button, mode in radio_button_modes.items():
            if radio_button.isChecked():
                self.data_store.type_push_to_db(patient=type, mode=mode)
                self.types_1_combobox()
    #############################################
    ########## TYPES 2 ##########################
    #############################################

    def types_2_combobox(self):
        tests = self.data_store.retrieve_types()
        current_text = self.ui.types_2_code_combobox.currentText()

        # Block signals during the update process
        self.ui.types_2_code_combobox.blockSignals(True)

        self.ui.types_2_code_combobox.clear()

        # Construct a list of patient items
        test_items = [
            f"[{test[0]}] {test[1]}" for test in tests]

        # Add the items to the combo box all at once
        self.ui.types_2_code_combobox.addItems(test_items)

        # Set the previously selected item if it still exists in the new items
        index = self.ui.types_2_code_combobox.findText(current_text)
        if index != -1:
            self.ui.types_2_code_combobox.setCurrentIndex(index)
            self.change_type_2_text(
                self.data_store.retrieve_type(current_text))
        else:
            if self.ui.content.currentWidget() != self.ui.home_content:
                self.show_error_popup(
                    "Selected value no longer in database, please try again.")
            self.ui.types_2_code_combobox.setCurrentIndex(0)
            self.change_type_2_text(self.data_store.retrieve_type(0))

        # Re-enable the signal
        self.ui.types_2_code_combobox.blockSignals(False)

    def change_type_2_text(self, patient):
        self.ui.types_2_code_label.setText(patient[1])
        self.ui.types_2_name_label.setText(patient[2])
        self.ui.types_2_description_label.setText(patient[3])
        self.ui.types_2_price_label.setText(f"${str(patient[4])}")

    #############################################
    ########## MISC #############################
    #############################################

    @staticmethod
    def show_error_popup(message):
        error_popup = QMessageBox()
        error_popup.setIcon(QMessageBox.Critical)
        error_popup.setWindowTitle("Error")
        error_popup.setText(message)
        error_popup.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.main_win.show()
    sys.exit(app.exec_())
