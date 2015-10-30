# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
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
import urllib
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
        self.go.clicked.connect(self.handleButton)
        

        
    def handleButton(self):
        self.myThread = T1()
        self.myThread.notifyProgress.connect(self.onProgress)
        self.myThread.start()
        type_dl = ''
        if self.streamRadio.isChecked() is True:
            type_dl = 'stream'
            print('stream mode')
        self.Tget_item = T_get_item(self.urlText.text(), self.pathText.text(), self.tokenText.text(), type_dl) #type_dl : 
        self.Tget_item.notifyProgress.connect(self.onProgress)
        self.Tget_item.start()  
        
    def browse_folder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                           "Pick a folder")
        # execute getExistingDirectory dialog and set the directory variable 
        self.pathText.setText(directory)
        
    def onProgress(self, i):
        self.progressBar.setValue(self.progressBar.value()+1)
    #def onURLChange(self):
     #   self.Tget_item.start()      
       
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
    
    def __init__(self, urlin, pathin, token, type):
        QThread.__init__(self)
        self.urlin = urlin
        self.pathin = pathin
        self.token = token
        self.type = type

    def __del__(self):
        self.wait()
    
    def _get_config(self, _path, _token):
        """
        read the path where to store music
        """
        #config = configparser.ConfigParser()
        config.read(os.path.join(os.path.expanduser('~'), '.config/scdl/scdl.cfg'))
        try:
            """token = config['scdl']['auth_token']"""
            path = config['scdl']['path']
        except:
            logger.error('Are you sure scdl.cfg is in $HOME/.config/scdl/ ?')
            sys.exit()
        if os.path.exists(path):
            os.chdir(path)
        else:
            logger.error('Invalid path in scdl.cfg...')
            sys.exit()
        
    def _get_item(self, urlin):
        """
        Fetches metadata for an track or playlist
        """
        track_url=urlin
        try:
            item = client.get('/resolve', url=track_url)
            logger.error('url {0}'.format(track_url))
        except Exception:
            logger.error('Error resolving url {0}, retrying...'.format(track_url))
            time.sleep(5)
            try:
                item = client.get('/resolve', url=track_url)
            except Exception as e:
                logger.error('Could not resolve url {0}'.format(track_url))
                logger.exception(e)
                #sys.exit(0)
        return item
            
    def _parse_url(self, track_url, date_t):
        """
        Detects if the URL is a track or playlists, and parses the track(s) to the track downloader
        """
        global arguments
        item = self._get_item(track_url)
    
        if not item:
            return
        #elif isinstance(item, soundcloud.resource.ResourceList):
            #download_all(item)
        elif item.kind == 'track':
            logger.info('Found a track')
            self._download_track(item, date_t)
        #elif item.kind == 'playlist' and arguments['-l']:
            #logger.info('Found a playlist')
            #download_playlist(item)
        elif item.kind == 'playlist':
            logger.info('Found a playlist, but i am setup to skip it :)')
            """download_playlist(item)"""
        elif item.kind == 'user':
            logger.info('Found an user profile')
        if type is 'f':
            self._download_all_of_user(self.urlin, 'favorite', self._download_track)
        elif type is 't':
            self._download_all_of_user(self.urlin, 'track', self._download_track)
        elif type is 'a':
            self._download_all_user_tracks(self.urlin)
        #elif type is 'p':
            '''if arguments['-f']:
                download_all_of_user(item, 'favorite', download_track)
            elif arguments['-t']:
                download_all_of_user(item, 'track', download_track)
            elif arguments['-a']:
                download_all_user_tracks(item)
            elif arguments['-p']:
                download_all_of_user(item, 'playlist', download_playlist)
            else:
                logger.error('Please provide a download type...')'''
        else:
            logger.error('Unknown item type')
    
    
    def _who_am_i(self):
        """
        display to who the current token correspond, check if the token is valid
        """
        global client
        client = soundcloud.Client(access_token=self.token, client_id='95a4c0ef214f2a4a0852142807b54b35')#scdl_client_id)
    
        try:
            current_user = client.get('/me')
        except:
            logger.error('Invalid token...')
            sys.exit(0)
        logger.info('Hello {0.username}!'.format(current_user))
        logger.newline()
        return current_user
    
    
    def _download_all_user_tracks(self, user):
        """
        Find track & repost of the user
        """
        #global offset
        logger.info('Hello ID {0.id}!'.format(user))
        url = 'https://api.sndcdn.com/e1/users/{0.id}/sounds.json?limit=1&offset={1}&client_id={2}'.format(user, 0, scdl_client_id)
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
            logger.info('Track n°{0}'.format(self._offset))
            self._parse_url(this_url, '0')
    
            url = 'https://api.sndcdn.com/e1/users/{0.id}/sounds.json?limit=1&offset={1}&client_id={2}'.format(user, self._offset, scdl_client_id)
            response = urllib.request.urlopen(url)
            data = response.read()
            text = data.decode('utf-8')
            json_data = json.loads(text)
    
    
    def _download_all_of_user(self, user, name, download_function):
        """
        Download all items of an user. Can be playlist or track, or whatever handled by the download function.
        """
        logger.info('Retrieving the {1}s of user {0.username}...'.format(user, name))
        items = client.get_all('/users/{0.id}/{1}s'.format(user, name))
        total = len(items)
        s = '' if total == 1 else 's'
        logger.info('Retrieved {2} {0}{1}'.format(name, s, total))
        for counter, item in enumerate(items, 1):
            try:
                logger.info('{0} n°{1} of {2}'.format(name.capitalize(), counter, total))
                download_function(item)
            except Exception as e:
                logger.exception(e)
        logger.info('Downloaded all {2} {0}{1} of user {3.username}!'.format(name, s, total, user))
    
    
    def _download_my_stream(self, user, name, download_function, token):
    
        offset=0
        print('test')
        url = 'https://api.soundcloud.com/me/activities/tracks/affiliated?limit=152&oauth_token={0}'.format(self.token)
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode('utf-8')
        json_data = json.loads(text)
        while json_data: #and offset <=150:
            this_url = json_data['collection'][offset]['origin']['uri'] # 0=offset
            type = json_data['collection'][offset]['type']
            """logger.info('Type:{0}'.format(type))"""
            date_track = json_data['collection'][offset]['created_at']
            offset += 1
            logger.info('Track n°{0}'.format(offset))
            format_src = "%Y/%m/%d %H:%M:%S"
            format_dest = "%y%m%d %H%M%S - "
            date_track  = time.strftime(format_dest, time.strptime(date_track[:-6],format_src))
            if ( type != 'track-repost'):
                self._parse_url(this_url, date_track)
            else:
                self._parse_url(this_url, date_track)
                logger.info('Repost NOT skipped')
        while 1:
            url = json_data['next_href']
            offset=0
            url = url + '&limit=150&oauth_token={0}'.format(token)
            logger.info(url)
            response = urllib.request.urlopen(url)
            data = response.read()
            text = data.decode('utf-8')
            json_data = json.loads(text)
            while json_data and offset <=145:
                this_url = json_data['collection'][offset]['origin']['uri']
                type = json_data['collection'][offset]['type']
                date_track = json_data['collection'][offset]['created_at']
                offset += 1
                logger.info('Track n°{0}'.format(offset))
                format_src = "%Y/%m/%d %H:%M:%S"
                format_dest = "%y%m%d %H%M%S - "
                date_track  = time.strftime(format_dest, time.strptime(date_track[:-6],format_src))
                if ( type != 'track-repost'):
                    self._parse_url(this_url, date_track)
                else:
                    logger.info('Repost NOT skipped')
                    self._parse_url(this_url, date_track)
    def _download_playlist(self, playlist):
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
            logger.info('Track n°{0}'.format(counter))
            self._download_track(mp3_url, '0', playlist.title)
    
        os.chdir('..')

    def _download_track(self, track, date_t, playlist_name=None):
        """
        Downloads a track
        """
        global arguments
    
        if track.streamable:
            try:
                stream_url = client.get(track.stream_url, allow_redirects=False)
                url = stream_url.location
            except HTTPError:
                url = self._alternative_download(track)
        else:
            logger.error('{0.title} is not streamable...'.format(track))
            logger.newline()
            return
        title = track.title
        logger.info('date {0}'.format(date_t))
        title = title.encode('utf-8', 'ignore').decode(sys.stdout.encoding)
        logger.info('Downloading {0}'.format(title))
    
        #filename
        if track.downloadable :
            logger.info('Downloading the orginal file.')
            url = '{0.download_url}?client_id={1}'.format(track, scdl_client_id)
    
            filename = urllib.request.urlopen(url).info()['Content-Disposition'].split('filename=')[1]
            if filename[0] == '"' or filename[0] == "'":
                filename = filename[1:-1]
        else:
            invalid_chars = ':"\/*?|<>'
            if track.user['username'] not in title: #and arguments['--addtofile']: TODO : GET VALUE FROM CHECKBOX
                title = '{0.user[username]} - {1}'.format(track, title)
            title = ''.join(c for c in title if c not in invalid_chars)
            logger.info('....{0} title b4 filters'.format(title))
            title.translate(':"\/*?|<>')
            title=''.join(i for i in title if i not in invalid_chars)
            logger.info('.........{0} title after filters'.format(title))
            filename = title + '.mp3'
            #filename = date_t + filename # REMOVED date-t for debug
            filename = filename
    
        # Download
        invalid_chars = ':"\/*?|<>'
        filename.translate(':"\/*?|<>')
        filename=''.join(i for i in filename if i not in invalid_chars)
        if not os.path.isfile(filename):
            wget.download(url, filename)
            logger.newline()
            if '.mp3' in filename:
                try:
                    if playlist_name is None:
                        self._settags(track, filename)
                    else:
                        self._settags(track, filename, playlist_name)
                except:
                    logger.error('Error trying to set the tags...')
            else:
                logger.error("This type of audio doesn't support tagging...")
        else:
            '''if arguments['-c']:  #TODO : GET VALUE FROM CHECKBOX
                logger.info('{0} already Downloaded - exiting software'.format(title))
                logger.newline()
                
                return
            else:
                logger.newline()
                logger.error('Music already exists ! (exiting)')
                sys.exit(0)'''
    
        logger.newline()
        logger.info('{0} Downloaded.'.format(filename))
        logger.newline()
    
    
    def _settags(self, track, filename, album='Soundcloud'):
        """
        Set the tags to the mp3
        """
        logger.info('Settings tags...')
        user = client.get('/users/{0.user_id}'.format(track), allow_redirects=False)
    
        """artwork_url = track.artwork_url
        if artwork_url is None:
            artwork_url = user.avatar_url
        artwork_url = artwork_url.replace('large', 't500x500')
        urllib.request.urlretrieve(artwork_url, '/tmp/scdl.jpg')"""
    
        audio = mutagen.File(filename)
        audio['TIT2'] = mutagen.id3.TIT2(encoding=3, text=track.title)
        audio['TALB'] = mutagen.id3.TALB(encoding=3, text=album)
        audio['TPE1'] = mutagen.id3.TPE1(encoding=3, text=user.username)
        audio['TCON'] = mutagen.id3.TCON(encoding=3, text=track.genre)
        """if artwork_url is not None:
            audio['APIC'] = mutagen.id3.APIC(encoding=3, mime='image/jpeg', type=3, desc='Cover',
                                             data=open('/tmp/scdl.jpg', 'rb').read())
        else:
            logger.error('Artwork can not be set.')"""
        audio.save()
    
    
    def _signal_handler(self, signal, frame):
        """
        handle keyboardinterrupt
        """
        time.sleep(1)
        files = os.listdir()
        for f in files:
            if not os.path.isdir(f) and '.tmp' in f:
                os.remove(f)
    
        logger.newline()
        logger.info('Good bye!')
        
    def run(self):
        if self.type is 'stream':
            print(self.token)
            self._download_my_stream(self._who_am_i(), 'track', 'download_track', self.token)
        self._parse_url(self.urlin, 0)
        self.finished.emit()
        self.sleep(2)
        
       
        
def main():
        app = QtWidgets.QApplication(sys.argv)
        form = ExampleApp()
        form.show()
        app.exec_()
        


        
if __name__ == "__main__":
        main()
