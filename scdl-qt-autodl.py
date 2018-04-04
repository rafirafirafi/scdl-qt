# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, QCoreApplication, QByteArray, QPropertyAnimation
import design
import sys
import os
import time
import json
import logging
import webbrowser
import urllib.request
import warnings
import configparser
import mutagen
import urllib
import soundcloud
import re
from requests.exceptions import HTTPError
import requests
requests.packages.urllib3.disable_warnings()

#from scdl import __version__
#from scdl import soundcloud, utils
from urllib.request import urlopen


scdl_client_id = '95a4c0ef214f2a4a0852142807b54b35'
client = soundcloud.Client(client_id=scdl_client_id)


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.btnBrowse.clicked.connect(self.browse_folder)
        self.gettokenButton.clicked.connect(self.gettoken)
        self.saveButton.clicked.connect(self.saveconfig)
        self.stopButton.clicked.connect(self.stop)
        self.go.setEnabled(True)
        self.stopButton.setEnabled(False)
        self.go.clicked.connect(self.handleButton)


        self._get_config()
        options = ''
        self.stopButton.setEnabled(True)
        if self.cBox.isChecked():
            options=options+'c'
        if self.rBox.isChecked():
            options=options+'r'
        if self.mp3Box.isChecked():
            options=options+'m'
        if self.sBox.isChecked():
            options=options+'s'
        self.go.setEnabled(False)
        type_dl = ''
        if self.streamRadio.isChecked() is False:
            if not re.match('(?:https?:\/\/)?(?:www\.?)?soundcloud\.com((?=([^a-z 0-9]))([^\s])*|)',self.urlText.text()):
                self.logTextEdit.insertHtml('not soundcloud URL<br>')
                self.go.setEnabled(True)
                return
        if self.streamRadio.isChecked() is True:
            type_dl='stream'
            pattern = re.compile("^\w-\w\w\w\w\w\w-*")
            if pattern.match(self.tokenText.text()):
                self.Tget_item = T_get_item(self.urlText.text(), self.pathText.text(), self.tokenText.text(), type_dl, self.progressBar, options) #type_dl : 
                self.Tget_item.console.connect(self.onProgress)
                self.Tget_item.start() 
            else:
                self.logTextEdit.insertHtml('Token doesnt look valid.... Valid token is like : 1-126000-000707-50006e52ef30d000. Click on get sc token<br>')
                self.go.setEnabled(True)
        elif self.allfavsRadio.isChecked() is True:
            type_dl='f'
            if not re.match('http.?://(?:www)?(?:[\w-]{2,255}(?:\.\w{2,6}){1,2})(?:/[\w&%?#-]{1,300})?/likes',self.urlText.text()):
                self.logTextEdit.insertHtml('if you want to dl favs, url needs to end with /likes or /likes/<br>')
                self.go.setEnabled(True)
                return

        elif self.alltracksRadio.isChecked() is True:
            type_dl='a'
            if not re.match('https?://(?:www)?(?:[\w-]{2,255}(?:\.\w{2,6}){1,2})(?:/[\w&%?#-]{1,300})?',self.urlText.text()):
                self.logTextEdit.insertHtml('URL doesnt seems to be valid<br>')
                self.go.setEnabled(True)
                return
        elif self.trackRadio.isChecked() is True:
            type_dl='t'
            if not re.match('https?://(?:www)?(?:[\w-]{2,255}(?:\.\w{2,6}){1,2})(?:/[\w&%?#-]{1,300})?',self.urlText.text()):
                self.logTextEdit.insertHtml('URL doesnt seems to be valid<br>')
                self.go.setEnabled(True)
                return
        elif self.playlistRadio.isChecked() is True:
            type_dl='p'
            if not re.match('https?://(?:www)?(?:[\w-]{2,255}(?:\.\w{2,6}){1,2})(?:/[\w&%?#-]{1,300})?',self.urlText.text()):
                self.logTextEdit.insertHtml('URL doesnt seems to be valid<br>')
                self.go.setEnabled(True)
                return
        if type_dl != 'stream':
            self.Tget_item = T_get_item(self.urlText.text(), self.pathText.text(), self.tokenText.text(), type_dl, self.progressBar, options) #type_dl : 
            self.Tget_item.mysignal.connect(lambda: self.go.setEnabled(True), QtCore.Qt.QueuedConnection)
            self.Tget_item.console.connect(self.onProgress)
            self.Tget_item.start()
     
        
    def stop(self): #Dirty way to kill thread. A restart of the app should be done to avoid memory leaks... fine for now.
        if (self.Tget_item.isRunning):
            self.Tget_item.terminate()
            self.go.setEnabled(True)
            self.stopButton.setEnabled(False)

    def _get_config(self):
        """
        read the path where to store music
        """
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.expanduser('~'), '.config/scdl/scdl-qt.cfg'))
        if not os.path.isfile(os.path.join(os.path.expanduser('~'), '.config/scdl/scdl-qt.cfg')):
            #print('config file doesnt exists.... creating a blank one in userprofile/.config/scdl')
            with open(os.path.join(os.path.expanduser('~'), '.config/scdl/scdl-qt.cfg'),'w+') as f:
                f.write('[scdl]\nauth_token = \npath = {0}'.format(os.environ['UserProfile']+'\Desktop\scdl')) # create config file with blank token and %userprofile%\desktop\scdl folder
                self.pathText.setText(os.environ['UserProfile']+'\Desktop\scdl')
                f.close()
        try:
            token = config['scdl']['auth_token']
            path = config['scdl']['path']
            options = config['scdl']['options']
            self.tokenText.setText(token)
            self.pathText.setText(path)
            if 'c' in options:
                self.cBox.setChecked(True)
            else:
                self.cBox.setChecked(False)
            if 'r' in options:
                self.rBox.setChecked(True)
            else:
                self.rBox.setChecked(False)
            if 'm' in options:
                self.mp3Box.setChecked(True)
            else:
                self.mp3Box.setChecked(False)
            if 's' in options:
                self.sBox.setChecked(True)
            else:
                self.sBox.setChecked(False)
        except:
            self.logTextEdit.insertHtml('Welcome to scdl-qt ! First run, creating config file....<br>To download tracks from your stream, get your token with "get sc token" and fill it in<br>')


    def saveconfig(self):
            with open(os.path.join(os.path.expanduser('~'), '.config/scdl/scdl-qt.cfg'),'w+') as f:
                tok = self.tokenText.text()
                pat = self.pathText.text()
                options = ''
                if self.cBox.isChecked():
                    options=options+'c'
                if self.rBox.isChecked():
                    options=options+'r'
                if self.mp3Box.isChecked():
                    options=options+'m'
                if self.sBox.isChecked():
                    options=options+'s'
                f.write('[scdl]\nauth_token = {0}\npath = {1}\noptions = {2}'.format(tok, pat,options))
    
    def handleButton(self):
        options = ''
        self.stopButton.setEnabled(True)
        if self.cBox.isChecked():
            options=options+'c'
        if self.rBox.isChecked():
            options=options+'r'
        if self.mp3Box.isChecked():
            options=options+'m'
        if self.sBox.isChecked():
            options=options+'s'
        self.go.setEnabled(False)
        type_dl = ''
        if self.streamRadio.isChecked() is False:
            if not re.match('(?:https?:\/\/)?(?:www\.?)?soundcloud\.com((?=([^a-z 0-9]))([^\s])*|)',self.urlText.text()):
                self.logTextEdit.insertHtml('not soundcloud URL<br>')
                self.go.setEnabled(True)
                return
        if self.streamRadio.isChecked() is True:
            type_dl='stream'
            pattern = re.compile("^\w-\w\w\w\w\w\w-*")
            if pattern.match(self.tokenText.text()):
                self.Tget_item = T_get_item(self.urlText.text(), self.pathText.text(), self.tokenText.text(), type_dl, self.progressBar, options) #type_dl : 
                self.Tget_item.console.connect(self.onProgress)
                self.Tget_item.start() 
            else:
                self.logTextEdit.insertHtml('Token doesnt look valid.... Valid token is like : 1-126000-000707-50006e52ef30d000. Click on get sc token<br>')
                self.go.setEnabled(True)
        elif self.allfavsRadio.isChecked() is True:
            type_dl='f'
            if not re.match('http.?://(?:www)?(?:[\w-]{2,255}(?:\.\w{2,6}){1,2})(?:/[\w&%?#-]{1,300})?/likes',self.urlText.text()):
                self.logTextEdit.insertHtml('if you want to dl favs, url needs to end with /likes or /likes/<br>')
                self.go.setEnabled(True)
                return

        elif self.alltracksRadio.isChecked() is True:
            type_dl='a'
            if not re.match('https?://(?:www)?(?:[\w-]{2,255}(?:\.\w{2,6}){1,2})(?:/[\w&%?#-]{1,300})?',self.urlText.text()):
                self.logTextEdit.insertHtml('URL doesnt seems to be valid<br>')
                self.go.setEnabled(True)
                return
        elif self.trackRadio.isChecked() is True:
            type_dl='t'
            if not re.match('https?://(?:www)?(?:[\w-]{2,255}(?:\.\w{2,6}){1,2})(?:/[\w&%?#-]{1,300})?',self.urlText.text()):
                self.logTextEdit.insertHtml('URL doesnt seems to be valid<br>')
                self.go.setEnabled(True)
                return
        elif self.playlistRadio.isChecked() is True:
            type_dl='p'
            if not re.match('https?://(?:www)?(?:[\w-]{2,255}(?:\.\w{2,6}){1,2})(?:/[\w&%?#-]{1,300})?',self.urlText.text()):
                self.logTextEdit.insertHtml('URL doesnt seems to be valid<br>')
                self.go.setEnabled(True)
                return
        if type_dl != 'stream':
            self.Tget_item = T_get_item(self.urlText.text(), self.pathText.text(), self.tokenText.text(), type_dl, self.progressBar, options) #type_dl : 
            self.Tget_item.mysignal.connect(lambda: self.go.setEnabled(True), QtCore.Qt.QueuedConnection)
            self.Tget_item.console.connect(self.onProgress)
            self.Tget_item.start()
        
    
    def gettoken(self):
        webbrowser.open_new('http://flyingrub.tk/soundcloud/')
        
    def browse_folder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                           "Pick a folder")
        self.pathText.setText(directory)
        
    def onProgress(self, message, p):
        if p==666:
            self.logTextEdit.insertHtml('<font color=red>File already exists, download stopped... Change options to change behavior :)<br></font>')
            self.stop()
            self.go.setEnabled(True)
            self.stopButton.setEnabled(False)
            sys.exit()
            return
        if '%%%sp33d' in message:
            self.speedLabel.setText(str(round(p/1000))+' KB/s')
            p=999
        elif '%%%PROGRESSSSS' not in message:
            self.logTextEdit.insertHtml(message+'<br>')
            self.logTextEdit.moveCursor(QtGui.QTextCursor.End)
            p=999
        if p is not (999 or 666):
            self.progressBar.setValue(p)
            self.logTextEdit.moveCursor(QtGui.QTextCursor.End)

class T_get_item(QThread): 
    console = QtCore.pyqtSignal(str, int)
    mysignal = QtCore.pyqtSignal()
    


    def __init__(self, urlin, pathin, token, type, progress,  options):
        QThread.__init__(self)
        self.urlin = urlin
        self.pathin = pathin
        self.token = token
        self.type = type
        self.progressBar = progress
        self.options = options
        
    def __del__(self):
        self.wait()
    
        
    def _get_item(self, urlin):

        """
        Fetches metadata for an track or playlist
        """
        try:
            item = client.get('/resolve', url=urlin)
            self.console.emit('item retrieved {0}'.format(item.kind),999)
            return item
        except Exception:
            self.console.emit('unknown error',999)
            #self._parse_url('','','','',True)
            return 
    
    def _download_all(self, tracks, options):
        """
        Download all song of a page
        Not recommended
        """
        for counter, track in enumerate(tracks, 1):
            #logger.newline()
            #logger.info('Track n°{0}'.format(counter))
            self._download_track(track, '0', options)            
                
    def _parse_url(self, track_url, date_t,  type,  options, abort=False):
        """
        Detects if the URL is a track or playlists, and parses the track(s) to the track downloader
        """
        #if abort is True:
            #return
        global arguments
        if type=='f':
           track_url = track_url.replace('/likes','')
           item = self._get_item(track_url)
           self._download_all_user_favs(self.urlin.replace('/likes',''), 'track', self._download_track, options)
           type = 'a'
        item = self._get_item(track_url)
        if not item:
            return
        if type is 't' and item.kind == 'track':
            self._download_track(item, date_t, options)
        elif item.kind == 'playlist' and type is 'p':
            self.console.emit('Found a playlist... starting loop to dl it', 999)
            self._download_playlist(item, options, len(item.tracks))
        elif item.kind == 'user' and type =='a':
            self._download_all_of_user(self.urlin, 'track', self._download_track, options)

    
    
    def _who_am_i(self):
        """
        display to who the current token correspond, check if the token is valid
        """
        global client
        client = soundcloud.Client(access_token=self.token, client_id='95a4c0ef214f2a4a0852142807b54b35')#scdl_client_id)
    
        try:
            current_user = client.get('/me')
        except:
            self.console.emit('<font color="#CC001E">token problem</font>',999)
            #self.console.emit('',666) #666 kills thread (or not)
            return
        self.console.emit('<font color="#CC497E">Hello {0.username}!</font>'.format(current_user).encode('utf-8', errors='ignore').decode('utf-8', errors='replace'), 999)
        return current_user
    
    
    def _download_all_user_tracks(self, user, options):
        """
        Find track & repost of the user
        """
        item = self._get_item(user)
        url = 'https://api.sndcdn.com/e1/users/{0.id}/tracks.json?limit=1&offset={1}&client_id={2}'.format(item, 0, scdl_client_id)
        response = urllib.request.urlopen(url)
        
        data = response.read()
        text = data.decode('utf-8')
        json_data = json.loads(text)
        while json_data:
            self._offset += 1
            try:
                this_url = json_data[0]['track']['uri']
            except:
                this_url = json_data[0]['playlist']['uri']
            self._parse_url(this_url, '0', 't', options)
            url = 'https://api.sndcdn.com/e1/users/{0.id}/tracks.json?limit=1&offset={1}&client_id={2}'.format(item, self._offset, scdl_client_id)
            response = urllib.request.urlopen(url)
            data = response.read()
            text = data.decode('utf-8')
            json_data = json.loads(text)

    def _download_all_user_favs(self, user, name, download_function, options, abort=False): #BETA
        """
        Download all items of an user. Can be playlist or track, or whatever handled by the download function.
        """
        #if abort is True:
            #return
        """
        user2 = self._get_item(user)
        self.console.emit('Retrieving the favorites of user {0.username}...might take a while...'.format(user2), 999)
        time.sleep(5)
        #logger.info('user is{0}'.format(user2))
        items = client.get_all('/users/{0.id}/favorites'.format(user2))
        #items = client.get_all('/users/rafi-ki/likes')
        total = len(items)
        s = '' if total == 1 else 's'
        self.console.emit('Retrieved {2} {0}{1}'.format(name, s, total), 999)
        for counter, item in enumerate(items, 1):
            try:
                self.console.emit('{0} n°{1} of {2}'.format(name.capitalize(), counter, total), 999)
                download_function(item, 0, options)
            except Exception as e:
                self.console.emit('ERROR:'+str(e), 999)
        self.console.emit('Downloaded all favorites of user {0.username}!'.format(user2), 999)
        """
        offset=0
        user2 = self._get_item(user)
        self.console.emit('Retrieving the favorites of user {0.username}...might take a while...'.format(user2), 999)
        #self.console.emit('https://api.soundcloud.com/users/{0.id}/favorites?limit=200&offset='.format(user2), 999)
        url = 'https://api.soundcloud.com/users/{0.id}/favorites?limit=200&offset={1}&client_id={2}'.format(user2, offset, scdl_client_id)
        #time.sleep(5)
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode('utf-8')
        json_data = json.loads(text)
        while json_data :
            if  json_data[offset]['uri'] is not None :
                this_url = json_data[offset]['uri']
                type = json_data[offset]['kind']
                """logger.info('Type:{0}'.format(type))"""
                date_track = json_data[offset]['created_at']
                offset += 1
                self.console.emit('Track n°{0}'.format(offset), 999)
                format_src = "%Y/%m/%d %H:%M:%S"
                format_dest = "%y%m%d %H%M%S - "
                date_track  = time.strftime(format_dest, time.strptime(date_track[:-6],format_src))
                if (type == 'track-repost') and 'r' in options:
                    self.console.emit('Repost skipped...', 999)
                else:
                    self._parse_url(this_url, date_track, 't', options)
            else:
                self.console.emit('error', 999)
        """while 1:
            url = json_data['next_href']
            offset=0
            url = url + '&limit=150&oauth_token={0}'.format(self.token)
            response = urllib.request.urlopen(url)
            data = response.read()
            text = data.decode('utf-8')
            json_data = json.loads(text)
            while json_data and offset <=145:
                this_url = json_data[offset]['uri']
                type = json_data[offset]['kind']
                date_track = json_data[offset]['created_at']
                offset += 1
                format_src = "%Y/%m/%d %H:%M:%S"
                format_dest = "%y%m%d %H%M%S - "
                date_track  = time.strftime(format_dest, time.strptime(date_track[:-6],format_src))
            if (type == 'track-repost') and 'r' in options:
                self.console.emit('Repost skipped...', 999)
            elif (type != 'track-repost'):
                self._parse_url(this_url, date_track, 't', options)"""
        
    
    def _download_all_of_user(self, user, name, download_function, options, abort=False):
        """
        Download all items of an user. Can be playlist or track, or whatever handled by the download function.
        """
        #if abort is True:
            #return
        
        user2 = self._get_item(user)
        self.console.emit('Retrieving the {1}s of user {0.username}...'.format(user2, name), 999)
        items = client.get_all('/users/{0.id}/{1}s'.format(user2, name))
        total = len(items)
        s = '' if total == 1 else 's'
        self.console.emit('Retrieved {2} {0}{1}'.format(name, s, total), 999)
        for counter, item in enumerate(items, 1):
            try:
                self.console.emit('{0} n°{1} of {2}'.format(name.capitalize(), counter, total), 999)
                download_function(item, 0, options)
            except Exception as e:
                self.console.emit('ERROR:'+str(e), 999)
        self.console.emit('Downloaded all {2} {0}{1} of user {3.username}!'.format(name, s, total, user2), 999)
    
    
    def _download_my_stream(self, user, name, download_function, token, options):
    
        offset=0
        url = 'https://api.soundcloud.com/me/activities/tracks/affiliated?limit=50&oauth_token={0}'.format(self.token)
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode('utf-8')
        json_data = json.loads(text)
        loop = 0
        while json_data and offset <=50:
            try:
                this_url = json_data['collection'][offset]['origin']['uri']
                type = json_data['collection'][offset]['type']
                """logger.info('Type:{0}'.format(type))"""
                date_track = json_data['collection'][offset]['created_at']
                offset += 1
                tracknum = offset+loop*50
                self.console.emit('Track n°{0}'.format(tracknum), 999)
                format_src = "%Y/%m/%d %H:%M:%S"
                format_dest = "%y%m%d %H%M%S - "
                date_track  = time.strftime(format_dest, time.strptime(date_track[:-6],format_src))
                if (type == 'track-repost') and 'r' in options:
                    self.console.emit('Repost skipped...', 999)
                else:
                    self._parse_url(this_url, date_track, 't', options)
                if offset==50:
                    url = json_data['next_href'] + '&oauth_token={0}'.format(self.token)
                    self.console.emit('next page loaded{0}'.format(url), 999)
                    response = urllib.request.urlopen(url)
                    data = response.read()
                    text = data.decode('utf-8')
                    json_data = json.loads(text)
                    offset = 0
                    loop += 1
            except TypeError:
                self.console.emit('error', 999)
        '''while 1:
            url = json_data['next_href']
            offset=0
            url = url + '&limit=149&oauth_token={0}'.format(self.token)
            response = urllib.request.urlopen(url)
            data = response.read()
            text = data.decode('utf-8')
            json_data = json.loads(text)
            while json_data and offset <=40:
                this_url = json_data['collection'][offset]['origin']['uri']
                type = json_data['collection'][offset]['type']
                date_track = json_data['collection'][offset]['created_at']
                offset += 1
                format_src = "%Y/%m/%d %H:%M:%S"
                format_dest = "%y%m%d %H%M%S - "
                date_track  = time.strftime(format_dest, time.strptime(date_track[:-6],format_src))
            if (type == 'track-repost') and 'r' in options:
                self.console.emit('Repost skipped...', 999)
            elif (type != 'track-repost'):
                self._parse_url(this_url, date_track, 't', options)'''
                
    def _download_playlist(self, playlist, options, number):
        """
        Download a playlist
        """
        
        invalid_chars = '\/:*?|<>"'
        playlist_name = playlist.title.encode('utf-8', 'ignore').decode('utf-8')
        playlist_name = ''.join(c for c in playlist_name if c not in invalid_chars)
    
        if not os.path.exists(playlist_name):
            os.makedirs(playlist_name)
        os.chdir(playlist_name)
    
        for counter, track_raw in enumerate(playlist.tracks, 1):
            mp3_url = self._get_item(track_raw['permalink_url'])
            #logger.info('Track n°{0} / {1}'.format(counter, track_raw in len(playlist.tracks)))
            self.console.emit('Track n°{0} / {1}'.format(counter, number),999)
            self._download_track(mp3_url, '0', options, playlist.title)
        os.chdir('..')

    def _download_track(self, track, date_t, options, playlist_name=None):
        """
        Downloads a track
        """
        if track.streamable:
            try:
                stream_url = client.get(track.stream_url, allow_redirects=False)
                url = stream_url.location
            except HTTPError:
                self.console.emit('<font color=red>internet error. please restart the app or check your internet connection</font>',999)
                return
                
        else:
            #logger.error('{0.title} is not streamable...'.format(track))
            self.console.emit('Problem downloading this track, soundcloud api didnt give proper url', 999)
            return
        title = track.title
        title = title.encode('utf-8', 'ignore').decode('utf-8', 'ignore')
        self.console.emit('<font color="#FF3196">>> {0}</font>'.format(title), 999)
        #filename
        if track.downloadable and 'm' not in options:
            #logger.info('Downloading the orginal file.')
            url = '{0.download_url}?client_id={1}'.format(track, scdl_client_id)
    
            filename = urllib.request.urlopen(url).info()['Content-Disposition'].split('filename=')[1]
            if filename[0] == '"' or filename[0] == "'":
                filename = filename[1:-1]
        else:
            invalid_chars = ':"\/*?|<>'
            if track.user['username'] not in title:
                title = '{0.user[username]} - {1}'.format(track, title)
            title = ''.join(c for c in title if c not in invalid_chars)
            title.translate(':"\/*?|<>')
            title=''.join(i for i in title if i not in invalid_chars)
            filename = title + '.mp3'
            
            #filename = date_t + filename # REMOVED date-t for debug
            filename = filename
    
        # Download
        invalid_chars = ':"\/*?|<>'
        filename.translate(':"\/*?|<>')
        filename=''.join(i for i in filename if i not in invalid_chars)
        if (os.path.isfile(self.pathin + '\\' + filename) and 'c' in options):
            #TODO: stop thread
            self.console.emit('',666)
            return
        if (os.path.isfile(self.pathin + '\\' + filename) and 's' in options):
            self.console.emit('<font color="#CC0066">file exists, skipped...</font>', 999)
            return
            
        if (os.path.isfile(self.pathin + '\\' + filename) and 'c' not in options) or (not os.path.isfile(self.pathin + '\\' + filename)): 
        #if not os.path.isfile(filename+):
            #print('oh yeah c is in options')
            u = urlopen(url)
            full_filename= self.pathin + '\\' + filename
            if not os.path.isdir(self.pathin):
                os.mkdir(self.pathin)
            f = open(full_filename, 'wb')
            file_size=int(u.getheader('Content-Length'))
            #print("Downloading: {0} Bytes: {1}".format(url, file_size))
            size=round(file_size/1000000, 1)
            self.console.emit('size: <font color="#CC0066">{0} MB</font>'.format(size), 999)
            speed_clock = 0
            file_size_dl = 0
            block_sz = 65536
            start_time = time.time()
            while True:
                buffer = u.read(block_sz)
                if not buffer:
                    break

                
                file_size_dl += len(buffer)
                speed_clock += len(buffer)
                if speed_clock > block_sz*5: #send speed signal to GUI every 5 blocks 
                    speed_clock =0
                    elapsed = time.time() - start_time
                    if elapsed > 0.0:
                        speed = float(file_size_dl) / elapsed
                        self.console.emit('%%%sp33d', speed) # send speed with special str to update speed meter
                f.write(buffer)
                p = float(file_size_dl) / file_size
                self.console.emit('%%%PROGRESSSSS', int(p*100)) # send progress with special str to update progressBar
                
                #now = time.time()


            f.close()
        #elif 'c' not in options:  
                #self.console.emit('Already exists, skipping...', 999)
    
        

    
    
    def _settags(self, track, filename, album='Soundcloud'):
        """
        Set the tags to the mp3
        
        logger.info('Settings tags...')
        user = client.get('/users/{0.user_id}'.format(track), allow_redirects=False)
        audio = mutagen.File(filename)
        audio['TIT2'] = mutagen.id3.TIT2(encoding=3, text=track.title)
        audio['TALB'] = mutagen.id3.TALB(encoding=3, text=album)
        audio['TPE1'] = mutagen.id3.TPE1(encoding=3, text=user.username)
        audio['TCON'] = mutagen.id3.TCON(encoding=3, text=track.genre)
        audio.save()
        """
    
    def _signal_handler(self, signal, frame):
        """
        handle keyboardinterrupt
        """
        time.sleep(1)
        files = os.listdir()
        for f in files:
            if not os.path.isdir(f) and '.tmp' in f:
                os.remove(f)
        
    def run(self):
        if self.type is 'stream':
            self._download_my_stream(self._who_am_i(), 'track', 'download_track', self.token, self.options)
        self._parse_url(self.urlin, 0, self.type,  self.options)
        self.mysignal.emit() #mysignal re enable the dl button
        self.finished.emit()
        self.sleep(2)

        
def main():
        app = QtWidgets.QApplication(sys.argv)
        form = ExampleApp()
        form.show()
        app.exec_()
        
        


        
if __name__ == "__main__":
        main()
