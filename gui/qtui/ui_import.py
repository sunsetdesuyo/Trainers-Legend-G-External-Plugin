from . import main_ui, ui_config, ui_rpc
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget


class MainUI(main_ui.Ui_MainWindow, QWidget):
    def __init__(self):
        super(MainUI, self).__init__()

    def setupUi(self, MainWindow):
        super(MainUI, self).setupUi(MainWindow)
        MainWindow.setFixedSize(MainWindow.rect().width(), MainWindow.rect().height())


class ConfigUI(ui_config.Ui_MainWindow, QWidget):
    def __init__(self):
        super(ConfigUI, self).__init__()

    def setupUi(self, MainWindow):
        super(ConfigUI, self).setupUi(MainWindow)
        MainWindow.setFixedSize(MainWindow.rect().width(), MainWindow.rect().height())


class RPCUI(ui_rpc.Ui_MainWindow, QWidget):
    def __init__(self):
        super(RPCUI, self).__init__()

    def setupUi(self, MainWindow):
        super(RPCUI, self).setupUi(MainWindow)
        MainWindow.setFixedSize(MainWindow.rect().width(), MainWindow.rect().height())
