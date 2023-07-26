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
        self.ui.taken_name_combo.currentIndexChanged.connect(
            self.taken_2_combobox_name)
        self.ui.taken_test_combo.currentIndexChanged.connect(
            lambda *args, b=False: self.taken_2_combobox_app(reset=b))

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
        self.taken_2_combobox_name()

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

    def taken_2_combobox_name(self):
        # The 'taken_2_combobox_name' function updates the contents of the 'taken_name_combo'
        # combo box with the list of patients. It also handles setting the current patient
        # if it still exists in the updated combo box items.

        # Retrieve the list of patients from the data store.
        patients = self.data_store.retrieve_patients()

        # Get the currently selected patient name from 'taken_name_combo'.
        current_text_patient = self.ui.taken_name_combo.currentText()

        # Block signals during the update process to prevent unnecessary signals from being emitted.
        self.ui.taken_name_combo.blockSignals(True)

        # Clear the contents of 'taken_name_combo'.
        self.ui.taken_name_combo.clear()

        # Construct a list of formatted patient items in the form "[Patient ID] Patient Name".
        patient_list = [
            f"[{patient[0]}] {patient[1]}" for patient in patients]

        # Add the items to 'taken_name_combo' all at once.
        self.ui.taken_name_combo.addItems(patient_list)

        # Set the previously selected patient if it still exists in the updated combo box items.
        index = self.ui.taken_name_combo.findText(current_text_patient)
        if index != -1:
            # If the previous selection exists in the updated combo box items,
            # set the current index to the previous selection.
            self.ui.taken_name_combo.setCurrentIndex(index)
        else:
            # If the previous selection no longer exists in the updated combo box items,
            # show an error popup if not resetting and set the current index to the first item.
            if self.ui.content.currentWidget() != self.ui.home_content:
                self.show_error_popup(
                    "Selected value no longer in database, please try again.")
            self.ui.taken_name_combo.setCurrentIndex(0)

        # Call 'taken_2_combobox_app' function with 'reset' set to True to update 'taken_test_combo'.
        self.taken_2_combobox_app(reset=True)

        # Re-enable the signal for 'taken_name_combo'.
        self.ui.taken_name_combo.blockSignals(False)

    def taken_2_combobox_app(self, reset=False):
        # The 'taken_2_combobox_app' function updates the contents of the 'taken_test_combo'
        # combo box based on the selected patient from 'taken_name_combo'. It also handles
        # setting the current item if it still exists in the updated combo box items.

        # Retrieve the patient's appointments from the data store based on the selected patient name.
        appointments = self.data_store.retrieve_patient_appointments(
            self.data_store.return_id(self.ui.taken_name_combo.currentText()))

        # Get the currently selected text from 'taken_test_combo'.
        current_text = self.ui.taken_test_combo.currentText()

        # Block signals during the update process to prevent unnecessary signals from being emitted.
        self.ui.taken_test_combo.blockSignals(True)

        # Clear the contents of 'taken_test_combo'.
        self.ui.taken_test_combo.clear()

        # Construct a list of formatted patient items in the form "[Patient ID] Patient Name".
        appointment_list = [
            f"[{patient[0]}] {patient[2]}" for patient in appointments]

        # Add the items to 'taken_test_combo' all at once.
        self.ui.taken_test_combo.addItems(appointment_list)

        # Set the previously selected item if it still exists in the new items.
        index = self.ui.taken_test_combo.findText(current_text)
        if index != -1 and not reset:
            # If the previous selection exists in the updated combo box items and 'reset' is False,
            # set the current index to the previous selection.
            self.ui.taken_test_combo.setCurrentIndex(index)
            app_id = self.data_store.return_id(current_text)
            if app_id == False:
                self.show_error_popup(
                    "There is no tests available for this patient.")
            else:
                # Fetch the details of the selected appointment and associated tests.
                self.change_taken_2_text(
                    self.data_store.retrieve_app(
                        self.ui.taken_name_combo.currentText(), app_id),
                    self.data_store.retrieve_tests(current_text)
                )
        else:
            # If the previous selection no longer exists in the updated combo box items,
            # show an error popup if not resetting and set the current index to the first item.
            if self.ui.content.currentWidget() != self.ui.home_content and not reset:
                self.show_error_popup(
                    "Selected value no longer in database, please try again.")
            self.ui.taken_test_combo.setCurrentIndex(0)

            app_id = self.data_store.return_id(
                self.ui.taken_test_combo.currentText())
            if app_id == False:
                self.show_error_popup(
                    "There is no tests available for this patient.")
            else:

                # Fetch the details of the first appointment and its associated tests.
                self.change_taken_2_text(
                    self.data_store.retrieve_app(
                        self.ui.taken_name_combo.currentText(), app_id),
                    self.data_store.retrieve_tests(
                        self.ui.taken_test_combo.currentText())
                )

        # Re-enable the signal
        self.ui.taken_test_combo.blockSignals(False)

    def change_taken_2_text(self, patient, tests):
        codes = self.data_store.get_(patient[0])
        performed_tests = "Tests:"
        for code in codes:
            performed_tests += f"    {code[0]}"
        self.ui.taken_2_patient_info.setText(
            f"Patient: {self.data_store.retrieve_patient(patient[1])[1]}")
        self.ui.taken_2_code_info.setText(f"Paid: {patient[4]}")
        self.ui.taken_2_date_info.setText(f"Date: {patient[2]}")
        self.ui.taken_2_results_info.setText(f"Results: {patient[3]}")
        self.ui.taken_2_tests_info.setText(performed_tests)

        # self.ui.taken_2_tests_info.setText(f)

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
