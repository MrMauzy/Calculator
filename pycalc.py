# pycalc.py

''' Making a calculator to learn how to use python with PyQt '''

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

WINDOW_SIZE = 235

class pyCalcWindow(QMainWindow):
    """Main Window"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Super Calc 2.0")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

def main():
    """Main Function"""
    calcApp = QApplication([])
    calcWindow = pyCalcWindow()
    calcWindow.show()
    sys.exit(calcApp.exec())


if __name__ == "__main__":
    main()
