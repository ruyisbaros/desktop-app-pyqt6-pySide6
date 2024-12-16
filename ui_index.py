# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1231, 867)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 3, 1233, 861))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.widget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(71, 0))
        self.icon_only_widget.setMaximumSize(QSize(71, 16777215))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color:white;\n"
"border-radius:3px;\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 30, -1, 15)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.icon_only_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setPixmap(QPixmap(u":/logo.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.std_tc_fi_blck_1 = QVBoxLayout()
        self.std_tc_fi_blck_1.setSpacing(10)
        self.std_tc_fi_blck_1.setObjectName(u"std_tc_fi_blck_1")
        self.std_tc_fi_blck_1.setContentsMargins(-1, 35, -1, 15)
        self.dashboard_1 = QPushButton(self.icon_only_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        self.dashboard_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dashboard_1.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/dashboardsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/dashboardsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.std_tc_fi_blck_1.addWidget(self.dashboard_1)

        self.instution_1 = QPushButton(self.icon_only_widget)
        self.instution_1.setObjectName(u"instution_1")
        self.instution_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.instution_1.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/institutionsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/institutionsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.instution_1.setIcon(icon1)
        self.instution_1.setIconSize(QSize(100, 16))
        self.instution_1.setCheckable(True)
        self.instution_1.setAutoExclusive(True)

        self.std_tc_fi_blck_1.addWidget(self.instution_1)

        self.stdn_1 = QPushButton(self.icon_only_widget)
        self.stdn_1.setObjectName(u"stdn_1")
        self.stdn_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.stdn_1.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/studentssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/studentssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.stdn_1.setIcon(icon2)
        self.stdn_1.setIconSize(QSize(100, 20))
        self.stdn_1.setCheckable(True)
        self.stdn_1.setAutoExclusive(True)

        self.std_tc_fi_blck_1.addWidget(self.stdn_1)

        self.teachers_1 = QPushButton(self.icon_only_widget)
        self.teachers_1.setObjectName(u"teachers_1")
        self.teachers_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.teachers_1.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/teacs.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/teacherssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.teachers_1.setIcon(icon3)
        self.teachers_1.setIconSize(QSize(100, 20))
        self.teachers_1.setCheckable(True)
        self.teachers_1.setAutoExclusive(True)

        self.std_tc_fi_blck_1.addWidget(self.teachers_1)

        self.finance_1 = QPushButton(self.icon_only_widget)
        self.finance_1.setObjectName(u"finance_1")
        self.finance_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.finance_1.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/financessmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/financessmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.finance_1.setIcon(icon4)
        self.finance_1.setIconSize(QSize(100, 20))
        self.finance_1.setCheckable(True)
        self.finance_1.setAutoExclusive(True)

        self.std_tc_fi_blck_1.addWidget(self.finance_1)


        self.verticalLayout_8.addLayout(self.std_tc_fi_blck_1)

        self.verticalSpacer_2 = QSpacerItem(20, 443, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.set_sig_blc_1 = QVBoxLayout()
        self.set_sig_blc_1.setSpacing(20)
        self.set_sig_blc_1.setObjectName(u"set_sig_blc_1")
        self.settings_1 = QPushButton(self.icon_only_widget)
        self.settings_1.setObjectName(u"settings_1")
        self.settings_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.settings_1.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/settingssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/settingssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings_1.setIcon(icon5)
        self.settings_1.setIconSize(QSize(100, 20))
        self.settings_1.setCheckable(True)
        self.settings_1.setAutoExclusive(True)

        self.set_sig_blc_1.addWidget(self.settings_1)

        self.signout_1 = QPushButton(self.icon_only_widget)
        self.signout_1.setObjectName(u"signout_1")
        self.signout_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.signout_1.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/signoutsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/signoutsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.signout_1.setIcon(icon6)
        self.signout_1.setIconSize(QSize(100, 20))
        self.signout_1.setCheckable(True)
        self.signout_1.setAutoExclusive(True)

        self.set_sig_blc_1.addWidget(self.signout_1)


        self.verticalLayout_8.addLayout(self.set_sig_blc_1)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_text_widget = QWidget(self.widget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"height:30px;\n"
"border:none\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 30, -1, 15)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, -1, -1, -1)
        self.logo = QLabel(self.icon_text_widget)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(40, 40))
        self.logo.setPixmap(QPixmap(u":/logo.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logo)

        self.scholl_title = QLabel(self.icon_text_widget)
        self.scholl_title.setObjectName(u"scholl_title")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.scholl_title.setFont(font)

        self.horizontalLayout.addWidget(self.scholl_title)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.st_tc_fi_block_2 = QVBoxLayout()
        self.st_tc_fi_block_2.setSpacing(20)
        self.st_tc_fi_block_2.setObjectName(u"st_tc_fi_block_2")
        self.st_tc_fi_block_2.setContentsMargins(-1, 35, -1, -1)
        self.dashboard_2 = QPushButton(self.icon_text_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dashboard_2.setStyleSheet(u"QPushButton{\n"
"padding-left:-60px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color:white;\n"
"border-radius:3px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/dashboard2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/dashboard1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_2.setIcon(icon7)
        self.dashboard_2.setIconSize(QSize(100, 60))
        self.dashboard_2.setCheckable(True)
        self.dashboard_2.setAutoExclusive(True)

        self.st_tc_fi_block_2.addWidget(self.dashboard_2)

        self.instution_2 = QPushButton(self.icon_text_widget)
        self.instution_2.setObjectName(u"instution_2")
        self.instution_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.instution_2.setStyleSheet(u"QPushButton{\n"
"padding-left:-63px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color:white;\n"
"border-radius:3px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/institution2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/institution1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.instution_2.setIcon(icon8)
        self.instution_2.setIconSize(QSize(95, 45))
        self.instution_2.setCheckable(True)
        self.instution_2.setAutoExclusive(True)

        self.st_tc_fi_block_2.addWidget(self.instution_2)

        self.students = QFrame(self.icon_text_widget)
        self.students.setObjectName(u"students")
        self.students.setFrameShape(QFrame.StyledPanel)
        self.students.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.students)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stdn_2 = QPushButton(self.students)
        self.stdn_2.setObjectName(u"stdn_2")
        self.stdn_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.stdn_2.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/students3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9.addFile(u":/students4.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.stdn_2.setIcon(icon9)
        self.stdn_2.setIconSize(QSize(200, 60))
        self.stdn_2.setCheckable(True)
        self.stdn_2.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.stdn_2)

        self.students_drp_dwn = QFrame(self.students)
        self.students_drp_dwn.setObjectName(u"students_drp_dwn")
        self.students_drp_dwn.setFrameShape(QFrame.StyledPanel)
        self.students_drp_dwn.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.students_drp_dwn)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stdn_info = QPushButton(self.students_drp_dwn)
        self.stdn_info.setObjectName(u"stdn_info")
        self.stdn_info.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.stdn_info.setStyleSheet(u"QPushButton{\n"
"padding-left:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:#12b298;\n"
"cursor:pointer\n"
"}")
        self.stdn_info.setCheckable(True)

        self.verticalLayout.addWidget(self.stdn_info)

        self.stdn_payments = QPushButton(self.students_drp_dwn)
        self.stdn_payments.setObjectName(u"stdn_payments")
        self.stdn_payments.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.stdn_payments.setStyleSheet(u"QPushButton{\n"
"padding-left:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:#12b298;\n"
"cursor:pointer\n"
"}")
        self.stdn_payments.setCheckable(True)

        self.verticalLayout.addWidget(self.stdn_payments)

        self.stdn_trans = QPushButton(self.students_drp_dwn)
        self.stdn_trans.setObjectName(u"stdn_trans")
        self.stdn_trans.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.stdn_trans.setStyleSheet(u"QPushButton{\n"
"padding-left:22px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:#12b298;\n"
"cursor:pointer\n"
"}")
        self.stdn_trans.setCheckable(True)

        self.verticalLayout.addWidget(self.stdn_trans)


        self.verticalLayout_4.addWidget(self.students_drp_dwn)


        self.st_tc_fi_block_2.addWidget(self.students)

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
        icon10 = QIcon()
        icon10.addFile(u":/teachers3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10.addFile(u":/teachers4.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.teachers_2.setIcon(icon10)
        self.teachers_2.setIconSize(QSize(200, 60))
        self.teachers_2.setCheckable(True)
        self.teachers_2.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.teachers_2)

        self.teachers_drp_dwn = QFrame(self.teachers)
        self.teachers_drp_dwn.setObjectName(u"teachers_drp_dwn")
        self.teachers_drp_dwn.setFrameShape(QFrame.StyledPanel)
        self.teachers_drp_dwn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.teachers_drp_dwn)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.teacher_info = QPushButton(self.teachers_drp_dwn)
        self.teacher_info.setObjectName(u"teacher_info")
        self.teacher_info.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.teacher_info.setStyleSheet(u"QPushButton{\n"
"padding-left:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:#12b298;\n"
"cursor:pointer\n"
"}")
        self.teacher_info.setCheckable(True)

        self.verticalLayout_2.addWidget(self.teacher_info)

        self.teacher_salary = QPushButton(self.teachers_drp_dwn)
        self.teacher_salary.setObjectName(u"teacher_salary")
        self.teacher_salary.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.teacher_salary.setStyleSheet(u"QPushButton{\n"
"padding-left:-4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:#12b298;\n"
"cursor:pointer\n"
"}")
        self.teacher_salary.setCheckable(True)

        self.verticalLayout_2.addWidget(self.teacher_salary)

        self.teacher_trans = QPushButton(self.teachers_drp_dwn)
        self.teacher_trans.setObjectName(u"teacher_trans")
        self.teacher_trans.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.teacher_trans.setStyleSheet(u"QPushButton{\n"
"padding-left:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:#12b298;\n"
"cursor:pointer\n"
"}")
        self.teacher_trans.setCheckable(True)

        self.verticalLayout_2.addWidget(self.teacher_trans)


        self.verticalLayout_5.addWidget(self.teachers_drp_dwn)


        self.st_tc_fi_block_2.addWidget(self.teachers)

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
        icon11 = QIcon()
        icon11.addFile(u":/finances3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon11.addFile(u":/finances4.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.finance_2.setIcon(icon11)
        self.finance_2.setIconSize(QSize(200, 60))
        self.finance_2.setCheckable(True)
        self.finance_2.setAutoExclusive(False)

        self.verticalLayout_6.addWidget(self.finance_2)

        self.finance_drp_dwn = QFrame(self.finance)
        self.finance_drp_dwn.setObjectName(u"finance_drp_dwn")
        self.finance_drp_dwn.setFrameShape(QFrame.StyledPanel)
        self.finance_drp_dwn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.finance_drp_dwn)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.budgets = QPushButton(self.finance_drp_dwn)
        self.budgets.setObjectName(u"budgets")
        self.budgets.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.budgets.setStyleSheet(u"QPushButton{\n"
"padding-left:-43px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:#12b298;\n"
"cursor:pointer\n"
"}")
        self.budgets.setCheckable(True)

        self.verticalLayout_3.addWidget(self.budgets)

        self.expenses = QPushButton(self.finance_drp_dwn)
        self.expenses.setObjectName(u"expenses")
        self.expenses.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.expenses.setStyleSheet(u"QPushButton{\n"
"padding-left:-40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:#12b298;\n"
"cursor:pointer\n"
"}")
        self.expenses.setCheckable(True)

        self.verticalLayout_3.addWidget(self.expenses)

        self.busines_overview = QPushButton(self.finance_drp_dwn)
        self.busines_overview.setObjectName(u"busines_overview")
        self.busines_overview.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.busines_overview.setStyleSheet(u"QPushButton{\n"
"padding-left:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:#12b298;\n"
"cursor:pointer\n"
"}")
        self.busines_overview.setCheckable(True)

        self.verticalLayout_3.addWidget(self.busines_overview)


        self.verticalLayout_6.addWidget(self.finance_drp_dwn)


        self.st_tc_fi_block_2.addWidget(self.finance)


        self.verticalLayout_7.addLayout(self.st_tc_fi_block_2)

        self.verticalSpacer = QSpacerItem(20, 27, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.set_sig_blc_2 = QVBoxLayout()
        self.set_sig_blc_2.setSpacing(20)
        self.set_sig_blc_2.setObjectName(u"set_sig_blc_2")
        self.settings_2 = QPushButton(self.icon_text_widget)
        self.settings_2.setObjectName(u"settings_2")
        self.settings_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.settings_2.setStyleSheet(u"QPushButton{\n"
"padding-left:-70px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color:white;\n"
"border-radius:3px;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/settings2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon12.addFile(u":/settings1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings_2.setIcon(icon12)
        self.settings_2.setIconSize(QSize(100, 60))
        self.settings_2.setCheckable(True)
        self.settings_2.setAutoExclusive(True)

        self.set_sig_blc_2.addWidget(self.settings_2)

        self.signout_2 = QPushButton(self.icon_text_widget)
        self.signout_2.setObjectName(u"signout_2")
        self.signout_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.signout_2.setStyleSheet(u"QPushButton{\n"
"padding-left:-70px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color:white;\n"
"border-radius:3px;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/signout2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon13.addFile(u":/signout1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.signout_2.setIcon(icon13)
        self.signout_2.setIconSize(QSize(100, 60))
        self.signout_2.setCheckable(True)
        self.signout_2.setAutoExclusive(True)

        self.set_sig_blc_2.addWidget(self.signout_2)


        self.verticalLayout_7.addLayout(self.set_sig_blc_2)


        self.gridLayout.addWidget(self.icon_text_widget, 0, 1, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.header_widget = QWidget(self.widget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.header_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"border:none\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon14)
        self.pushButton.setIconSize(QSize(29, 35))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(15, 20, -1, 20)
        self.label = QLabel(self.header_widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label.setFont(font1)

        self.verticalLayout_9.addWidget(self.label)

        self.label_2 = QLabel(self.header_widget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"QLabel{\n"
"color:rgb(72, 72, 72)\n"
"}")

        self.verticalLayout_9.addWidget(self.label_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(343, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 20, -1)
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 31))
        self.lineEdit.setMaximumSize(QSize(16777215, 31))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"padding-left:15px;\n"
"border:1px solid gray;\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.label_3 = QLabel(self.header_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(40, 40))
        self.label_3.setPixmap(QPixmap(u":/profile.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_10.addWidget(self.header_widget)

        self.main_scr_widget = QWidget(self.widget)
        self.main_scr_widget.setObjectName(u"main_scr_widget")
        self.main_scr_widget.setMinimumSize(QSize(915, 741))
        self.main_scr_widget.setMaximumSize(QSize(841, 741))
        self.main_scr_widget.setStyleSheet(u"")
        self.stackedWidget = QStackedWidget(self.main_scr_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 9, 901, 741))
        self.stackedWidget.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(330, 310, 281, 141))
        font3 = QFont()
        font3.setPointSize(25)
        self.label_5.setFont(font3)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(260, 210, 281, 141))
        self.label_7.setFont(font3)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_8 = QLabel(self.page_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(310, 250, 281, 141))
        self.label_8.setFont(font3)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_9 = QLabel(self.page_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(320, 220, 281, 141))
        self.label_9.setFont(font3)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_10 = QLabel(self.page_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(270, 220, 341, 141))
        self.label_10.setFont(font3)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_11 = QLabel(self.page_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(290, 210, 281, 141))
        self.label_11.setFont(font3)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_12 = QLabel(self.page_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(300, 220, 281, 141))
        self.label_12.setFont(font3)
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.label_13 = QLabel(self.page_8)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(290, 220, 351, 141))
        self.label_13.setFont(font3)
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.label_14 = QLabel(self.page_9)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(320, 240, 281, 141))
        self.label_14.setFont(font3)
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.label_15 = QLabel(self.page_10)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(270, 240, 281, 141))
        self.label_15.setFont(font3)
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.label_16 = QLabel(self.page_11)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(270, 250, 301, 141))
        self.label_16.setFont(font3)
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.label_17 = QLabel(self.page_12)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(280, 230, 281, 141))
        self.label_17.setFont(font3)
        self.stackedWidget.addWidget(self.page_12)

        self.verticalLayout_10.addWidget(self.main_scr_widget)


        self.gridLayout.addLayout(self.verticalLayout_10, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stdn_2.toggled.connect(self.students_drp_dwn.hide)
        self.teachers_2.toggled.connect(self.teachers_drp_dwn.setHidden)
        self.finance_2.toggled.connect(self.finance_drp_dwn.setHidden)
        self.stdn_2.toggled.connect(self.students_drp_dwn.setHidden)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.instution_2.toggled.connect(self.instution_1.setChecked)
        self.stdn_2.toggled.connect(self.stdn_1.setChecked)
        self.teachers_2.toggled.connect(self.teachers_1.setChecked)
        self.finance_2.toggled.connect(self.finance_1.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.signout_2.toggled.connect(self.signout_1.setChecked)
        self.signout_1.toggled.connect(MainWindow.close)
        self.signout_2.toggled.connect(MainWindow.close)
        self.pushButton.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton.toggled.connect(self.icon_only_widget.setVisible)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.dashboard_1.setText("")
        self.instution_1.setText("")
        self.stdn_1.setText("")
        self.teachers_1.setText("")
        self.finance_1.setText("")
        self.settings_1.setText("")
        self.signout_1.setText("")
        self.logo.setText("")
        self.scholl_title.setText(QCoreApplication.translate("MainWindow", u"School", None))
        self.dashboard_2.setText("")
        self.instution_2.setText("")
        self.stdn_2.setText("")
        self.stdn_info.setText(QCoreApplication.translate("MainWindow", u"Student Information", None))
        self.stdn_payments.setText(QCoreApplication.translate("MainWindow", u"Student Payments", None))
        self.stdn_trans.setText(QCoreApplication.translate("MainWindow", u"Student Transactions", None))
        self.teachers_2.setText("")
        self.teacher_info.setText(QCoreApplication.translate("MainWindow", u"Teacher Information", None))
        self.teacher_salary.setText(QCoreApplication.translate("MainWindow", u"Teacher Salaries", None))
        self.teacher_trans.setText(QCoreApplication.translate("MainWindow", u"Student Transactions", None))
        self.finance_2.setText("")
        self.budgets.setText(QCoreApplication.translate("MainWindow", u"Budgets", None))
        self.expenses.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.busines_overview.setText(QCoreApplication.translate("MainWindow", u"Business Overview", None))
        self.settings_2.setText("")
        self.signout_2.setText("")
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hello, Ahmet!", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Welcome to your page.", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter keyword for search ...", None))
        self.label_3.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Institution", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Student Info", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Student Payments", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Student Transactions", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Teacher Info", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Teacher Salaries", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Teacher Transactions", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Budgets", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Business Overview", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

