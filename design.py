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
        self.streamRadio.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.streamRadio.setChecked(True)
        self.streamRadio.setObjectName("streamRadio")
        self.alltracksRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.alltracksRadio.setGeometry(QtCore.QRect(101, 11, 115, 16))
        self.alltracksRadio.setObjectName("alltracksRadio")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 210, 151, 16))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 310, 681, 23))
        font = QtGui.QFont()
        font.setKerning(True)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("")
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.urlText = QtWidgets.QLineEdit(self.centralwidget)
        self.urlText.setGeometry(QtCore.QRect(100, 30, 411, 21))
        self.urlText.setObjectName("urlText")
        self.go = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.go.setEnabled(True)
        self.go.setGeometry(QtCore.QRect(550, 30, 101, 41))
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
        self.btnBrowse.setGeometry(QtCore.QRect(450, 70, 62, 21))
        self.btnBrowse.setFlat(False)
        self.btnBrowse.setObjectName("btnBrowse")
        self.pathText = QtWidgets.QLineEdit(self.centralwidget)
        self.pathText.setGeometry(QtCore.QRect(100, 70, 341, 20))
        self.pathText.setObjectName("pathText")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.label_3.setObjectName("label_3")
        self.cBox = QtWidgets.QCheckBox(self.centralwidget)
        self.cBox.setEnabled(True)
        self.cBox.setGeometry(QtCore.QRect(450, 117, 190, 17))
        self.cBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cBox.setChecked(False)
        self.cBox.setAutoRepeat(False)
        self.cBox.setObjectName("cBox")
        self.mp3Box = QtWidgets.QCheckBox(self.centralwidget)
        self.mp3Box.setEnabled(True)
        self.mp3Box.setGeometry(QtCore.QRect(450, 160, 167, 17))
        self.mp3Box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mp3Box.setAutoRepeat(False)
        self.mp3Box.setObjectName("mp3Box")
        self.allfavsRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.allfavsRadio.setEnabled(True)
        self.allfavsRadio.setGeometry(QtCore.QRect(220, 10, 131, 16))
        self.allfavsRadio.setChecked(False)
        self.allfavsRadio.setObjectName("allfavsRadio")
        self.playlistRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.playlistRadio.setEnabled(True)
        self.playlistRadio.setGeometry(QtCore.QRect(400, 10, 115, 16))
        self.playlistRadio.setObjectName("playlistRadio")
        self.rBox = QtWidgets.QCheckBox(self.centralwidget)
        self.rBox.setEnabled(True)
        self.rBox.setGeometry(QtCore.QRect(450, 180, 94, 17))
        self.rBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rBox.setAutoRepeat(False)
        self.rBox.setObjectName("rBox")
        self.gettokenButton = QtWidgets.QPushButton(self.centralwidget)
        self.gettokenButton.setGeometry(QtCore.QRect(10, 30, 81, 31))
        self.gettokenButton.setObjectName("gettokenButton")
        self.trackRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.trackRadio.setEnabled(True)
        self.trackRadio.setGeometry(QtCore.QRect(350, 10, 51, 16))
        self.trackRadio.setObjectName("trackRadio")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(600, 260, 91, 31))
        self.saveButton.setObjectName("saveButton")
        self.tokenText = QtWidgets.QLineEdit(self.centralwidget)
        self.tokenText.setGeometry(QtCore.QRect(450, 230, 241, 20))
        self.tokenText.setText("")
        self.tokenText.setObjectName("tokenText")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setEnabled(False)
        self.stopButton.setGeometry(QtCore.QRect(660, 30, 41, 41))
        self.stopButton.setObjectName("stopButton")
        self.logTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.logTextEdit.setGeometry(QtCore.QRect(10, 100, 431, 211))
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
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.logTextEdit.setFont(font)
        self.logTextEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.logTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logTextEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.logTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.logTextEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.logTextEdit.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.logTextEdit.setReadOnly(True)
        self.logTextEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.logTextEdit.setObjectName("logTextEdit")
        self.speedLabel = QtWidgets.QLabel(self.centralwidget)
        self.speedLabel.setGeometry(QtCore.QRect(360, 290, 81, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.speedLabel.setPalette(palette)
        self.speedLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.speedLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.speedLabel.setObjectName("speedLabel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 100, 47, 13))
        self.label_2.setObjectName("label_2")
        self.sBox = QtWidgets.QCheckBox(self.centralwidget)
        self.sBox.setEnabled(True)
        self.sBox.setGeometry(QtCore.QRect(450, 140, 190, 17))
        self.sBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sBox.setChecked(True)
        self.sBox.setAutoRepeat(False)
        self.sBox.setObjectName("sBox")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "scdl-qt :)"))
        self.streamRadio.setText(_translate("MainWindow", "My Stream"))
        self.alltracksRadio.setText(_translate("MainWindow", "All Tracks from URL"))
        self.label.setText(_translate("MainWindow", "sc token for stream download"))
        self.urlText.setText(_translate("MainWindow", "https://soundcloud.com/rafi-ki"))
        self.go.setText(_translate("MainWindow", "Download"))
        self.btnBrowse.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "download folder:"))
        self.cBox.setText(_translate("MainWindow", "Stop download if file already exists"))
        self.mp3Box.setText(_translate("MainWindow", "Download mp3 only (128kbits)"))
        self.allfavsRadio.setText(_translate("MainWindow", "All Favorites from URL"))
        self.playlistRadio.setText(_translate("MainWindow", "Playlist"))
        self.rBox.setText(_translate("MainWindow", "Ignore reposts"))
        self.gettokenButton.setText(_translate("MainWindow", "get sc token"))
        self.trackRadio.setText(_translate("MainWindow", "Track"))
        self.saveButton.setText(_translate("MainWindow", "save to config"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.speedLabel.setText(_translate("MainWindow", "0KB/s"))
        self.label_2.setText(_translate("MainWindow", "Settings:"))
        self.sBox.setText(_translate("MainWindow", "Skip if file exists"))

