# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reverse_timer_form1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import resorce_src_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(280, 231)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/my_foto.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 200, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 241, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(50, 125, 180, 41))
        self.pushButton_start.setObjectName("start")
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(50, 125, 180, 41))
        self.pushButton_stop.setObjectName("stop")
        self.pushButton_stop.hide()
        self.spinBox_sec = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_sec.setRange(0, 59)
        self.spinBox_sec.setGeometry(QtCore.QRect(196, 50, 70, 50))
        self.spinBox_sec.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_sec.setFont(font)
        self.spinBox_sec.setObjectName("spinBox_2")
        self.spinBox_min = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_min.setGeometry(QtCore.QRect(105, 50, 70, 50))
        self.spinBox_min.setRange(0, 59)
        self.spinBox_min.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_min.setFont(font)
        self.spinBox_min.setObjectName("spinBox")
        self.spinBox_hour = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_hour.setEnabled(True)
        self.spinBox_hour.setGeometry(QtCore.QRect(15, 50, 70, 50))
        self.spinBox_hour.setRange(0, 999)
        self.spinBox_hour.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_hour.setFont(font)
        self.spinBox_hour.setFrame(True)
        self.spinBox_hour.setObjectName("spinBox_3")
        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reverse Timer"))
        self.pushButton_start.setText(_translate("MainWindow", "start"))
        self.pushButton_stop.setText(_translate("MainWindow", "stop"))
        self.label.setText(_translate("MainWindow", "Krupeichenko Victor"))
        self.label_2.setText(_translate("MainWindow", "    hours"))
        self.label_3.setText(_translate("MainWindow", "     minutes"))
        self.label_4.setText(_translate("MainWindow", "       seconds"))
