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
        MainWindow.setEnabled(True)
        MainWindow.resize(704, 350)
        MainWindow.setMinimumSize(QtCore.QSize(704, 350))
        MainWindow.setMaximumSize(QtCore.QSize(704, 350))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStatusTip("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("#MainWindow {\n"
"background: gray;\n"
"}\n"
"QLineEdit {\n"
"padding: 0.5px;\n"
"border-style: solid;\n"
"\n"
"\n"
"background: lightgray;\n"
"}\n"
"\n"
"\n"
"QProgressBar {\n"
"\n"
"\n"
"\n"
"background: gray;\n"
"border-size=0px;\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: black;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #303232;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ff69b4,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: lightgray;\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover\n"
"{\n"
"    border: 1px solid #303232;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.streamRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.streamRadio.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.streamRadio.setChecked(True)
        self.streamRadio.setObjectName("streamRadio")
        self.alltracksRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.alltracksRadio.setGeometry(QtCore.QRect(91, 21, 115, 16))
        self.alltracksRadio.setObjectName("alltracksRadio")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 200, 111, 16))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 320, 681, 23))
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.logTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.logTextEdit.setGeometry(QtCore.QRect(10, 120, 421, 191))
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
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.logTextEdit.setFont(font)
        self.logTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logTextEdit.setReadOnly(True)
        self.logTextEdit.setPlainText("")
        self.logTextEdit.setObjectName("logTextEdit")
        self.urlText = QtWidgets.QLineEdit(self.centralwidget)
        self.urlText.setGeometry(QtCore.QRect(90, 40, 421, 20))
        self.urlText.setObjectName("urlText")
        self.go = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.go.setEnabled(True)
        self.go.setGeometry(QtCore.QRect(550, 40, 101, 41))
        palette = QtGui.QPalette()
        self.go.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.go.setFont(font)
        self.go.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.go.setAutoFillBackground(True)
        self.go.setIconSize(QtCore.QSize(40, 40))
        self.go.setObjectName("go")
        self.btnBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowse.setGeometry(QtCore.QRect(450, 90, 62, 21))
        self.btnBrowse.setFlat(False)
        self.btnBrowse.setObjectName("btnBrowse")
        self.pathText = QtWidgets.QLineEdit(self.centralwidget)
        self.pathText.setGeometry(QtCore.QRect(90, 90, 351, 20))
        self.pathText.setObjectName("pathText")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 70, 81, 16))
        self.label_3.setObjectName("label_3")
        self.cBox = QtWidgets.QCheckBox(self.centralwidget)
        self.cBox.setEnabled(True)
        self.cBox.setGeometry(QtCore.QRect(450, 120, 162, 17))
        self.cBox.setChecked(True)
        self.cBox.setObjectName("cBox")
        self.mp3Box = QtWidgets.QCheckBox(self.centralwidget)
        self.mp3Box.setEnabled(True)
        self.mp3Box.setGeometry(QtCore.QRect(450, 140, 167, 17))
        self.mp3Box.setObjectName("mp3Box")
        self.allfavsRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.allfavsRadio.setEnabled(True)
        self.allfavsRadio.setGeometry(QtCore.QRect(210, 20, 101, 16))
        self.allfavsRadio.setObjectName("allfavsRadio")
        self.playlistRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.playlistRadio.setEnabled(True)
        self.playlistRadio.setGeometry(QtCore.QRect(370, 20, 115, 16))
        self.playlistRadio.setObjectName("playlistRadio")
        self.rBox = QtWidgets.QCheckBox(self.centralwidget)
        self.rBox.setEnabled(True)
        self.rBox.setGeometry(QtCore.QRect(450, 160, 94, 17))
        self.rBox.setObjectName("rBox")
        self.gettokenButton = QtWidgets.QPushButton(self.centralwidget)
        self.gettokenButton.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.gettokenButton.setObjectName("gettokenButton")
        self.trackRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.trackRadio.setEnabled(True)
        self.trackRadio.setGeometry(QtCore.QRect(320, 20, 51, 16))
        self.trackRadio.setObjectName("trackRadio")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(450, 250, 81, 21))
        self.saveButton.setObjectName("saveButton")
        self.tokenText = QtWidgets.QLineEdit(self.centralwidget)
        self.tokenText.setGeometry(QtCore.QRect(450, 220, 241, 20))
        self.tokenText.setText("")
        self.tokenText.setObjectName("tokenText")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setEnabled(False)
        self.stopButton.setGeometry(QtCore.QRect(660, 50, 31, 23))
        self.stopButton.setObjectName("stopButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "scdl-qt :)"))
        self.streamRadio.setText(_translate("MainWindow", "My Stream"))
        self.alltracksRadio.setText(_translate("MainWindow", "All Tracks from URL"))
        self.label.setText(_translate("MainWindow", "sc token for stream dl"))
        self.urlText.setText(_translate("MainWindow", "https://soundcloud.com/"))
        self.go.setText(_translate("MainWindow", "Download"))
        self.btnBrowse.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "download folder"))
        self.cBox.setText(_translate("MainWindow", "Skip download if file exists"))
        self.mp3Box.setText(_translate("MainWindow", "Download mp3 only (128kbits)"))
        self.allfavsRadio.setText(_translate("MainWindow", "All Favs from URL"))
        self.playlistRadio.setText(_translate("MainWindow", "Playlist"))
        self.rBox.setText(_translate("MainWindow", "Ignore reposts"))
        self.gettokenButton.setText(_translate("MainWindow", "get sc token"))
        self.trackRadio.setText(_translate("MainWindow", "Track"))
        self.saveButton.setText(_translate("MainWindow", "save to config"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))

