# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homework.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1309, 714)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.NAME_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.NAME_LABEL.setGeometry(QtCore.QRect(20, 10, 821, 121))
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.NAME_LABEL.setFont(font)
        self.NAME_LABEL.setFrameShape(QtWidgets.QFrame.Panel)
        self.NAME_LABEL.setAlignment(QtCore.Qt.AlignCenter)
        self.NAME_LABEL.setObjectName("NAME_LABEL")
        self.MODE_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.MODE_LABEL.setGeometry(QtCore.QRect(50, 140, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.MODE_LABEL.setFont(font)
        self.MODE_LABEL.setObjectName("MODE_LABEL")
        self.MODE_1 = QtWidgets.QPushButton(self.centralwidget)
        self.MODE_1.setGeometry(QtCore.QRect(50, 200, 91, 61))
        self.MODE_1.setObjectName("MODE_1")
        self.MODE_1.clicked.connect(self.activate_mode_1)
        self.MODE_2 = QtWidgets.QPushButton(self.centralwidget)
        self.MODE_2.setGeometry(QtCore.QRect(50, 310, 93, 61))
        self.MODE_2.setObjectName("MODE_2")
        self.MODE_2.clicked.connect(self.activate_mode_2)
        self.MODE_3 = QtWidgets.QPushButton(self.centralwidget)
        self.MODE_3.setGeometry(QtCore.QRect(50, 420, 93, 61))
        self.MODE_3.setObjectName("MODE_3")
        self.MODE_3.clicked.connect(self.activate_mode_3)
        self.CONTROL_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.CONTROL_LABEL.setGeometry(QtCore.QRect(240, 140, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.CONTROL_LABEL.setFont(font)
        self.CONTROL_LABEL.setObjectName("CONTROL_LABEL")
        self.DEVICE_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.DEVICE_LABEL.setGeometry(QtCore.QRect(550, 140, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.DEVICE_LABEL.setFont(font)
        self.DEVICE_LABEL.setObjectName("DEVICE_LABEL")
        self.CHART_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.CHART_LABEL.setGeometry(QtCore.QRect(920, 110, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.CHART_LABEL.setFont(font)
        self.CHART_LABEL.setObjectName("CHART_LABEL")
        self.SENSOR_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.SENSOR_LABEL.setGeometry(QtCore.QRect(920, 400, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.SENSOR_LABEL.setFont(font)
        self.SENSOR_LABEL.setObjectName("SENSOR_LABEL")
        self.NAME_MSSV = QtWidgets.QLabel(self.centralwidget)
        self.NAME_MSSV.setGeometry(QtCore.QRect(10, 590, 691, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.NAME_MSSV.setFont(font)
        self.NAME_MSSV.setFrameShape(QtWidgets.QFrame.Panel)
        self.NAME_MSSV.setAlignment(QtCore.Qt.AlignCenter)
        self.NAME_MSSV.setObjectName("NAME_MSSV")
        self.CLEAR_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.CLEAR_BUTTON.setGeometry(QtCore.QRect(120, 530, 131, 51))
        self.CLEAR_BUTTON.setObjectName("CLEAR_BUTTON")
        self.CLEAR_BUTTON.clicked.connect(self.clear_all)
        self.EXIT_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.EXIT_BUTTON.setGeometry(QtCore.QRect(500, 530, 131, 51))
        self.EXIT_BUTTON.setObjectName("EXIT_BUTTON")
        self.EXIT_BUTTON.clicked.connect(quit)
        self.FAN_ON_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.FAN_ON_BUTTON.setGeometry(QtCore.QRect(220, 210, 81, 61))
        self.FAN_ON_BUTTON.setObjectName("FAN_ON_BUTTON")
        self.FAN_ON_BUTTON.clicked.connect(self.turn_fan_on)
        self.FAN_OFF_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.FAN_OFF_BUTTON.setGeometry(QtCore.QRect(320, 210, 81, 61))
        self.FAN_OFF_BUTTON.setObjectName("FAN_OFF_BUTTON")
        self.FAN_OFF_BUTTON.clicked.connect(self.turn_fan_off)
        self.LIGHT_SLIDER = QtWidgets.QSlider(self.centralwidget)
        self.LIGHT_SLIDER.setGeometry(QtCore.QRect(220, 330, 181, 51))
        self.LIGHT_SLIDER.setOrientation(QtCore.Qt.Horizontal)
        self.LIGHT_SLIDER.setObjectName("LIGHT_SLIDER")
        self.LIGHT_SLIDER.setMaximum(2)
        self.LIGHT_SLIDER.valueChanged.connect(self.update_light_image)
        self.OVEN_SWITCH = QtWidgets.QPushButton(self.centralwidget)
        self.OVEN_SWITCH.setGeometry(QtCore.QRect(240, 430, 151, 51))
        self.OVEN_SWITCH.setStyleSheet("")
        self.OVEN_SWITCH.setText("")
        self.OVEN_SWITCH.setIconSize(QtCore.QSize(80, 80))
        self.OVEN_SWITCH.setCheckable(True)
        self.OVEN_SWITCH.setObjectName("OVEN_SWITCH")
        self.OVEN_SWITCH.setIcon(QtGui.QIcon(":/device/switch_off.png"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/device/switch_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/device/switch_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.OVEN_SWITCH.clicked.connect(self.toggleOvenswitch)
        self.FAN_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.FAN_LABEL.setGeometry(QtCore.QRect(530, 200, 151, 81))
        self.FAN_LABEL.setStyleSheet("image: url(:/device/fan_off.png);")
        self.FAN_LABEL.setText("")
        self.FAN_LABEL.setObjectName("FAN_LABEL")
        self.LIGHT_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.LIGHT_LABEL.setGeometry(QtCore.QRect(530, 300, 151, 81))
        self.LIGHT_LABEL.setStyleSheet("image: url(:/device/tat.png);")
        self.LIGHT_LABEL.setText("")
        self.LIGHT_LABEL.setObjectName("LIGHT_LABEL")
        self.OVEN_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.OVEN_LABEL.setGeometry(QtCore.QRect(530, 410, 151, 81))
        self.OVEN_LABEL.setStyleSheet("image: url(:/device/oven_off.png);")
        self.OVEN_LABEL.setText("")
        self.OVEN_LABEL.setObjectName("OVEN_LABEL")
        self.BOX_DEVICE = QtWidgets.QGraphicsView(self.centralwidget)
        self.BOX_DEVICE.setGeometry(QtCore.QRect(500, 180, 211, 321))
        self.BOX_DEVICE.setObjectName("BOX_DEVICE")
        self.BOX_CONTROL = QtWidgets.QGraphicsView(self.centralwidget)
        self.BOX_CONTROL.setGeometry(QtCore.QRect(210, 180, 211, 321))
        self.BOX_CONTROL.setObjectName("BOX_CONTROL")
        self.BOX_MODE = QtWidgets.QGraphicsView(self.centralwidget)
        self.BOX_MODE.setGeometry(QtCore.QRect(30, 180, 131, 321))
        self.BOX_MODE.setObjectName("BOX_MODE")
        self.CHART_DISPLAY = QtWidgets.QWidget(self.centralwidget)
        self.CHART_DISPLAY.setGeometry(QtCore.QRect(740, 160, 531, 241))
        self.CHART_DISPLAY.setObjectName("CHART_DISPLAY")
        self.SENSOR_DISPLAY = QtWidgets.QWidget(self.centralwidget)
        self.SENSOR_DISPLAY.setGeometry(QtCore.QRect(740, 450, 551, 201))
        self.SENSOR_DISPLAY.setObjectName("SENSOR_DISPLAY")
        self.LOGO = QtWidgets.QLabel(self.centralwidget)
        self.LOGO.setGeometry(QtCore.QRect(1120, -10, 221, 141))
        self.LOGO.setStyleSheet("image: url(:/device/logo.png);")
        self.LOGO.setText("")
        self.LOGO.setObjectName("LOGO")
        self.BOX_MODE.raise_()
        self.BOX_CONTROL.raise_()
        self.BOX_DEVICE.raise_()
        self.NAME_LABEL.raise_()
        self.MODE_LABEL.raise_()
        self.MODE_1.raise_()
        self.MODE_2.raise_()
        self.MODE_3.raise_()
        self.CONTROL_LABEL.raise_()
        self.DEVICE_LABEL.raise_()
        self.CHART_LABEL.raise_()
        self.SENSOR_LABEL.raise_()
        self.NAME_MSSV.raise_()
        self.CLEAR_BUTTON.raise_()
        self.EXIT_BUTTON.raise_()
        self.FAN_ON_BUTTON.raise_()
        self.FAN_OFF_BUTTON.raise_()
        self.LIGHT_SLIDER.raise_()
        self.OVEN_SWITCH.raise_()
        self.FAN_LABEL.raise_()
        self.LIGHT_LABEL.raise_()
        self.OVEN_LABEL.raise_()
        self.CHART_DISPLAY.raise_()
        self.SENSOR_DISPLAY.raise_()
        self.LOGO.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1309, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.NAME_LABEL.setText(_translate("MainWindow", "PROJECT: ĐIỀU KHIỂN THIẾT BỊ"))
        self.MODE_LABEL.setText(_translate("MainWindow", "MODE"))
        self.MODE_1.setText(_translate("MainWindow", "1"))
        self.MODE_2.setText(_translate("MainWindow", "2"))
        self.MODE_3.setText(_translate("MainWindow", "3"))
        self.CONTROL_LABEL.setText(_translate("MainWindow", "CONTROL"))
        self.DEVICE_LABEL.setText(_translate("MainWindow", "DEVICE"))
        self.CHART_LABEL.setText(_translate("MainWindow", "CHART"))
        self.SENSOR_LABEL.setText(_translate("MainWindow", "SENSOR"))
        self.NAME_MSSV.setText(_translate("MainWindow", "TRẦN ĐỨC HƯỞNG - 22119186"))
        self.CLEAR_BUTTON.setText(_translate("MainWindow", "CLEAR"))
        self.EXIT_BUTTON.setText(_translate("MainWindow", "EXIT"))
        self.FAN_ON_BUTTON.setText(_translate("MainWindow", "ON"))
        self.FAN_OFF_BUTTON.setText(_translate("MainWindow", "OFF"))
    def turn_fan_on(self):
        self.FAN_LABEL.setStyleSheet("image: url(:/device/fan_on.png);")
    def turn_fan_off(self):
        self.FAN_LABEL.setStyleSheet("image: url(:/device/fan_off.png);")
    def update_light_image(self, value):
        if value == 0:
            self.LIGHT_LABEL.setStyleSheet("image: url(:/device/tat.png);")
        elif value == 1:
            self.LIGHT_LABEL.setStyleSheet("image: url(:/device/vua.png);")
        elif value == 2:
            self.LIGHT_LABEL.setStyleSheet("image: url(:/device/sang.png);")
    def toggleOvenswitch(self):
        if  self.OVEN_SWITCH.isChecked():
            self.OVEN_SWITCH.setIcon(QtGui.QIcon(":/device/switch_on.png"))
            self.OVEN_LABEL.setStyleSheet("image: url(:/device/oven_on.png);")
        else:
            self.OVEN_SWITCH.setIcon(QtGui.QIcon(":/device/switch_off.png"))
            self.OVEN_LABEL.setStyleSheet("image: url(:/device/oven_off.png);")
    def activate_mode_1(self):
        self.FAN_ON_BUTTON.click()
        self.LIGHT_SLIDER.setValue(1)
        if self.OVEN_SWITCH.isChecked():
            self.OVEN_SWITCH.click()
    def activate_mode_2(self):
        self.FAN_OFF_BUTTON.click()
        self.LIGHT_SLIDER.setValue(2)
        if not self.OVEN_SWITCH.isChecked():
            self.OVEN_SWITCH.click()
    def activate_mode_3(self):
        self.FAN_ON_BUTTON.click()
        self.LIGHT_SLIDER.setValue(2)
        if not self.OVEN_SWITCH.isChecked():
            self.OVEN_SWITCH.click()
    def clear_all(self):
        self.LIGHT_LABEL.setStyleSheet("image: url(:/device/tat.png);")
        self.FAN_LABEL.setStyleSheet("image: url(:/device/fan_off.png);")
        self.OVEN_LABEL.setStyleSheet("image: url(:/device/oven_off.png);")
        self.LIGHT_SLIDER.setValue(0)
        self.OVEN_SWITCH.setChecked(False)
        self.OVEN_SWITCH.setIcon(QtGui.QIcon(":/device/switch_off.png"))
import image


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
