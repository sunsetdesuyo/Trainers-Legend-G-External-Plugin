# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_config.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1036, 741)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 1011, 721))
        self.groupBox.setObjectName("groupBox")
        self.scrollArea_config = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea_config.setGeometry(QtCore.QRect(20, 30, 971, 621))
        self.scrollArea_config.setWidgetResizable(True)
        self.scrollArea_config.setObjectName("scrollArea_config")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 969, 619))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea_config.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_save = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_save.setGeometry(QtCore.QRect(435, 660, 141, 51))
        self.pushButton_save.setObjectName("pushButton_save")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(587, 680, 411, 31))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "config - Trainers-Legend-G"))
        self.groupBox.setTitle(_translate("MainWindow", "Config settings"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.label.setText(_translate("MainWindow", "* Effective after restarting the game."))
