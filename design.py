# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scdl-qt.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(705, 374)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tokenText = QtWidgets.QLineEdit(self.centralwidget)
        self.tokenText.setGeometry(QtCore.QRect(10, 330, 201, 20))
        self.tokenText.setText("")
        self.tokenText.setObjectName("tokenText")
        self.streamRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.streamRadio.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.streamRadio.setChecked(True)
        self.streamRadio.setObjectName("streamRadio")
        self.alltracksRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.alltracksRadio.setGeometry(QtCore.QRect(111, 11, 115, 16))
        self.alltracksRadio.setObjectName("alltracksRadio")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 310, 111, 16))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(220, 330, 471, 23))
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.logTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.logTextEdit.setGeometry(QtCore.QRect(10, 120, 501, 191))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.logTextEdit.setPalette(palette)
        self.logTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logTextEdit.setReadOnly(False)
        self.logTextEdit.setObjectName("logTextEdit")
        self.urlText = QtWidgets.QLineEdit(self.centralwidget)
        self.urlText.setGeometry(QtCore.QRect(221, 27, 391, 20))
        self.urlText.setObjectName("urlText")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(615, 26, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 111, 16))
        self.label_2.setObjectName("label_2")
        self.go = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.go.setGeometry(QtCore.QRect(580, 280, 111, 41))
        self.go.setObjectName("go")
        self.btnBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowse.setGeometry(QtCore.QRect(610, 90, 75, 23))
        self.btnBrowse.setObjectName("btnBrowse")
        self.pathText = QtWidgets.QLineEdit(self.centralwidget)
        self.pathText.setGeometry(QtCore.QRect(171, 91, 441, 20))
        self.pathText.setObjectName("pathText")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 90, 81, 16))
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setEnabled(False)
        self.checkBox.setGeometry(QtCore.QRect(521, 161, 162, 17))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setGeometry(QtCore.QRect(521, 184, 129, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setEnabled(False)
        self.checkBox_3.setGeometry(QtCore.QRect(521, 207, 167, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.allfavsRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.allfavsRadio.setEnabled(True)
        self.allfavsRadio.setGeometry(QtCore.QRect(111, 30, 115, 16))
        self.allfavsRadio.setObjectName("allfavsRadio")
        self.playlistRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.playlistRadio.setEnabled(True)
        self.playlistRadio.setGeometry(QtCore.QRect(111, 68, 115, 16))
        self.playlistRadio.setObjectName("playlistRadio")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setEnabled(False)
        self.checkBox_4.setGeometry(QtCore.QRect(521, 230, 94, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.gettokenButton = QtWidgets.QPushButton(self.centralwidget)
        self.gettokenButton.setGeometry(QtCore.QRect(10, 60, 75, 23))
        self.gettokenButton.setObjectName("gettokenButton")
        self.trackRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.trackRadio.setEnabled(True)
        self.trackRadio.setGeometry(QtCore.QRect(111, 49, 115, 16))
        self.trackRadio.setObjectName("trackRadio")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 140, 151, 16))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "scdl-qt :)"))
        self.streamRadio.setText(_translate("MainWindow", "My Stream"))
        self.alltracksRadio.setText(_translate("MainWindow", "All Tracks from URL"))
        self.label.setText(_translate("MainWindow", "sc token for stream dl"))
        self.logTextEdit.setPlainText(_translate("MainWindow", "coucou\n"
""))
        self.urlText.setText(_translate("MainWindow", "https://soundcloud.com/iamdjday/four-hills"))
        self.pushButton.setText(_translate("MainWindow", "Paste"))
        self.label_2.setText(_translate("MainWindow", "debug"))
        self.go.setText(_translate("MainWindow", "Download"))
        self.btnBrowse.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "download folder"))
        self.checkBox.setText(_translate("MainWindow", "Continue if file already exists"))
        self.checkBox_2.setText(_translate("MainWindow", "Add artist to file name"))
        self.checkBox_3.setText(_translate("MainWindow", "Download mp3 only (128kbits)"))
        self.allfavsRadio.setText(_translate("MainWindow", "All Favs from URL"))
        self.playlistRadio.setText(_translate("MainWindow", "Playlist"))
        self.checkBox_4.setText(_translate("MainWindow", "Ignore reposts"))
        self.gettokenButton.setText(_translate("MainWindow", "get sc token"))
        self.trackRadio.setText(_translate("MainWindow", "Track"))
        self.label_4.setText(_translate("MainWindow", "options not implemented yet"))

