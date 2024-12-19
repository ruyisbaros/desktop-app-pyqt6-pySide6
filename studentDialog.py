# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'studentDialog.ui'
##
# Created by: Qt User Interface Compiler version 6.8.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
                               QFrame, QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QVBoxLayout, QWidget, QMessageBox)

import mysql.connector
import random
from datetime import datetime


class Ui_StudentsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(548, 584)
        self.setStyleSheet(u"QDialog{\n"
                           "background-color:white;\n"
                           "}\n"
                           "\n"
                           "QLineEdit{\n"
                           "border:1px solid gray;\n"
                           "border-radius:6px;\n"
                           "padding-left:10px;\n"
                           "height:35px;\n"
                           "}\n"
                           "QDateEdit{\n"
                           "border:1px solid gray;\n"
                           "border-radius:6px;\n"
                           "padding-left:10px;\n"
                           "height:31px;\n"
                           "}\n"
                           "QComboBox{\n"
                           "border:2px solid white;\n"
                           "border-radius:9px;\n"
                           "padding:1px 18px 1px 15px;\n"
                           "background-color:black;\n"
                           "color:white;\n"
                           "height:35px;\n"
                           "font-weight:bold;\n"
                           "selection-background-color:#2980b9;\n"
                           "}")
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 551, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 16, 261, 31))
        font = QFont()
        font.setFamilies([u"DejaVu Sans Mono"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 90, 531, 361))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.full_name = QVBoxLayout()
        self.full_name.setObjectName(u"full_name")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"DejaVu Sans Mono"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_2.setFont(font1)

        self.full_name.addWidget(self.label_2)

        self.name_lineEdit = QLineEdit(self.widget)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMinimumSize(QSize(0, 35))
        self.name_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.full_name.addWidget(self.name_lineEdit)

        self.verticalLayout_4.addLayout(self.full_name)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setFamilies([u"DejaVu Sans Mono"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.label_6.setFont(font2)

        self.verticalLayout.addWidget(self.label_6)

        self.gender_comboBox = QComboBox(self.widget)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")

        self.verticalLayout.addWidget(self.gender_comboBox)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_7)

        self.class_comboBox = QComboBox(self.widget)
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.setObjectName(u"class_comboBox")

        self.verticalLayout_2.addWidget(self.class_comboBox)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_8)

        self.dob_comboBox = QDateEdit(self.widget)
        self.dob_comboBox.setObjectName(u"dob_comboBox")

        self.verticalLayout_3.addWidget(self.dob_comboBox)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.full_name_2 = QVBoxLayout()
        self.full_name_2.setObjectName(u"full_name_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.full_name_2.addWidget(self.label_3)

        self.email_lineEdit = QLineEdit(self.widget)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.email_lineEdit.setMinimumSize(QSize(0, 35))
        self.email_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.full_name_2.addWidget(self.email_lineEdit)

        self.verticalLayout_4.addLayout(self.full_name_2)

        self.full_name_3 = QVBoxLayout()
        self.full_name_3.setObjectName(u"full_name_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.full_name_3.addWidget(self.label_4)

        self.address_lineEdit = QLineEdit(self.widget)
        self.address_lineEdit.setObjectName(u"address_lineEdit")
        self.address_lineEdit.setMinimumSize(QSize(0, 35))
        self.address_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.full_name_3.addWidget(self.address_lineEdit)

        self.verticalLayout_4.addLayout(self.full_name_3)

        self.full_name_4 = QVBoxLayout()
        self.full_name_4.setObjectName(u"full_name_4")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.full_name_4.addWidget(self.label_5)

        self.phone_lineEdit = QLineEdit(self.widget)
        self.phone_lineEdit.setObjectName(u"phone_lineEdit")
        self.phone_lineEdit.setMinimumSize(QSize(0, 35))
        self.phone_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.full_name_4.addWidget(self.phone_lineEdit)

        self.verticalLayout_4.addLayout(self.full_name_4)

        self.widget1 = QWidget(self)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(290, 510, 251, 43))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.save_student_btn = QPushButton(self.widget1)
        self.save_student_btn.setObjectName(u"save_student_btn")
        self.save_student_btn.setMinimumSize(QSize(0, 41))
        self.save_student_btn.setMaximumSize(QSize(16777215, 41))
        self.save_student_btn.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_student_btn.setStyleSheet(u"QPushButton{\n"
                                            "background-color:#34d481;\n"
                                            "color:white;\n"
                                            "border:none;\n"
                                            "border-radius:8px;\n"
                                            "font-weight:bold;\n"
                                            "font-size:15px\n"
                                            "}")

        self.horizontalLayout_2.addWidget(self.save_student_btn)

        self.cancel_add_student_btn = QPushButton(self.widget1)
        self.cancel_add_student_btn.setObjectName(u"cancel_add_student_btn")
        self.cancel_add_student_btn.setMinimumSize(QSize(0, 41))
        self.cancel_add_student_btn.setMaximumSize(QSize(16777215, 41))
        self.cancel_add_student_btn.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.cancel_add_student_btn.setStyleSheet(u"QPushButton{\n"
                                                  "background-color:red;\n"
                                                  "color:white;\n"
                                                  "border:none;\n"
                                                  "border-radius:8px;\n"
                                                  "font-weight:bold;\n"
                                                  "font-size:15px\n"
                                                  "}")
        self.cancel_add_student_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.cancel_add_student_btn)

        self.retranslateUi(self)
        self.cancel_add_student_btn.toggled.connect(self.close)

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self, StudentsDialog):
        StudentsDialog.setWindowTitle(QCoreApplication.translate(
            "StudentsDialog", u"Students Dialog", None))
        self.label.setText(QCoreApplication.translate(
            "StudentsDialog", u"Add New Student", None))
        self.label_2.setText(QCoreApplication.translate(
            "StudentsDialog", u"Full Name", None))
        self.label_6.setText(QCoreApplication.translate(
            "StudentsDialog", u"Gender", None))
        self.gender_comboBox.setItemText(
            0, QCoreApplication.translate("StudentsDialog", u"Male", None))
        self.gender_comboBox.setItemText(
            1, QCoreApplication.translate("StudentsDialog", u"Female", None))

        self.label_7.setText(QCoreApplication.translate(
            "StudentsDialog", u"Class", None))
        self.class_comboBox.setItemText(
            0, QCoreApplication.translate("StudentsDialog", u"Grade_1", None))
        self.class_comboBox.setItemText(
            1, QCoreApplication.translate("StudentsDialog", u"Grade_2", None))
        self.class_comboBox.setItemText(
            2, QCoreApplication.translate("StudentsDialog", u"Grade_3", None))
        self.class_comboBox.setItemText(
            3, QCoreApplication.translate("StudentsDialog", u"Grade_4", None))
        self.class_comboBox.setItemText(
            4, QCoreApplication.translate("StudentsDialog", u"Grade_5", None))
        self.class_comboBox.setItemText(
            5, QCoreApplication.translate("StudentsDialog", u"Grade_6", None))
        self.class_comboBox.setItemText(
            6, QCoreApplication.translate("StudentsDialog", u"Grade_7", None))
        self.class_comboBox.setItemText(
            7, QCoreApplication.translate("StudentsDialog", u"Grade_8", None))
        self.class_comboBox.setItemText(
            8, QCoreApplication.translate("StudentsDialog", u"Grade_9", None))
        self.class_comboBox.setItemText(
            9, QCoreApplication.translate("StudentsDialog", u"Grade_10", None))
        self.class_comboBox.setItemText(
            10, QCoreApplication.translate("StudentsDialog", u"Grade_11", None))
        self.class_comboBox.setItemText(
            11, QCoreApplication.translate("StudentsDialog", u"Grade_12", None))

        self.label_8.setText(QCoreApplication.translate(
            "StudentsDialog", u"Date of Birth", None))
        self.label_3.setText(QCoreApplication.translate(
            "StudentsDialog", u"Email", None))
        self.label_4.setText(QCoreApplication.translate(
            "StudentsDialog", u"Address", None))
        self.label_5.setText(QCoreApplication.translate(
            "StudentsDialog", u"Phone Number", None))
        self.save_student_btn.setText(
            QCoreApplication.translate("StudentsDialog", u"Save", None))
        self.cancel_add_student_btn.setText(
            QCoreApplication.translate("StudentsDialog", u"Cancel", None))
    # retranslateUi
    # when press add student button popup dialog
        self.save_student_btn.clicked.connect(self.add_student_box)
        self.cancel_add_student_btn.clicked.connect(self.close)
    # DB CONNECTION

    def create_connection(self):
        db_name = "my_school_database"
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
        )
        cursor = self.mydb.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")

        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database=db_name
        )
        return self.mydb

    # ADD STUDENT
    def add_student(self):
        names = self.name_lineEdit.text()
        gender = self.gender_comboBox.currentText()
        student_id = self.generate_student_id(gender)
        grade = self.class_comboBox.currentText()
        birthday = self.dob_comboBox.date().toString(Qt.ISODate)  # Qt.ISODate
        age = self.calculate_age(birthday)
        email = self.email_lineEdit.text()
        address = self.address_lineEdit.text()
        phone_number = self.phone_lineEdit.text()

        if not student_id or not names or not gender or not grade or not birthday or not email or not address or not phone_number:
            QMessageBox.critical(self, "Error", "All fields are required!")
            return

        cursor = self.create_connection().cursor()
        cursor.execute(
            "INSERT INTO students (student_id, names, gender, grade, birthday, email, address, phone_number, age) VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s)",
            (student_id, names, gender, grade, birthday,
             email, address, phone_number, age)
        )
        self.mydb.commit()
        QMessageBox.information(self, "Success", "Student added successfully!")
        self.clear_fields()
        self.mydb.close()

    # GENERATE STUDENT ID
    def generate_student_id(self, gender):
        cursor = self.create_connection().cursor()
        while True:
            if gender == "Male":
                id_start_value = '24' + '/U/M'
            else:
                id_start_value = '24' + '/U/F'

            student_id = id_start_value + '04d' + random.randint(1, 1000)
            cursor.execute(
                f"SELECT student_id FROM students WHERE student_id = '{student_id}'")
            if not cursor.fetchone():
                return student_id

    def handleDateFormat(self):
        dob = self.dob_comboBox.date().toString("yyyy-MM-dd")
        self.dob_label.setText(dob)

    # CALCULATE AGE
    def calculate_age(self, birthday):
        current_date = datetime.now()
        birth_date = datetime.strptime(birthday, "%Y-%m-%d")
        age = current_date.year - birth_date.year - \
            ((current_date.month, current_date.day)
             < (birth_date.month, birth_date.day))
        return age

    # CLEAR FIELDS
    def clear_fields(self):
        self.name_lineEdit.clear()
        self.gender_comboBox.setCurrentIndex(0)
        self.class_comboBox.setCurrentIndex(0)
        self.dob_label.clear()
        self.email_lineEdit.clear()
        self.address_lineEdit.clear()
        self.phone_lineEdit.clear()

    def show_custom_message(self):
        msg_box = QMessageBox(self)

    def add_student_box(self):
        self.add_student()
        self.accept()
