from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
import mysql.connector

from ui_index import Ui_MainWindow


class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Sidebar Menu")

    # Hide icon only widget initially
        self.icon_only_widget.setHidden(True)
    # Hide dropdown menus hidden initially
        self.students_dropdown.setHidden(True)
        self.teachers_dropdown.setHidden(True)
        self.finances_dropdown.setHidden(True)

    # Connect buttons with stack pages
        self.dashboard_1.clicked.connect(self.switch_to_dashboard_page)
        self.dashboard_2.clicked.connect(self.switch_to_dashboard_page)

        self.institution_1.clicked.connect(self.switch_to_institution_page)
        self.institution_2.clicked.connect(self.switch_to_institution_page)

        self.student_info.clicked.connect(self.switch_to_studentInfo_page)
        self.student_payment.clicked.connect(
            self.switch_to_studentPayments_page)
        self.student_trans.clicked.connect(
            self.switch_to_studentTransactions_page)

        self.teacher_info.clicked.connect(self.switch_to_teacherInfo_page)
        self.teachers_salary.clicked.connect(self.switch_to_teacherSalary_page)
        self.teacher_trans.clicked.connect(
            self.switch_to_teacherTransactions_page)

        self.budget.clicked.connect(self.switch_to_budget_page)
        self.expenses.clicked.connect(self.switch_to_expenses_page)
        self.business_overview.clicked.connect(
            self.switch_to_businessOverview_page)

        self.settings_1.clicked.connect(self.switch_to_settings_page)
        self.settings_2.clicked.connect(self.switch_to_settings_page)

        # Custom btn functions
        self.student_1.clicked.connect(self.show_student_context_menu)
        self.teachers_1.clicked.connect(self.show_teacher_context_menu)
        self.finance_1.clicked.connect(self.show_finance_context_menu)

        # Trigger database connection
        self.create_connection()
        # Create tables
        self.create_tables()
    # switch between stack pages

    def switch_to_dashboard_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_institution_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_studentInfo_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_studentPayments_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_studentTransactions_page(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_teacherInfo_page(self):
        self.stackedWidget.setCurrentIndex(5)

    def switch_to_teacherSalary_page(self):
        self.stackedWidget.setCurrentIndex(6)

    def switch_to_teacherTransactions_page(self):
        self.stackedWidget.setCurrentIndex(7)

    def switch_to_budget_page(self):
        self.stackedWidget.setCurrentIndex(8)

    def switch_to_expenses_page(self):
        self.stackedWidget.setCurrentIndex(9)

    def switch_to_businessOverview_page(self):
        self.stackedWidget.setCurrentIndex(10)

    def switch_to_settings_page(self):
        self.stackedWidget.setCurrentIndex(11)

    # METHODS TO SHOW CONTEXT MENUS
    def show_student_context_menu(self):
        self.show_custom_context_menu(
            self.student_1, ["Student Information", "Student Payment", "Student Transaction"])

    def show_teacher_context_menu(self):
        self.show_custom_context_menu(self.teachers_1, [
                                      "Teacher Information", "Teacher Salary", "Teacher Transaction"])

    def show_finance_context_menu(self):
        self.show_custom_context_menu(self.finance_1, [
                                      "Budget", "Expenses", "Business Overview"])

    def show_custom_context_menu(self, btn, menu_items):
        menu = QMenu(self)
        # set style for menu
        menu.setStyleSheet("""
                         QMenu { 
                         background-color: black; 
                         color:  white; 
                         }
                         QMenu:selected { 
                         background-color: white; 
                         color: #12b298;
                         }
                           """)
        for item_text in menu_items:
            action = QAction(item_text, self)
            action.triggered.connect(self.handle_menu_item_click)
            menu.addAction(action)
        # set Menu position
        menu.move(btn.mapToGlobal(btn.rect().topRight()))
        menu.exec()

    def handle_menu_item_click(self):
        text = self.sender().text()
        if text == "Student Information":
            self.switch_to_studentInfo_page()
        elif text == "Student Payment":
            self.switch_to_studentPayments_page()
        elif text == "Student Transaction":
            self.switch_to_studentTransactions_page()
        elif text == "Teacher Information":
            self.switch_to_teacherInfo_page()
        elif text == "Teacher Salary":
            self.switch_to_teacherSalary_page()
        elif text == "Teacher Transaction":
            self.switch_to_teacherTransactions_page()
        elif text == "Budget":
            self.switch_to_budget_page()
        elif text == "Expenses":
            self.switch_to_expenses_page()
        elif text == "Business Overview":
            self.switch_to_businessOverview_page()

    # CREATE DATABASE CONNECTION
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

    # CREATE TABLES
    def create_tables(self):
        cursor = self.mydb.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY,
                names TEXT NOT NULL,
                email TEXT NOT NULL,
                gender TEXT NOT NULL,
                birthday TEXT NOT NULL,
                address TEXT NOT NULL,
                phone_number TEXT NOT NULL,
                age INT ,
                grade TEXT NOT NULL
            );
        """)

        self.mydb.commit()
        print("Tables created successfully")
        self.mydb.close()

    def open_create_student_dialog(self):
        from studentDialog import Ui_StudentsDialog
        dialog = Ui_StudentsDialog(self)
        result = dialog.exec()

        if result == Ui_StudentsDialog.accepted:
            pass
