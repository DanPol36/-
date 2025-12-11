#import sys
#from PyQt5 import QtWidgets

#from interface import Ui_MainWindow 

class RobotGui:
    # заглушка с функциями под будущее управление и подвязку кнопок

    def power_on(self):
        while True:
            print(1)
        # pass

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

    def init(self):
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
    def init(self, path="logs.txt"):
        self.path = path

    def write(self, text):
        pass


class Statistics:
    # cтата
    def init(self):
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