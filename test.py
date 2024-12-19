import asyncio
import sys
import websockets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal


class WebSocketThread(QThread):
    message_received = pyqtSignal(str)

    def __init__(self, url):
        super().__init__()
        self.url = url
        self.running = True

    async def _run(self):
        async with websockets.connect(self.url) as websocket:
            while self.running:
                try:
                    message = await websocket.recv()
                    self.message_received.emit(message)
                except websockets.exceptions.ConnectionClosedOK:
                    break
                except Exception as e:
                    print(f"Error receiving message: {e}")
                    break

    def run(self):
        asyncio.run(self._run())

    def stop(self):
        self.running = False


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Real-Time Translation Overlay")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel("Waiting for translation...", self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

        self.websocket_thread = WebSocketThread(
            "ws://localhost:8000/ws")  # Replace with your backend URL
        self.websocket_thread.message_received.connect(self.update_text)
        self.websocket_thread.start()

    def update_text(self, text):
        self.label.setText(text)

    def closeEvent(self, event):
        self.websocket_thread.stop()
        self.websocket_thread.wait()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
