# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
import design
import sys
import os
import time
import json
import logging
import signal
import urllib.request
import warnings
import configparser
import mutagen
import wget
from docopt import docopt
from requests.exceptions import HTTPError

from scdl import __version__
from scdl import soundcloud, utils

logging.basicConfig(level=logging.INFO, format='%(message)s')
logging.getLogger('urllib3.connectionpool').setLevel(logging.ERROR)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addFilter(utils.ColorizeFilter())
logger.newline = print
scdl_client_id = '95a4c0ef214f2a4a0852142807b54b35'
client = soundcloud.Client(client_id=scdl_client_id)
token = ''


        
class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.btnBrowse.clicked.connect(self.browse_folder)
        self.pathText.setText(os.environ['UserProfile']+'\Desktop\scdl')
        self.myThread = T1()
        self.myThread.notifyProgress.connect(self.onProgress)
        self.myThread.start() 
        self.Tget_item = T_get_item()
        self.Tget_item.notifyProgress.connect(self.onProgress)
        self.urlText.returnPressed.connect(self.onURLChange)
        
        
        
    def browse_folder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                           "Pick a folder")
        # execute getExistingDirectory dialog and set the directory variable 
        self.pathText.setText(directory)
        
    def onProgress(self, i):
        self.progressBar.setValue(self.progressBar.value()+1)
    def onURLChange(self):
        self.Tget_item.start(self.urlText.text())      
       
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
        self.finished.emit()
        
class T_get_item(QThread): 
    notifyProgress = QtCore.pyqtSignal(str)
    def __init__(self,  url):
        QThread.__init__(self)

    def __del__(self):
        self.wait()
        
    def _get_item(track_url):
        """
        Fetches metadata for an track or playlist
        """

        try:
            item = client.get('/resolve', url=track_url)
        except Exception:
            logger.error('Error resolving url {0}, retrying...'.format(track_url))
            time.sleep(5)
            try:
                item = client.get('/resolve', url=track_url)
            except Exception as e:
                logger.error('Could not resolve url {0}'.format(track_url))
                logger.exception(e)
                sys.exit(0)
        return item
    def run(self,  url):
        #global url
        self._get_item(url)
        for i in range(10):
            self.notifyProgress.emit(1,  'test') #1progress bar +1
            time.sleep(0.1)
        self.finished.emit()
        
def main():
        app = QtWidgets.QApplication(sys.argv)
        form = ExampleApp()
        form.show()
        app.exec_()
        


        
if __name__ == "__main__":
        main()
