# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.btn_botnet_none = QtWidgets.QPushButton(self.centralWidget)
        self.btn_botnet_none.setGeometry(QtCore.QRect(360, 10, 60, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.btn_botnet_none.setFont(font)
        self.btn_botnet_none.setObjectName("btn_botnet_none")
        self.btn_botnet_all = QtWidgets.QPushButton(self.centralWidget)
        self.btn_botnet_all.setGeometry(QtCore.QRect(280, 10, 60, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.btn_botnet_all.setFont(font)
        self.btn_botnet_all.setObjectName("btn_botnet_all")
        self.slider_synflood = QtWidgets.QSlider(self.centralWidget)
        self.slider_synflood.setGeometry(QtCore.QRect(500, 50, 20, 200))
        self.slider_synflood.setOrientation(QtCore.Qt.Vertical)
        self.slider_synflood.setObjectName("slider_synflood")
        self.slider_httpflood = QtWidgets.QSlider(self.centralWidget)
        self.slider_httpflood.setGeometry(QtCore.QRect(620, 50, 20, 200))
        self.slider_httpflood.setOrientation(QtCore.Qt.Vertical)
        self.slider_httpflood.setObjectName("slider_httpflood")
        self.slider_slowloris = QtWidgets.QSlider(self.centralWidget)
        self.slider_slowloris.setGeometry(QtCore.QRect(740, 50, 20, 200))
        self.slider_slowloris.setOrientation(QtCore.Qt.Vertical)
        self.slider_slowloris.setObjectName("slider_slowloris")
        self.btn_set = QtWidgets.QPushButton(self.centralWidget)
        self.btn_set.setGeometry(QtCore.QRect(670, 270, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.btn_set.setFont(font)
        self.btn_set.setObjectName("btn_set")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(420, 10, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(540, 10, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(660, 10, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(450, 230, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(450, 50, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(570, 230, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(570, 50, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(690, 230, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(690, 50, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.btn_status = QtWidgets.QPushButton(self.centralWidget)
        self.btn_status.setGeometry(QtCore.QRect(670, 500, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.btn_status.setFont(font)
        self.btn_status.setObjectName("btn_status")
        self.btn_botnet_load = QtWidgets.QPushButton(self.centralWidget)
        self.btn_botnet_load.setGeometry(QtCore.QRect(200, 10, 60, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.btn_botnet_load.setFont(font)
        self.btn_botnet_load.setObjectName("btn_botnet_load")
        self.line_botnet_path = QtWidgets.QLineEdit(self.centralWidget)
        self.line_botnet_path.setGeometry(QtCore.QRect(20, 10, 160, 40))
        self.line_botnet_path.setObjectName("line_botnet_path")
        self.tab_botnet = QtWidgets.QTableWidget(self.centralWidget)
        self.tab_botnet.setGeometry(QtCore.QRect(20, 60, 400, 480))
        self.tab_botnet.setObjectName("tab_botnet")
        self.tab_botnet.setColumnCount(0)
        self.tab_botnet.setRowCount(0)
        self.tab_status = QtWidgets.QTableWidget(self.centralWidget)
        self.tab_status.setGeometry(QtCore.QRect(470, 360, 300, 120))
        self.tab_status.setObjectName("tab_status")
        self.tab_status.setColumnCount(0)
        self.tab_status.setRowCount(0)
        self.btn_target = QtWidgets.QPushButton(self.centralWidget)
        self.btn_target.setGeometry(QtCore.QRect(550, 270, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.btn_target.setFont(font)
        self.btn_target.setObjectName("btn_target")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 17))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_botnet_none.setText(_translate("MainWindow", "None"))
        self.btn_botnet_all.setText(_translate("MainWindow", "All"))
        self.btn_set.setText(_translate("MainWindow", "Set"))
        self.label.setText(_translate("MainWindow", "SYNFlood"))
        self.label_2.setText(_translate("MainWindow", "HTTPFlood"))
        self.label_3.setText(_translate("MainWindow", "Slowloris"))
        self.label_4.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "1000"))
        self.label_6.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "300"))
        self.label_8.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "300"))
        self.btn_status.setText(_translate("MainWindow", "Status"))
        self.btn_botnet_load.setText(_translate("MainWindow", "Load"))
        self.btn_target.setText(_translate("MainWindow", "Target"))

