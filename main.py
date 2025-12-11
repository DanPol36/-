from design import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from hypoviy_robot import RobotGui, StateManager, Logger, Statistics
import sys
import threading

class Controller:
    # контроллер
    def init(self, ui):
        self.ui = ui
        self.robot = RobotGui()
        self.state = StateManager()
        self.logger = Logger()
        self.stats = Statistics()
        self.connect_buttons()

def main():
    # запуск Qt
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    # создание контроллера
    controller = Controller(ui)

    # показ окна
    window.show()
    sys.exit(app.exec_())


if __name__ == "main":
    main()