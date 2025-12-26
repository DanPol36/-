from design import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from hypoviy_robot import RobotGui, StateManager, Logger, Statistics
import sys

class Controller:
    def __init__(self, ui):
        self.ui = ui
        self.root = RobotGui(ui)
        self.state = StateManager()
        self.logger = Logger()
        self.stats = Statistics()

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()  
    ui.setupUi(window)
    
    # Инициализация контроллера
    controller = Controller(ui)
    # Подключаем кнопки и прочие сигналы
    controller.root.power_on()
    
    # Показ окна
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
