# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(646, 541)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addshop = QtWidgets.QPushButton(self.centralwidget)
        self.addshop.setGeometry(QtCore.QRect(-10, 120, 661, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.addshop.setFont(font)
        self.addshop.setObjectName("addshop")
        self.addnewuser = QtWidgets.QPushButton(self.centralwidget)
        self.addnewuser.setGeometry(QtCore.QRect(-10, 210, 661, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.addnewuser.setFont(font)
        self.addnewuser.setObjectName("addnewuser")
        self.allorders = QtWidgets.QPushButton(self.centralwidget)
        self.allorders.setGeometry(QtCore.QRect(-10, 300, 661, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.allorders.setFont(font)
        self.allorders.setObjectName("allorders")
        self.shop_general = QtWidgets.QPushButton(self.centralwidget)
        self.shop_general.setGeometry(QtCore.QRect(-10, 390, 661, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.shop_general.setFont(font)
        self.shop_general.setObjectName("shop_general")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 20, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.backtologin = QtWidgets.QPushButton(self.centralwidget)
        self.backtologin.setGeometry(QtCore.QRect(10, 10, 91, 28))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.backtologin.setFont(font)
        self.backtologin.setObjectName("backtologin")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addshop.setText(_translate("MainWindow", "ADD NEW SHOP NAME"))
        self.addnewuser.setText(_translate("MainWindow", "ADD NEW USER NAME"))
        self.allorders.setText(_translate("MainWindow", "Veiw All Orders"))
        self.shop_general.setText(_translate("MainWindow", "Total Shops Payments"))
        self.label.setText(_translate("MainWindow", "Admin Panel"))
        self.backtologin.setText(_translate("MainWindow", "Back"))