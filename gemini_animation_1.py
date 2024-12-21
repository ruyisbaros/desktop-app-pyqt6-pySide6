from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # ... your other UI setup ...

        self.sidebar = QWidget()  # Replace with your sidebar widget
        self.sidebar.setFixedWidth(200)  # Initial width

        # Create the animation
        self.animation = QPropertyAnimation(
            self.sidebar, b"geometry")  # Animate the geometry
        self.animation.setDuration(200)  # Animation duration in milliseconds
        self.animation.setEasingCurve(
            QEasingCurve.InOutCubic)  # Smooth easing curve

        self.toggleButton = QPushButton("Toggle Sidebar")  # Your toggle button
        self.toggleButton.clicked.connect(self.toggle_sidebar)

        # ... add sidebar and toggle button to your layout ...

    def toggle_sidebar(self):
        current_width = self.sidebar.width()
        if current_width > 0:  # Sidebar is open, close it
            self.animation.setStartValue(self.sidebar.geometry())
            self.animation.setEndValue(
                QRect(self.sidebar.x(), self.sidebar.y(), 0, self.sidebar.height()))
        else:  # Sidebar is closed, open it
            self.animation.setStartValue(self.sidebar.geometry())
            self.animation.setEndValue(QRect(self.sidebar.x(), self.sidebar.y(
            ), 200, self.sidebar.height()))  # Restore to original width

        self.animation.start()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
