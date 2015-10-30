# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
import design
import sys
import os
import time
import logging


        
class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.btnBrowse.clicked.connect(self.browse_folder)
        self.pathText.setText(os.environ['UserProfile']+'\Desktop\scdl')
        self.myThread = T1()
        w = T1()
        self.myThread.notifyProgress.connect(self.onProgress)
        w.moveToThread(self.myThread)
        self.myThread.start() 
        log_handler = logme(self.logTextEdit)
        logging.getLogger().addHandler(log_handler)
        
    def browse_folder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                           "Pick a folder")
        # execute getExistingDirectory dialog and set the directory variable 
        self.pathText.setText(directory)
        
    def onProgress(self, i):
        self.progressBar.setValue(self.progressBar.value()+1)
       
class T1(QThread):
    notifyProgress = QtCore.pyqtSignal(int)
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        for i in range(10):
            self.notifyProgress.emit(i) #progress bar +1
            time.sleep(0.1)
            #logme.emit('Offset should be an Integer...',  '1')
        self.finished.emit()
        
class logme(logging.Handler):
    def __init__(self, parent):
        super(logme, self).__init__()

        self.widget = parent
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.insertPlainText()(msg)

    def write(self, m):
        pass

def main():
        app = QtWidgets.QApplication(sys.argv)
        form = ExampleApp()
        form.show()
        app.exec_()
        


        
if __name__ == "__main__":
        main()
