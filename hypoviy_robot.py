# import sys
# from PyQt5 import QtWidgets
# from design import Ui_MainWindow

class RobotGui():
    # заглушка с функциями под будущее управление и подвязку кнопок
    def __init__(self, ui=None):
        self.ui = ui

    def power_on(self):
        if not hasattr(self, "ui") or self.ui is None:
            return
        self.ui.pushButton.clicked.connect(lambda: print(1))
        print(1)

    def power_off(self):
        pass

    def pause(self):
        pass

    def emergency_stop(self):
        pass

    def go_home(self):
        pass

    def move_l(self, dx=0, dy=0, dz=0, drx=0, dry=0, drz=0):
        pass

    def move_j(self, joints):
        pass

    def gopen(self):
        pass

    def gclose(self):
        pass

    def con(self):
        pass

    def coff(self):
        pass

    def linear_move(self, delta):
        pass


class StateManager:
    # состояние программы
    IDLE = "IDLE"
    RUNNING = "RUNNING"
    PAUSED = "PAUSED"
    ESTOP = "ESTOP"
    MANUAL = "MANUAL"

    def __init__(self):
        self.state = self.IDLE
        self.manual_enabled = False

    def set(self, st):
        self.state = st

    def enablem(self):
        self.manual_enabled = True
        self.set(self.MANUAL)

    def disablem(self):
        self.manual_enabled = False
        self.set(self.IDLE)


class Logger:
    # логгер
    def __init__(self, path="logs.txt"):
        self.path = path

    def write(self, text):
        pass


class Statistics:
    # cтата
    def __init__(self):
        self.categories = [
            {"name": "A", "count": 0},
            {"name": "B", "count": 0},
            {"name": "C", "count": 0},
            {"name": "Reject", "count": 0},
        ]

    def increment(self, index):
        self.categories[index]["count"] += 1

    def save(self, path):
        pass

# Знакомый код?))) так как это шаблон не постеснялся использовать, в будущем понятное дело буду под себя менять, пока пусть так побудет
