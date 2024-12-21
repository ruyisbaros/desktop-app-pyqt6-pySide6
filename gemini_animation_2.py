import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *  # Import for QIcon (if needed)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load UI from Designer
        self.ui = loadUi("your_ui_file.ui", self)  # Replace with your .ui file

        # Assuming 'sidebarWidget' is the object name of your sidebar in Designer
        self.sidebar = self.ui.sidebarWidget
        self.sidebar_width = self.sidebar.width()  # Store original width

        # Create animation
        self.animation = QPropertyAnimation(self.sidebar, b"geometry")
        self.animation.setDuration(200)  # Adjust duration as needed
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)

        # Connect toggle button (assuming its object name is 'toggleButton')
        self.ui.toggleButton.clicked.connect(self.toggle_sidebar)

        self.sidebar_open = True  # Initial state: open

    def toggle_sidebar(self):
        if self.sidebar_open:  # Close sidebar (slide left)
            start_rect = self.sidebar.geometry()
            end_rect = QRect(-self.sidebar_width, start_rect.y(),
                             self.sidebar_width, start_rect.height())
        else:  # Open sidebar (slide right)
            start_rect = self.sidebar.geometry()
            end_rect = QRect(0, start_rect.y(),
                             self.sidebar_width, start_rect.height())

        self.animation.setStartValue(start_rect)
        self.animation.setEndValue(end_rect)
        self.animation.start()

        self.sidebar_open = not self.sidebar_open


# ... (rest of your code) ...

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
