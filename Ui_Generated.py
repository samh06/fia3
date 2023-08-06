# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Bundaberg_Physio.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1021, 601)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 1021, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(140, 80, 20, 521))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.sideBar = QtWidgets.QStackedWidget(self.centralwidget)
        self.sideBar.setGeometry(QtCore.QRect(0, 90, 141, 511))
        self.sideBar.setObjectName("sideBar")
        self.home_side = QtWidgets.QWidget()
        self.home_side.setObjectName("home_side")
        self.label = QtWidgets.QLabel(self.home_side)
        self.label.setGeometry(QtCore.QRect(10, 120, 111, 71))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.home_sidebar_1 = QtWidgets.QPushButton(self.home_side)
        self.home_sidebar_1.setGeometry(QtCore.QRect(30, 310, 1, 1))
        self.home_sidebar_1.setMaximumSize(QtCore.QSize(1, 1))
        self.home_sidebar_1.setObjectName("home_sidebar_1")
        self.home_sidebar_2 = QtWidgets.QPushButton(self.home_side)
        self.home_sidebar_2.setGeometry(QtCore.QRect(0, 0, 1, 1))
        self.home_sidebar_2.setMaximumSize(QtCore.QSize(1, 1))
        self.home_sidebar_2.setObjectName("home_sidebar_2")
        self.sideBar.addWidget(self.home_side)
        self.patients_side = QtWidgets.QWidget()
        self.patients_side.setObjectName("patients_side")
        self.patients_sidebar_1 = QtWidgets.QPushButton(self.patients_side)
        self.patients_sidebar_1.setGeometry(QtCore.QRect(0, 10, 131, 241))
        self.patients_sidebar_1.setObjectName("patients_sidebar_1")
        self.patients_sidebar_2 = QtWidgets.QPushButton(self.patients_side)
        self.patients_sidebar_2.setGeometry(QtCore.QRect(0, 260, 131, 241))
        self.patients_sidebar_2.setObjectName("patients_sidebar_2")
        self.sideBar.addWidget(self.patients_side)
        self.taken_side = QtWidgets.QWidget()
        self.taken_side.setObjectName("taken_side")
        self.taken_sidebar_1 = QtWidgets.QPushButton(self.taken_side)
        self.taken_sidebar_1.setGeometry(QtCore.QRect(0, 10, 131, 163))
        self.taken_sidebar_1.setObjectName("taken_sidebar_1")
        self.taken_sidebar_2 = QtWidgets.QPushButton(self.taken_side)
        self.taken_sidebar_2.setGeometry(QtCore.QRect(0, 338, 131, 163))
        self.taken_sidebar_2.setObjectName("taken_sidebar_2")
        self.taken_sidebar_5 = QtWidgets.QPushButton(self.taken_side)
        self.taken_sidebar_5.setGeometry(QtCore.QRect(0, 180, 131, 151))
        self.taken_sidebar_5.setObjectName("taken_sidebar_5")
        self.sideBar.addWidget(self.taken_side)
        self.types_side = QtWidgets.QWidget()
        self.types_side.setObjectName("types_side")
        self.types_sidebar_1 = QtWidgets.QPushButton(self.types_side)
        self.types_sidebar_1.setGeometry(QtCore.QRect(0, 10, 131, 241))
        self.types_sidebar_1.setObjectName("types_sidebar_1")
        self.types_sidebar_2 = QtWidgets.QPushButton(self.types_side)
        self.types_sidebar_2.setGeometry(QtCore.QRect(0, 260, 131, 241))
        self.types_sidebar_2.setObjectName("types_sidebar_2")
        self.sideBar.addWidget(self.types_side)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 1011, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.home_title_button = QtWidgets.QPushButton(self.layoutWidget)
        self.home_title_button.setObjectName("home_title_button")
        self.horizontalLayout_2.addWidget(self.home_title_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.patients_title_button = QtWidgets.QPushButton(self.layoutWidget)
        self.patients_title_button.setObjectName("patients_title_button")
        self.horizontalLayout_2.addWidget(self.patients_title_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.taken_title_button = QtWidgets.QPushButton(self.layoutWidget)
        self.taken_title_button.setObjectName("taken_title_button")
        self.horizontalLayout_2.addWidget(self.taken_title_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.type_title_button = QtWidgets.QPushButton(self.layoutWidget)
        self.type_title_button.setObjectName("type_title_button")
        self.horizontalLayout_2.addWidget(self.type_title_button)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.content = QtWidgets.QStackedWidget(self.centralwidget)
        self.content.setGeometry(QtCore.QRect(160, 90, 851, 501))
        self.content.setStyleSheet("")
        self.content.setObjectName("content")
        self.home_content = QtWidgets.QWidget()
        self.home_content.setObjectName("home_content")
        self.home_content_title = QtWidgets.QLabel(self.home_content)
        self.home_content_title.setGeometry(QtCore.QRect(10, -10, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.home_content_title.setFont(font)
        self.home_content_title.setObjectName("home_content_title")
        self.home_content_line = QtWidgets.QFrame(self.home_content)
        self.home_content_line.setGeometry(QtCore.QRect(-20, 40, 891, 20))
        self.home_content_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.home_content_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.home_content_line.setObjectName("home_content_line")
        self.content.addWidget(self.home_content)
        self.patients_1_content = QtWidgets.QWidget()
        self.patients_1_content.setObjectName("patients_1_content")
        self.patient_1_content_title = QtWidgets.QLabel(self.patients_1_content)
        self.patient_1_content_title.setGeometry(QtCore.QRect(10, -10, 561, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.patient_1_content_title.setFont(font)
        self.patient_1_content_title.setObjectName("patient_1_content_title")
        self.patient_1_content_line = QtWidgets.QFrame(self.patients_1_content)
        self.patient_1_content_line.setGeometry(QtCore.QRect(-20, 40, 891, 20))
        self.patient_1_content_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.patient_1_content_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.patient_1_content_line.setObjectName("patient_1_content_line")
        self.patient_1_studnum_edit = QtWidgets.QLineEdit(self.patients_1_content)
        self.patient_1_studnum_edit.setGeometry(QtCore.QRect(60, 110, 113, 20))
        self.patient_1_studnum_edit.setObjectName("patient_1_studnum_edit")
        self.patient_1_DOB_edit = QtWidgets.QLineEdit(self.patients_1_content)
        self.patient_1_DOB_edit.setGeometry(QtCore.QRect(50, 150, 113, 20))
        self.patient_1_DOB_edit.setObjectName("patient_1_DOB_edit")
        self.patient_1_post_edit = QtWidgets.QLineEdit(self.patients_1_content)
        self.patient_1_post_edit.setGeometry(QtCore.QRect(50, 250, 113, 20))
        self.patient_1_post_edit.setObjectName("patient_1_post_edit")
        self.patient_1_combo_autofill = QtWidgets.QComboBox(self.patients_1_content)
        self.patient_1_combo_autofill.setGeometry(QtCore.QRect(488, 150, 231, 22))
        self.patient_1_combo_autofill.setObjectName("patient_1_combo_autofill")
        self.patient_1_update_button = QtWidgets.QPushButton(self.patients_1_content)
        self.patient_1_update_button.setGeometry(QtCore.QRect(390, 250, 75, 23))
        self.patient_1_update_button.setObjectName("patient_1_update_button")
        self.layoutWidget1 = QtWidgets.QWidget(self.patients_1_content)
        self.layoutWidget1.setGeometry(QtCore.QRect(460, 90, 260, 19))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.patient_1_insert_radio = QtWidgets.QRadioButton(self.layoutWidget1)
        self.patient_1_insert_radio.setChecked(True)
        self.patient_1_insert_radio.setObjectName("patient_1_insert_radio")
        self.horizontalLayout.addWidget(self.patient_1_insert_radio)
        self.patient_1_update_radio = QtWidgets.QRadioButton(self.layoutWidget1)
        self.patient_1_update_radio.setObjectName("patient_1_update_radio")
        self.horizontalLayout.addWidget(self.patient_1_update_radio)
        self.patient_1_remove_radio = QtWidgets.QRadioButton(self.layoutWidget1)
        self.patient_1_remove_radio.setObjectName("patient_1_remove_radio")
        self.horizontalLayout.addWidget(self.patient_1_remove_radio)
        self.patient_1_hei_edit = QtWidgets.QLineEdit(self.patients_1_content)
        self.patient_1_hei_edit.setGeometry(QtCore.QRect(60, 290, 113, 20))
        self.patient_1_hei_edit.setObjectName("patient_1_hei_edit")
        self.patient_1_add_edit = QtWidgets.QLineEdit(self.patients_1_content)
        self.patient_1_add_edit.setGeometry(QtCore.QRect(50, 200, 341, 20))
        self.patient_1_add_edit.setObjectName("patient_1_add_edit")
        self.patient_1_wei_edit = QtWidgets.QLineEdit(self.patients_1_content)
        self.patient_1_wei_edit.setGeometry(QtCore.QRect(70, 330, 113, 20))
        self.patient_1_wei_edit.setObjectName("patient_1_wei_edit")
        self.patient_1_name_edit = QtWidgets.QLineEdit(self.patients_1_content)
        self.patient_1_name_edit.setGeometry(QtCore.QRect(60, 80, 113, 20))
        self.patient_1_name_edit.setObjectName("patient_1_name_edit")
        self.content.addWidget(self.patients_1_content)
        self.patients_2_content = QtWidgets.QWidget()
        self.patients_2_content.setObjectName("patients_2_content")
        self.patient_2_content_title = QtWidgets.QLabel(self.patients_2_content)
        self.patient_2_content_title.setGeometry(QtCore.QRect(10, -10, 561, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.patient_2_content_title.setFont(font)
        self.patient_2_content_title.setObjectName("patient_2_content_title")
        self.patient_2_content_line = QtWidgets.QFrame(self.patients_2_content)
        self.patient_2_content_line.setGeometry(QtCore.QRect(-20, 40, 891, 20))
        self.patient_2_content_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.patient_2_content_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.patient_2_content_line.setObjectName("patient_2_content_line")
        self.comboBox = QtWidgets.QComboBox(self.patients_2_content)
        self.comboBox.setGeometry(QtCore.QRect(640, 100, 151, 22))
        self.comboBox.setObjectName("comboBox")
        self.patients_2_SNO_title = QtWidgets.QLabel(self.patients_2_content)
        self.patients_2_SNO_title.setGeometry(QtCore.QRect(56, 170, 51, 20))
        self.patients_2_SNO_title.setObjectName("patients_2_SNO_title")
        self.patients_2_DOB_title = QtWidgets.QLabel(self.patients_2_content)
        self.patients_2_DOB_title.setGeometry(QtCore.QRect(60, 200, 47, 13))
        self.patients_2_DOB_title.setObjectName("patients_2_DOB_title")
        self.patients_2_address_title = QtWidgets.QLabel(self.patients_2_content)
        self.patients_2_address_title.setGeometry(QtCore.QRect(60, 230, 47, 13))
        self.patients_2_address_title.setObjectName("patients_2_address_title")
        self.patients_2_POST_title = QtWidgets.QLabel(self.patients_2_content)
        self.patients_2_POST_title.setGeometry(QtCore.QRect(60, 260, 47, 13))
        self.patients_2_POST_title.setObjectName("patients_2_POST_title")
        self.patients_2_height_title = QtWidgets.QLabel(self.patients_2_content)
        self.patients_2_height_title.setGeometry(QtCore.QRect(60, 290, 47, 13))
        self.patients_2_height_title.setObjectName("patients_2_height_title")
        self.patients_2_weight_title = QtWidgets.QLabel(self.patients_2_content)
        self.patients_2_weight_title.setGeometry(QtCore.QRect(60, 320, 47, 13))
        self.patients_2_weight_title.setObjectName("patients_2_weight_title")
        self.patients_2_SNO_recieving = QtWidgets.QLabel(self.patients_2_content)
        self.patients_2_SNO_recieving.setGeometry(QtCore.QRect(150, 180, 351, 16))
        self.patients_2_SNO_recieving.setText("")
        self.patients_2_SNO_recieving.setObjectName("patients_2_SNO_recieving")
        self.patients_2_DOB_title_recieving = QtWidgets.QLabel(self.patients_2_content)
        self.patients_2_DOB_title_recieving.setGeometry(QtCore.QRect(150, 210, 381, 16))
        self.patients_2_DOB_title_recieving.setText("")
        self.patients_2_DOB_title_recieving.setObjectName("patients_2_DOB_title_recieving")
        self.patients_2_POST_recieving = QtWidgets.QLabel(self.patients_2_content)
        self.patients_2_POST_recieving.setGeometry(QtCore.QRect(150, 260, 471, 16))
        self.patients_2_POST_recieving.setText("")
        self.patients_2_POST_recieving.setObjectName("patients_2_POST_recieving")
        self.patients_2_address_recieving = QtWidgets.QLabel(self.patients_2_content)
        self.patients_2_address_recieving.setGeometry(QtCore.QRect(150, 230, 391, 16))
        self.patients_2_address_recieving.setText("")
        self.patients_2_address_recieving.setObjectName("patients_2_address_recieving")
        self.patients_2_height_recieving = QtWidgets.QLabel(self.patients_2_content)
        self.patients_2_height_recieving.setGeometry(QtCore.QRect(150, 290, 541, 16))
        self.patients_2_height_recieving.setText("")
        self.patients_2_height_recieving.setObjectName("patients_2_height_recieving")
        self.patients_2_weight_recieving = QtWidgets.QLabel(self.patients_2_content)
        self.patients_2_weight_recieving.setGeometry(QtCore.QRect(140, 320, 601, 16))
        self.patients_2_weight_recieving.setText("")
        self.patients_2_weight_recieving.setObjectName("patients_2_weight_recieving")
        self.content.addWidget(self.patients_2_content)
        self.taken_1_content = QtWidgets.QWidget()
        self.taken_1_content.setObjectName("taken_1_content")
        self.taken_1_content_line = QtWidgets.QFrame(self.taken_1_content)
        self.taken_1_content_line.setGeometry(QtCore.QRect(-20, 40, 891, 20))
        self.taken_1_content_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.taken_1_content_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.taken_1_content_line.setObjectName("taken_1_content_line")
        self.taken_1_name_combo = QtWidgets.QComboBox(self.taken_1_content)
        self.taken_1_name_combo.setGeometry(QtCore.QRect(500, 120, 191, 22))
        self.taken_1_name_combo.setObjectName("taken_1_name_combo")
        self.taken_1_patient_info = QtWidgets.QLabel(self.taken_1_content)
        self.taken_1_patient_info.setGeometry(QtCore.QRect(450, 120, 161, 16))
        self.taken_1_patient_info.setObjectName("taken_1_patient_info")
        self.taken_1_code_info = QtWidgets.QLabel(self.taken_1_content)
        self.taken_1_code_info.setGeometry(QtCore.QRect(60, 150, 31, 16))
        self.taken_1_code_info.setObjectName("taken_1_code_info")
        self.taken_1_date_info = QtWidgets.QLabel(self.taken_1_content)
        self.taken_1_date_info.setGeometry(QtCore.QRect(60, 180, 141, 16))
        self.taken_1_date_info.setObjectName("taken_1_date_info")
        self.taken_1_results_info = QtWidgets.QLabel(self.taken_1_content)
        self.taken_1_results_info.setGeometry(QtCore.QRect(70, 220, 141, 16))
        self.taken_1_results_info.setObjectName("taken_1_results_info")
        self.taken_1_date_edit = QtWidgets.QLineEdit(self.taken_1_content)
        self.taken_1_date_edit.setGeometry(QtCore.QRect(140, 180, 113, 20))
        self.taken_1_date_edit.setObjectName("taken_1_date_edit")
        self.taken_1_results_edit = QtWidgets.QLineEdit(self.taken_1_content)
        self.taken_1_results_edit.setGeometry(QtCore.QRect(140, 220, 113, 20))
        self.taken_1_results_edit.setObjectName("taken_1_results_edit")
        self.pushButton = QtWidgets.QPushButton(self.taken_1_content)
        self.pushButton.setGeometry(QtCore.QRect(180, 290, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.patient_2_content_title_3 = QtWidgets.QLabel(self.taken_1_content)
        self.patient_2_content_title_3.setGeometry(QtCore.QRect(0, -10, 711, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.patient_2_content_title_3.setFont(font)
        self.patient_2_content_title_3.setObjectName("patient_2_content_title_3")
        self.layoutWidget_3 = QtWidgets.QWidget(self.taken_1_content)
        self.layoutWidget_3.setGeometry(QtCore.QRect(420, 80, 260, 19))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.taken_1_insert_radio = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.taken_1_insert_radio.setChecked(True)
        self.taken_1_insert_radio.setObjectName("taken_1_insert_radio")
        self.horizontalLayout_4.addWidget(self.taken_1_insert_radio)
        self.taken_1_update_radio = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.taken_1_update_radio.setObjectName("taken_1_update_radio")
        self.horizontalLayout_4.addWidget(self.taken_1_update_radio)
        self.taken_1_remove_radio = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.taken_1_remove_radio.setObjectName("taken_1_remove_radio")
        self.horizontalLayout_4.addWidget(self.taken_1_remove_radio)
        self.taken_1_paid_checkBox = QtWidgets.QCheckBox(self.taken_1_content)
        self.taken_1_paid_checkBox.setGeometry(QtCore.QRect(140, 150, 70, 17))
        self.taken_1_paid_checkBox.setText("")
        self.taken_1_paid_checkBox.setObjectName("taken_1_paid_checkBox")
        self.taken_1_combo_autofill = QtWidgets.QComboBox(self.taken_1_content)
        self.taken_1_combo_autofill.setGeometry(QtCore.QRect(480, 180, 191, 22))
        self.taken_1_combo_autofill.setObjectName("taken_1_combo_autofill")
        self.content.addWidget(self.taken_1_content)
        self.taken_2_content = QtWidgets.QWidget()
        self.taken_2_content.setObjectName("taken_2_content")
        self.taken_2_content_title = QtWidgets.QLabel(self.taken_2_content)
        self.taken_2_content_title.setGeometry(QtCore.QRect(10, -10, 561, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.taken_2_content_title.setFont(font)
        self.taken_2_content_title.setObjectName("taken_2_content_title")
        self.taken_2_content_line = QtWidgets.QFrame(self.taken_2_content)
        self.taken_2_content_line.setGeometry(QtCore.QRect(-20, 40, 891, 20))
        self.taken_2_content_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.taken_2_content_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.taken_2_content_line.setObjectName("taken_2_content_line")
        self.taken_name_combo = QtWidgets.QComboBox(self.taken_2_content)
        self.taken_name_combo.setGeometry(QtCore.QRect(640, 130, 191, 22))
        self.taken_name_combo.setObjectName("taken_name_combo")
        self.taken_test_combo = QtWidgets.QComboBox(self.taken_2_content)
        self.taken_test_combo.setGeometry(QtCore.QRect(640, 200, 201, 22))
        self.taken_test_combo.setObjectName("taken_test_combo")
        self.taken_2_patient_info = QtWidgets.QLabel(self.taken_2_content)
        self.taken_2_patient_info.setGeometry(QtCore.QRect(70, 110, 161, 16))
        self.taken_2_patient_info.setObjectName("taken_2_patient_info")
        self.taken_2_code_info = QtWidgets.QLabel(self.taken_2_content)
        self.taken_2_code_info.setGeometry(QtCore.QRect(60, 150, 141, 16))
        self.taken_2_code_info.setObjectName("taken_2_code_info")
        self.taken_2_date_info = QtWidgets.QLabel(self.taken_2_content)
        self.taken_2_date_info.setGeometry(QtCore.QRect(60, 170, 141, 16))
        self.taken_2_date_info.setObjectName("taken_2_date_info")
        self.taken_2_results_info = QtWidgets.QLabel(self.taken_2_content)
        self.taken_2_results_info.setGeometry(QtCore.QRect(70, 200, 141, 16))
        self.taken_2_results_info.setObjectName("taken_2_results_info")
        self.taken_2_tests_info = QtWidgets.QLabel(self.taken_2_content)
        self.taken_2_tests_info.setGeometry(QtCore.QRect(60, 240, 141, 16))
        self.taken_2_tests_info.setObjectName("taken_2_tests_info")
        self.content.addWidget(self.taken_2_content)
        self.taken_5_content = QtWidgets.QWidget()
        self.taken_5_content.setObjectName("taken_5_content")
        self.label_3 = QtWidgets.QLabel(self.taken_5_content)
        self.label_3.setGeometry(QtCore.QRect(270, 100, 47, 13))
        self.label_3.setObjectName("label_3")
        self.taken_3_name_combo = QtWidgets.QComboBox(self.taken_5_content)
        self.taken_3_name_combo.setGeometry(QtCore.QRect(440, 180, 191, 22))
        self.taken_3_name_combo.setObjectName("taken_3_name_combo")
        self.taken_3_test_combo = QtWidgets.QComboBox(self.taken_5_content)
        self.taken_3_test_combo.setGeometry(QtCore.QRect(440, 250, 201, 22))
        self.taken_3_test_combo.setObjectName("taken_3_test_combo")
        self.layoutWidget_2 = QtWidgets.QWidget(self.taken_5_content)
        self.layoutWidget_2.setGeometry(QtCore.QRect(450, 100, 260, 19))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.taken_3_insert_radio = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.taken_3_insert_radio.setChecked(True)
        self.taken_3_insert_radio.setObjectName("taken_3_insert_radio")
        self.horizontalLayout_3.addWidget(self.taken_3_insert_radio)
        self.taken_3_remove_radio = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.taken_3_remove_radio.setObjectName("taken_3_remove_radio")
        self.horizontalLayout_3.addWidget(self.taken_3_remove_radio)
        self.taken_3_type_combo = QtWidgets.QComboBox(self.taken_5_content)
        self.taken_3_type_combo.setGeometry(QtCore.QRect(440, 310, 201, 22))
        self.taken_3_type_combo.setObjectName("taken_3_type_combo")
        self.taken_3_update_button = QtWidgets.QPushButton(self.taken_5_content)
        self.taken_3_update_button.setGeometry(QtCore.QRect(280, 290, 75, 23))
        self.taken_3_update_button.setObjectName("taken_3_update_button")
        self.content.addWidget(self.taken_5_content)
        self.types_1_content = QtWidgets.QWidget()
        self.types_1_content.setObjectName("types_1_content")
        self.types_1_content_title = QtWidgets.QLabel(self.types_1_content)
        self.types_1_content_title.setGeometry(QtCore.QRect(10, -10, 561, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.types_1_content_title.setFont(font)
        self.types_1_content_title.setObjectName("types_1_content_title")
        self.types_1_content_line = QtWidgets.QFrame(self.types_1_content)
        self.types_1_content_line.setGeometry(QtCore.QRect(-20, 40, 891, 20))
        self.types_1_content_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.types_1_content_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.types_1_content_line.setObjectName("types_1_content_line")
        self.types_1_code_edit = QtWidgets.QLineEdit(self.types_1_content)
        self.types_1_code_edit.setGeometry(QtCore.QRect(60, 110, 113, 20))
        self.types_1_code_edit.setObjectName("types_1_code_edit")
        self.types_1_name_edit = QtWidgets.QLineEdit(self.types_1_content)
        self.types_1_name_edit.setGeometry(QtCore.QRect(50, 150, 113, 20))
        self.types_1_name_edit.setObjectName("types_1_name_edit")
        self.types_1_price_edit = QtWidgets.QLineEdit(self.types_1_content)
        self.types_1_price_edit.setGeometry(QtCore.QRect(50, 250, 113, 20))
        self.types_1_price_edit.setObjectName("types_1_price_edit")
        self.types_1_combo_autofill = QtWidgets.QComboBox(self.types_1_content)
        self.types_1_combo_autofill.setGeometry(QtCore.QRect(488, 150, 231, 22))
        self.types_1_combo_autofill.setObjectName("types_1_combo_autofill")
        self.types_1_update_button = QtWidgets.QPushButton(self.types_1_content)
        self.types_1_update_button.setGeometry(QtCore.QRect(390, 250, 75, 23))
        self.types_1_update_button.setObjectName("types_1_update_button")
        self.types_1_description_edit = QtWidgets.QPlainTextEdit(self.types_1_content)
        self.types_1_description_edit.setGeometry(QtCore.QRect(60, 190, 301, 51))
        self.types_1_description_edit.setObjectName("types_1_description_edit")
        self.layoutWidget2 = QtWidgets.QWidget(self.types_1_content)
        self.layoutWidget2.setGeometry(QtCore.QRect(460, 90, 260, 19))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout1 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout1.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout1.setObjectName("horizontalLayout1")
        self.types_1_insert_radio = QtWidgets.QRadioButton(self.layoutWidget2)
        self.types_1_insert_radio.setChecked(True)
        self.types_1_insert_radio.setObjectName("types_1_insert_radio")
        self.horizontalLayout1.addWidget(self.types_1_insert_radio)
        self.types_1_update_radio = QtWidgets.QRadioButton(self.layoutWidget2)
        self.types_1_update_radio.setObjectName("types_1_update_radio")
        self.horizontalLayout1.addWidget(self.types_1_update_radio)
        self.types_1_remove_radio = QtWidgets.QRadioButton(self.layoutWidget2)
        self.types_1_remove_radio.setObjectName("types_1_remove_radio")
        self.horizontalLayout1.addWidget(self.types_1_remove_radio)
        self.content.addWidget(self.types_1_content)
        self.types_2_content = QtWidgets.QWidget()
        self.types_2_content.setObjectName("types_2_content")
        self.types_2_content_title = QtWidgets.QLabel(self.types_2_content)
        self.types_2_content_title.setGeometry(QtCore.QRect(10, -10, 561, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.types_2_content_title.setFont(font)
        self.types_2_content_title.setObjectName("types_2_content_title")
        self.types_2_content_line = QtWidgets.QFrame(self.types_2_content)
        self.types_2_content_line.setGeometry(QtCore.QRect(-20, 40, 891, 20))
        self.types_2_content_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.types_2_content_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.types_2_content_line.setObjectName("types_2_content_line")
        self.types_2_code_label = QtWidgets.QLabel(self.types_2_content)
        self.types_2_code_label.setGeometry(QtCore.QRect(90, 140, 381, 16))
        self.types_2_code_label.setObjectName("types_2_code_label")
        self.types_2_code_combobox = QtWidgets.QComboBox(self.types_2_content)
        self.types_2_code_combobox.setGeometry(QtCore.QRect(508, 120, 181, 22))
        self.types_2_code_combobox.setObjectName("types_2_code_combobox")
        self.types_2_name_label = QtWidgets.QLabel(self.types_2_content)
        self.types_2_name_label.setGeometry(QtCore.QRect(80, 170, 401, 16))
        self.types_2_name_label.setObjectName("types_2_name_label")
        self.types_2_description_label = QtWidgets.QLabel(self.types_2_content)
        self.types_2_description_label.setGeometry(QtCore.QRect(80, 210, 511, 61))
        self.types_2_description_label.setWordWrap(True)
        self.types_2_description_label.setObjectName("types_2_description_label")
        self.types_2_price_label = QtWidgets.QLabel(self.types_2_content)
        self.types_2_price_label.setGeometry(QtCore.QRect(80, 280, 501, 16))
        self.types_2_price_label.setObjectName("types_2_price_label")
        self.content.addWidget(self.types_2_content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.sideBar.setCurrentIndex(0)
        self.content.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Press on a Button to update the sidebar!"))
        self.home_sidebar_1.setText(_translate("MainWindow", "PushButton"))
        self.home_sidebar_2.setText(_translate("MainWindow", "PushButton"))
        self.patients_sidebar_1.setText(_translate("MainWindow", "Add or Edit Patients"))
        self.patients_sidebar_1.setProperty("nxt_page", _translate("MainWindow", "patients_2_content"))
        self.patients_sidebar_2.setText(_translate("MainWindow", "View Patient Details"))
        self.patients_sidebar_2.setProperty("nxt_page", _translate("MainWindow", "patients_1_content"))
        self.taken_sidebar_1.setText(_translate("MainWindow", "Add New Appointment"))
        self.taken_sidebar_1.setProperty("nxt_page", _translate("MainWindow", "taken_2_content"))
        self.taken_sidebar_2.setText(_translate("MainWindow", "View Appointments"))
        self.taken_sidebar_2.setProperty("nxt_page", _translate("MainWindow", "taken_1_content"))
        self.taken_sidebar_5.setText(_translate("MainWindow", "Add New Test"))
        self.taken_sidebar_5.setProperty("nxt_page", _translate("MainWindow", "taken_1_content"))
        self.types_sidebar_1.setText(_translate("MainWindow", "Add or Edit Test Types"))
        self.types_sidebar_1.setProperty("nxt_page", _translate("MainWindow", "types_2_content"))
        self.types_sidebar_2.setText(_translate("MainWindow", "View Test Types"))
        self.types_sidebar_2.setProperty("nxt_page", _translate("MainWindow", "types_1_content"))
        self.home_title_button.setText(_translate("MainWindow", "Home"))
        self.home_title_button.setProperty("nxt_page", _translate("MainWindow", "home_content"))
        self.patients_title_button.setText(_translate("MainWindow", "Patients"))
        self.patients_title_button.setProperty("nxt_page", _translate("MainWindow", "patients_1_content"))
        self.taken_title_button.setText(_translate("MainWindow", "Taken"))
        self.taken_title_button.setProperty("nxt_page", _translate("MainWindow", "taken_1_content"))
        self.type_title_button.setText(_translate("MainWindow", "Types"))
        self.type_title_button.setProperty("nxt_page", _translate("MainWindow", "types_1_content"))
        self.home_content_title.setText(_translate("MainWindow", "Home"))
        self.patient_1_content_title.setText(_translate("MainWindow", "Add or Edit Patients"))
        self.patient_1_update_button.setText(_translate("MainWindow", "PushButton"))
        self.patient_1_insert_radio.setText(_translate("MainWindow", "Insert"))
        self.patient_1_update_radio.setText(_translate("MainWindow", "Update"))
        self.patient_1_remove_radio.setText(_translate("MainWindow", "Remove"))
        self.patient_2_content_title.setText(_translate("MainWindow", "View Patient Details"))
        self.patients_2_SNO_title.setText(_translate("MainWindow", "Name"))
        self.patients_2_DOB_title.setText(_translate("MainWindow", "DOB"))
        self.patients_2_address_title.setText(_translate("MainWindow", "Address"))
        self.patients_2_POST_title.setText(_translate("MainWindow", "Postcode"))
        self.patients_2_height_title.setText(_translate("MainWindow", "Height"))
        self.patients_2_weight_title.setText(_translate("MainWindow", "Weight"))
        self.taken_1_patient_info.setText(_translate("MainWindow", "Patient:"))
        self.taken_1_code_info.setText(_translate("MainWindow", "Paid:"))
        self.taken_1_date_info.setText(_translate("MainWindow", "Date:"))
        self.taken_1_results_info.setText(_translate("MainWindow", "Results:"))
        self.pushButton.setText(_translate("MainWindow", "Insert"))
        self.patient_2_content_title_3.setText(_translate("MainWindow", "Edit or Remove Appointments"))
        self.taken_1_insert_radio.setText(_translate("MainWindow", "Insert"))
        self.taken_1_update_radio.setText(_translate("MainWindow", "Update"))
        self.taken_1_remove_radio.setText(_translate("MainWindow", "Remove"))
        self.taken_2_content_title.setText(_translate("MainWindow", "View Tests Taken"))
        self.taken_2_patient_info.setText(_translate("MainWindow", "Patient:"))
        self.taken_2_code_info.setText(_translate("MainWindow", "Text Code:"))
        self.taken_2_date_info.setText(_translate("MainWindow", "Date:"))
        self.taken_2_results_info.setText(_translate("MainWindow", "Results:"))
        self.taken_2_tests_info.setText(_translate("MainWindow", "Results:"))
        self.label_3.setText(_translate("MainWindow", "Taken_3"))
        self.taken_3_insert_radio.setText(_translate("MainWindow", "Insert"))
        self.taken_3_remove_radio.setText(_translate("MainWindow", "Remove"))
        self.taken_3_update_button.setText(_translate("MainWindow", "PushButton"))
        self.types_1_content_title.setText(_translate("MainWindow", "Add or Edit Test Types"))
        self.types_1_update_button.setText(_translate("MainWindow", "PushButton"))
        self.types_1_insert_radio.setText(_translate("MainWindow", "Insert"))
        self.types_1_update_radio.setText(_translate("MainWindow", "Update"))
        self.types_1_remove_radio.setText(_translate("MainWindow", "Remove"))
        self.types_2_content_title.setText(_translate("MainWindow", "View Test Types"))
        self.types_2_code_label.setText(_translate("MainWindow", "TextLabel"))
        self.types_2_name_label.setText(_translate("MainWindow", "TextLabel"))
        self.types_2_description_label.setText(_translate("MainWindow", "TextLabel"))
        self.types_2_price_label.setText(_translate("MainWindow", "TextLabel"))
