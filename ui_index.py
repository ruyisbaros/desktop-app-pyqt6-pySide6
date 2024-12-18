# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index_2.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1243, 867)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 10, 1243, 853))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 0, 0, 0)
        self.icon_only_widget = QWidget(self.widget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMaximumSize(QSize(71, 16777215))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: white;\n"
"border-radius:3px;\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.icon_only_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_4.setPixmap(QPixmap(u":/imgs/logo.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_12.addLayout(self.horizontalLayout_2)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 35, -1, 30)
        self.dashboard_1 = QPushButton(self.icon_only_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        self.dashboard_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/imgs/dashboardsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/imgs/dashboardsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.dashboard_1)

        self.institution_1 = QPushButton(self.icon_only_widget)
        self.institution_1.setObjectName(u"institution_1")
        self.institution_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/imgs/institutionsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/imgs/institutionsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.institution_1.setIcon(icon1)
        self.institution_1.setIconSize(QSize(100, 16))
        self.institution_1.setCheckable(True)
        self.institution_1.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.institution_1)

        self.student_1 = QPushButton(self.icon_only_widget)
        self.student_1.setObjectName(u"student_1")
        self.student_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/imgs/studentssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/imgs/studentssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.student_1.setIcon(icon2)
        self.student_1.setIconSize(QSize(100, 20))
        self.student_1.setCheckable(True)
        self.student_1.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.student_1)

        self.teachers_1 = QPushButton(self.icon_only_widget)
        self.teachers_1.setObjectName(u"teachers_1")
        self.teachers_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/imgs/teacs.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/imgs/teacherssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.teachers_1.setIcon(icon3)
        self.teachers_1.setIconSize(QSize(100, 20))
        self.teachers_1.setCheckable(True)
        self.teachers_1.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.teachers_1)

        self.finance_1 = QPushButton(self.icon_only_widget)
        self.finance_1.setObjectName(u"finance_1")
        self.finance_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/imgs/financessmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/imgs/financessmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.finance_1.setIcon(icon4)
        self.finance_1.setIconSize(QSize(100, 20))
        self.finance_1.setCheckable(True)
        self.finance_1.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.finance_1)


        self.verticalLayout_12.addLayout(self.verticalLayout_10)

        self.verticalSpacer_2 = QSpacerItem(20, 432, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.settings_1 = QPushButton(self.icon_only_widget)
        self.settings_1.setObjectName(u"settings_1")
        self.settings_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/imgs/settingssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/imgs/settingssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings_1.setIcon(icon5)
        self.settings_1.setIconSize(QSize(100, 20))
        self.settings_1.setCheckable(True)
        self.settings_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.settings_1)

        self.singout_1 = QPushButton(self.icon_only_widget)
        self.singout_1.setObjectName(u"singout_1")
        self.singout_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/imgs/signoutsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/imgs/signoutsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.singout_1.setIcon(icon6)
        self.singout_1.setIconSize(QSize(80, 15))
        self.singout_1.setCheckable(True)
        self.singout_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.singout_1)


        self.verticalLayout_12.addLayout(self.verticalLayout_9)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_text_widget = QWidget(self.widget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(0, 0, 0);\n"
"color:#fff;\n"
"}\n"
"QPushButton{\n"
"height:30px;\n"
"border:none;\n"
"}\n"
"")
        self.verticalLayout_11 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, -1, -1, -1)
        self.label_2 = QLabel(self.icon_text_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_2.setPixmap(QPixmap(u":/imgs/logo.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_text_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_11.addLayout(self.horizontalLayout)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 35, -1, -1)
        self.dashboard_2 = QPushButton(self.icon_text_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dashboard_2.setStyleSheet(u"QPushButton{\n"
"padding-left:-60px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: white;\n"
"border-radius:4px;\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/imgs/dashboard2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/imgs/dashboard1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_2.setIcon(icon7)
        self.dashboard_2.setIconSize(QSize(100, 55))
        self.dashboard_2.setCheckable(True)
        self.dashboard_2.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.dashboard_2)

        self.institution_2 = QPushButton(self.icon_text_widget)
        self.institution_2.setObjectName(u"institution_2")
        self.institution_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.institution_2.setStyleSheet(u"QPushButton{\n"
"padding-left:-65px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: white;\n"
"border-radius:4px;\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/imgs/institution2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/imgs/institution1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.institution_2.setIcon(icon8)
        self.institution_2.setIconSize(QSize(90, 45))
        self.institution_2.setCheckable(True)
        self.institution_2.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.institution_2)

        self.students = QFrame(self.icon_text_widget)
        self.students.setObjectName(u"students")
        self.students.setFrameShape(QFrame.StyledPanel)
        self.students.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.students)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.student_2 = QPushButton(self.students)
        self.student_2.setObjectName(u"student_2")
        self.student_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.student_2.setStyleSheet(u"QPushButton{\n"
"padding-left:-0px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/imgs/students3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9.addFile(u":/imgs/students4.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.student_2.setIcon(icon9)
        self.student_2.setIconSize(QSize(200, 55))
        self.student_2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.student_2)

        self.students_dropdown = QFrame(self.students)
        self.students_dropdown.setObjectName(u"students_dropdown")
        self.students_dropdown.setFrameShape(QFrame.StyledPanel)
        self.students_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.students_dropdown)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.student_info = QPushButton(self.students_dropdown)
        self.student_info.setObjectName(u"student_info")
        self.student_info.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.student_info.setStyleSheet(u"QPushButton{\n"
"padding-left:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:#12b298;\n"
"}\n"
"\n"
"\n"
"")
        self.student_info.setCheckable(True)
        self.student_info.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.student_info)

        self.student_payment = QPushButton(self.students_dropdown)
        self.student_payment.setObjectName(u"student_payment")
        self.student_payment.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.student_payment.setStyleSheet(u"QPushButton{\n"
"padding-left:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:#12b298;\n"
"}")
        self.student_payment.setCheckable(True)
        self.student_payment.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.student_payment)

        self.student_trans = QPushButton(self.students_dropdown)
        self.student_trans.setObjectName(u"student_trans")
        self.student_trans.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.student_trans.setStyleSheet(u"QPushButton{\n"
"padding-left:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:#12b298;\n"
"}")
        self.student_trans.setCheckable(True)
        self.student_trans.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.student_trans)


        self.verticalLayout_4.addWidget(self.students_dropdown)


        self.verticalLayout_7.addWidget(self.students)

        self.teachers = QFrame(self.icon_text_widget)
        self.teachers.setObjectName(u"teachers")
        self.teachers.setFrameShape(QFrame.StyledPanel)
        self.teachers.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.teachers)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.teachers_2 = QPushButton(self.teachers)
        self.teachers_2.setObjectName(u"teachers_2")
        self.teachers_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.teachers_2.setStyleSheet(u"QPushButton{\n"
"padding-left:-2px;\n"
"}\n"
"\n"
"\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/imgs/teachers3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10.addFile(u":/imgs/teachers4.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.teachers_2.setIcon(icon10)
        self.teachers_2.setIconSize(QSize(200, 55))
        self.teachers_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.teachers_2)

        self.teachers_dropdown = QFrame(self.teachers)
        self.teachers_dropdown.setObjectName(u"teachers_dropdown")
        self.teachers_dropdown.setFrameShape(QFrame.StyledPanel)
        self.teachers_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.teachers_dropdown)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.teacher_info = QPushButton(self.teachers_dropdown)
        self.teacher_info.setObjectName(u"teacher_info")
        self.teacher_info.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.teacher_info.setStyleSheet(u"QPushButton{\n"
"padding-left:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:#12b298;\n"
"}")
        self.teacher_info.setCheckable(True)
        self.teacher_info.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.teacher_info)

        self.teachers_salary = QPushButton(self.teachers_dropdown)
        self.teachers_salary.setObjectName(u"teachers_salary")
        self.teachers_salary.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.teachers_salary.setStyleSheet(u"QPushButton{\n"
"padding-left:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:#12b298;\n"
"}")
        self.teachers_salary.setCheckable(True)
        self.teachers_salary.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.teachers_salary)

        self.teacher_trans = QPushButton(self.teachers_dropdown)
        self.teacher_trans.setObjectName(u"teacher_trans")
        self.teacher_trans.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.teacher_trans.setStyleSheet(u"QPushButton{\n"
"padding-left:32px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:#12b298;\n"
"}")
        self.teacher_trans.setCheckable(True)
        self.teacher_trans.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.teacher_trans)


        self.verticalLayout_5.addWidget(self.teachers_dropdown)


        self.verticalLayout_7.addWidget(self.teachers)

        self.finance = QFrame(self.icon_text_widget)
        self.finance.setObjectName(u"finance")
        self.finance.setFrameShape(QFrame.StyledPanel)
        self.finance.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.finance)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.finance_2 = QPushButton(self.finance)
        self.finance_2.setObjectName(u"finance_2")
        self.finance_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.finance_2.setStyleSheet(u"QPushButton{\n"
"padding-left:5px;\n"
"}\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/imgs/finances3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon11.addFile(u":/imgs/finances4.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.finance_2.setIcon(icon11)
        self.finance_2.setIconSize(QSize(200, 100))
        self.finance_2.setCheckable(True)

        self.verticalLayout_6.addWidget(self.finance_2)

        self.finances_dropdown = QFrame(self.finance)
        self.finances_dropdown.setObjectName(u"finances_dropdown")
        self.finances_dropdown.setFrameShape(QFrame.StyledPanel)
        self.finances_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.finances_dropdown)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.budget = QPushButton(self.finances_dropdown)
        self.budget.setObjectName(u"budget")
        self.budget.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.budget.setStyleSheet(u"QPushButton{\n"
"padding-left:-35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:#12b298;\n"
"}")
        self.budget.setCheckable(True)
        self.budget.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.budget)

        self.expenses = QPushButton(self.finances_dropdown)
        self.expenses.setObjectName(u"expenses")
        self.expenses.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.expenses.setStyleSheet(u"QPushButton{\n"
"padding-left:-30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:#12b298;\n"
"}")
        self.expenses.setCheckable(True)
        self.expenses.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.expenses)

        self.business_overview = QPushButton(self.finances_dropdown)
        self.business_overview.setObjectName(u"business_overview")
        self.business_overview.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.business_overview.setStyleSheet(u"QPushButton{\n"
"padding-left:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:#12b298;\n"
"}")
        self.business_overview.setCheckable(True)
        self.business_overview.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.business_overview)


        self.verticalLayout_6.addWidget(self.finances_dropdown)


        self.verticalLayout_7.addWidget(self.finance)


        self.verticalLayout_11.addLayout(self.verticalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 74, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.settings_2 = QPushButton(self.icon_text_widget)
        self.settings_2.setObjectName(u"settings_2")
        self.settings_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.settings_2.setStyleSheet(u"QPushButton{\n"
"padding-left:-40px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: white;\n"
"border-radius:4px;\n"
"}\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/imgs/settings2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon12.addFile(u":/imgs/settings1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings_2.setIcon(icon12)
        self.settings_2.setIconSize(QSize(100, 55))
        self.settings_2.setCheckable(True)
        self.settings_2.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.settings_2)

        self.signout_2 = QPushButton(self.icon_text_widget)
        self.signout_2.setObjectName(u"signout_2")
        self.signout_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.signout_2.setStyleSheet(u"QPushButton{\n"
"padding-left:-30px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: white;\n"
"border-radius:4px;\n"
"}\n"
"")
        icon13 = QIcon()
        icon13.addFile(u":/imgs/signout2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon13.addFile(u":/imgs/signout1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.signout_2.setIcon(icon13)
        self.signout_2.setIconSize(QSize(100, 55))
        self.signout_2.setCheckable(True)
        self.signout_2.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.signout_2)


        self.verticalLayout_11.addLayout(self.verticalLayout_8)


        self.gridLayout.addWidget(self.icon_text_widget, 0, 1, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.header_widget = QWidget(self.widget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMinimumSize(QSize(911, 91))
        self.header_widget.setMaximumSize(QSize(1666666, 91))
        self.horizontalLayout_5 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.header_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/imgs/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon14)
        self.pushButton.setIconSize(QSize(29, 35))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 15, -1, 15)
        self.label = QLabel(self.header_widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label.setFont(font1)

        self.verticalLayout_13.addWidget(self.label)

        self.label_5 = QLabel(self.header_widget)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color:#484848;")

        self.verticalLayout_13.addWidget(self.label_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_13)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(351, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 20, -1)
        self.search_anything = QLineEdit(self.header_widget)
        self.search_anything.setObjectName(u"search_anything")
        self.search_anything.setMinimumSize(QSize(0, 31))
        self.search_anything.setMaximumSize(QSize(16777215, 31))
        self.search_anything.setStyleSheet(u"QLineEdit{\n"
"padding-left:10px;\n"
"border: 1px solid gray;\n"
"border-radius:10px\n"
"}")

        self.horizontalLayout_3.addWidget(self.search_anything)

        self.profile_img = QLabel(self.header_widget)
        self.profile_img.setObjectName(u"profile_img")
        self.profile_img.setMinimumSize(QSize(40, 40))
        self.profile_img.setMaximumSize(QSize(40, 40))
        self.profile_img.setPixmap(QPixmap(u":/imgs/profile.png"))
        self.profile_img.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.profile_img)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_14.addWidget(self.header_widget)

        self.main_screen_widget = QWidget(self.widget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setMinimumSize(QSize(911, 0))
        self.main_screen_widget.setMaximumSize(QSize(1666666, 751))
        self.main_screen_widget.setStyleSheet(u"")
        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, 9, 891, 741))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(300, 180, 281, 231))
        font3 = QFont()
        font3.setPointSize(25)
        font3.setBold(True)
        self.label_7.setFont(font3)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(280, 150, 281, 231))
        self.label_8.setFont(font3)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 0, 221, 41))
        font4 = QFont()
        font4.setFamilies([u"DejaVu Sans Mono"])
        font4.setPointSize(20)
        font4.setBold(True)
        self.label_9.setFont(font4)
        self.label_19 = QLabel(self.page_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(0, 50, 321, 31))
        font5 = QFont()
        font5.setFamilies([u"DejaVu Sans Mono"])
        font5.setPointSize(10)
        font5.setBold(False)
        self.label_19.setFont(font5)
        self.studentInfo_table = QTableWidget(self.page_3)
        if (self.studentInfo_table.columnCount() < 10):
            self.studentInfo_table.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.studentInfo_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.studentInfo_table.setObjectName(u"studentInfo_table")
        self.studentInfo_table.setGeometry(QRect(-5, 220, 900, 491))
        self.studentInfo_table.setMaximumSize(QSize(900, 16777215))
        self.studentInfo_table.setStyleSheet(u"QHeaderView::section{\n"
"font-weight:bold;\n"
"color:white;\n"
"background-color:black;\n"
"}\n"
"QTableWidget{\n"
"alternate-background-color:#b0edfb;\n"
"background-color:#f4f9fa;\n"
"}")
        self.studentInfo_table.setAlternatingRowColors(True)
        self.widget1 = QWidget(self.page_3)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 90, 441, 43))
        self.horizontalLayout_6 = QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.add_student_btn = QPushButton(self.widget1)
        self.add_student_btn.setObjectName(u"add_student_btn")
        self.add_student_btn.setMinimumSize(QSize(0, 41))
        self.add_student_btn.setMaximumSize(QSize(16777215, 41))
        self.add_student_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_student_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-weight:bold;\n"
"font-size:12px;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/imgs/add student.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_student_btn.setIcon(icon15)
        self.add_student_btn.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.add_student_btn)

        self.excelExport_btn = QPushButton(self.widget1)
        self.excelExport_btn.setObjectName(u"excelExport_btn")
        self.excelExport_btn.setMinimumSize(QSize(0, 41))
        self.excelExport_btn.setMaximumSize(QSize(16777215, 41))
        self.excelExport_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.excelExport_btn.setStyleSheet(u"QPushButton{\n"
"background-color:#34d481;\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-weight:bold;\n"
"font-size:12px\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/imgs/excel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.excelExport_btn.setIcon(icon16)
        self.excelExport_btn.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.excelExport_btn)

        self.pdfExport_btn = QPushButton(self.widget1)
        self.pdfExport_btn.setObjectName(u"pdfExport_btn")
        self.pdfExport_btn.setMinimumSize(QSize(0, 41))
        self.pdfExport_btn.setMaximumSize(QSize(16777215, 41))
        self.pdfExport_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pdfExport_btn.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(255,78,78);\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-weight:bold;\n"
"font-size:12px\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/imgs/pdf.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pdfExport_btn.setIcon(icon17)
        self.pdfExport_btn.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.pdfExport_btn)

        self.widget2 = QWidget(self.page_3)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 150, 601, 43))
        self.horizontalLayout_7 = QHBoxLayout(self.widget2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.select_gender = QComboBox(self.widget2)
        self.select_gender.addItem("")
        self.select_gender.addItem("")
        self.select_gender.addItem("")
        self.select_gender.setObjectName(u"select_gender")
        self.select_gender.setMinimumSize(QSize(150, 0))
        self.select_gender.setStyleSheet(u"QComboBox{\n"
"border:2px solid white;\n"
"border-radius:9px;\n"
"padding:1px 18px 1px 15px;\n"
"background-color:black;\n"
"color:white;\n"
"height:35px;\n"
"font-weight:bold;\n"
"selection-background-color:#2980b9;\n"
"}")

        self.horizontalLayout_7.addWidget(self.select_gender)

        self.select_class = QComboBox(self.widget2)
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.setObjectName(u"select_class")
        self.select_class.setMinimumSize(QSize(150, 0))
        self.select_class.setStyleSheet(u"QComboBox{\n"
"border:2px solid white;\n"
"border-radius:9px;\n"
"padding:1px 18px 1px 15px;\n"
"background-color:black;\n"
"color:white;\n"
"height:35px;\n"
"font-weight:bold;\n"
"selection-background-color:#2980b9;\n"
"}")

        self.horizontalLayout_7.addWidget(self.select_class)

        self.search_student = QLineEdit(self.widget2)
        self.search_student.setObjectName(u"search_student")
        self.search_student.setMinimumSize(QSize(0, 38))
        self.search_student.setMaximumSize(QSize(16777215, 38))
        self.search_student.setStyleSheet(u"QLineEdit{\n"
"padding-left:10px;\n"
"border: 1px solid gray;\n"
"border-radius:10px\n"
"}")

        self.horizontalLayout_7.addWidget(self.search_student)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_10 = QLabel(self.page_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(300, 160, 301, 231))
        self.label_10.setFont(font3)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_11 = QLabel(self.page_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(300, 170, 341, 231))
        self.label_11.setFont(font3)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_12 = QLabel(self.page_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(310, 190, 281, 231))
        self.label_12.setFont(font3)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_13 = QLabel(self.page_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(340, 190, 281, 231))
        self.label_13.setFont(font3)
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.label_14 = QLabel(self.page_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(320, 170, 331, 231))
        self.label_14.setFont(font3)
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.label_15 = QLabel(self.page_9)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(360, 230, 281, 231))
        self.label_15.setFont(font3)
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.label_16 = QLabel(self.page_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(320, 190, 281, 231))
        self.label_16.setFont(font3)
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.label_17 = QLabel(self.page_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(320, 220, 351, 231))
        self.label_17.setFont(font3)
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.label_18 = QLabel(self.page_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(340, 160, 281, 231))
        self.label_18.setFont(font3)
        self.stackedWidget.addWidget(self.page_12)

        self.verticalLayout_14.addWidget(self.main_screen_widget)


        self.gridLayout.addLayout(self.verticalLayout_14, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.student_2.toggled.connect(self.students_dropdown.setHidden)
        self.teachers_2.toggled.connect(self.teachers_dropdown.setHidden)
        self.finance_2.toggled.connect(self.finances_dropdown.setHidden)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.institution_2.toggled.connect(self.institution_1.setChecked)
        self.student_2.toggled.connect(self.student_1.setChecked)
        self.teachers_2.toggled.connect(self.teachers_1.setChecked)
        self.finance_2.toggled.connect(self.finance_1.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.signout_2.toggled.connect(self.singout_1.setChecked)
        self.singout_1.toggled.connect(MainWindow.close)
        self.signout_2.toggled.connect(MainWindow.close)
        self.pushButton.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton.toggled.connect(self.icon_only_widget.setVisible)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.dashboard_1.setText("")
        self.institution_1.setText("")
        self.student_1.setText("")
        self.teachers_1.setText("")
        self.finance_1.setText("")
        self.settings_1.setText("")
        self.singout_1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"School", None))
        self.dashboard_2.setText("")
        self.institution_2.setText("")
        self.student_2.setText("")
        self.student_info.setText(QCoreApplication.translate("MainWindow", u"Student Information", None))
        self.student_payment.setText(QCoreApplication.translate("MainWindow", u"Student Payments", None))
        self.student_trans.setText(QCoreApplication.translate("MainWindow", u"Student Transactions", None))
        self.teachers_2.setText("")
        self.teacher_info.setText(QCoreApplication.translate("MainWindow", u"Teacher Information", None))
        self.teachers_salary.setText(QCoreApplication.translate("MainWindow", u"Teacher Salaries", None))
        self.teacher_trans.setText(QCoreApplication.translate("MainWindow", u"Teacher Transactions", None))
        self.finance_2.setText("")
        self.budget.setText(QCoreApplication.translate("MainWindow", u"Budgets", None))
        self.expenses.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.business_overview.setText(QCoreApplication.translate("MainWindow", u"Business Overview", None))
        self.settings_2.setText("")
        self.signout_2.setText("")
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hello Ahmet", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Welcome to your page.", None))
        self.search_anything.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter keyword for search things...", None))
        self.profile_img.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Institution", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Student Info", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Wellcome to the student information page.", None))
        ___qtablewidgetitem = self.studentInfo_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Student ID", None));
        ___qtablewidgetitem1 = self.studentInfo_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.studentInfo_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem3 = self.studentInfo_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem4 = self.studentInfo_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem5 = self.studentInfo_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"DOB", None));
        ___qtablewidgetitem6 = self.studentInfo_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem7 = self.studentInfo_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem8 = self.studentInfo_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Phone No", None));
        ___qtablewidgetitem9 = self.studentInfo_table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.add_student_btn.setText(QCoreApplication.translate("MainWindow", u"Add Student", None))
        self.excelExport_btn.setText(QCoreApplication.translate("MainWindow", u"Export to Excel", None))
        self.pdfExport_btn.setText(QCoreApplication.translate("MainWindow", u"Export to PDF", None))
        self.select_gender.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT_GENDER", None))
        self.select_gender.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.select_gender.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))

        self.select_class.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT_CLASS", None))
        self.select_class.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade_1", None))
        self.select_class.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade_2", None))
        self.select_class.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade_3", None))
        self.select_class.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade_4", None))
        self.select_class.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade_5", None))
        self.select_class.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade_6", None))
        self.select_class.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade_7", None))
        self.select_class.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade_8", None))
        self.select_class.setItemText(9, QCoreApplication.translate("MainWindow", u"Grade_9", None))
        self.select_class.setItemText(10, QCoreApplication.translate("MainWindow", u"Grade_10", None))
        self.select_class.setItemText(11, QCoreApplication.translate("MainWindow", u"Grade_11", None))
        self.select_class.setItemText(12, QCoreApplication.translate("MainWindow", u"Grade_12", None))

        self.search_student.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search student...", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Student Payment", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Student Trans", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Teacher Info", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Teacher Salary", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Teacher Trans", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Budget", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Business Over", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

