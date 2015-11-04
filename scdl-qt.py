# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
import design
import sys
import os
import time
import json
import logging
import webbrowser
import urllib.request
#import warnings
#import configparser
import mutagen
import urllib
import re
#from docopt import docopt
#from requests.exceptions import HTTPError

#from scdl import __version__
from scdl import soundcloud#, utils
from urllib.request import urlopen


scdl_client_id = '95a4c0ef214f2a4a0852142807b54b35'
client = soundcloud.Client(client_id=scdl_client_id)
token = ''


logging.basicConfig(level=logging.INFO, format='%(message)s')
logging.getLogger('urllib3.connectionpool').setLevel(logging.ERROR)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#logger.addFilter(utils.ColorizeFilter())
logger.newline = print
      
class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.btnBrowse.clicked.connect(self.browse_folder)
        self.gettokenButton.clicked.connect(self.gettoken)
        self.pathText.setText(os.environ['UserProfile']+'\Desktop\scdl')
        self.go.clicked.connect(self.handleButton)

    def handleButton(self):
        type_dl = ''
        if self.streamRadio.isChecked() is True:
            type_dl='stream'
            print('stream mode')
            pattern = re.compile("^\w-\w\w\w\w\w\w-\w\w\w\w\w\w-\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w")
            if pattern.match(self.tokenText.text()):
                print('token matches RegEx')
                self.Tget_item = T_get_item(self.urlText.text(), self.pathText.text(), self.tokenText.text(), type_dl, self.progressBar) #type_dl : 
                self.Tget_item.notifyProgress2.connect(self.onProgress)
                self.Tget_item.start() 
            else:
                self.logTextEdit.appendPlainText('Token inputed doesnt look valid.... Valid token is like : 1-126000-000707-50006e52ef30d000')
        elif self.allfavsRadio.isChecked() is True:
            type_dl='f'
        elif self.alltracksRadio.isChecked() is True:
            type_dl='a'
        elif self.trackRadio.isChecked() is True:
            type_dl='t'
        elif self.playlistRadio.isChecked() is True:
            type_dl='p'
        if type_dl != 'stream':
            self.Tget_item = T_get_item(self.urlText.text(), self.pathText.text(), self.tokenText.text(), type_dl, self.progressBar) #type_dl : 
            self.Tget_item.notifyProgress2.connect(self.onProgress)
            self.Tget_item.start()
            
    def gettoken(self):
        print('uck offf')
        webbrowser.open_new('http://flyingrub.tk/soundcloud/')
        
    def browse_folder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                           "Pick a folder")
        # execute getExistingDirectory dialog and set the directory variable 
        self.pathText.setText(directory)
        
    def onProgress(self, message, p):
        if 'fuck' not in message:
            self.logTextEdit.appendPlainText(message)
        if p is not 999:
            self.progressBar.setValue(p)

class T_get_item(QThread): 
    notifyProgress2 = QtCore.pyqtSignal(str, int)
    
    def __init__(self, urlin, pathin, token, type, progress):
        QThread.__init__(self)
        self.urlin = urlin
        self.pathin = pathin
        self.token = token
        self.type = type
        self.progressBar = progress

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
            
    def _parse_url(self, track_url, date_t,  type):
        """
        Detects if the URL is a track or playlists, and parses the track(s) to the track downloader
        """
        global arguments
        print('DFDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD')
        item = self._get_item(track_url)
        print('url being read is {0}'.format(track_url))
        if item.kind == 'track' and type is 't':
            logger.info('Found a track')
            self._download_track(item, date_t)
        elif item.kind == 'playlist' and type is 'p':
            logger.info('Found a playlist')
            self.notifyProgress2.emit('Found a playlist... starting loop to dl it', 999)
            self._download_playlist(item)
        elif item.kind == 'user' and type =='a':
            logger.info('Found an user profile')
            self._download_all_of_user(self.urlin, 'track', self._download_track)
            print(type)
        if type is 'f':
            self._download_all_of_user(self.urlin, 'favorite', self._download_track)
            print(type)
        elif type is 't':
            #self._download_all_of_user(self.urlin, 'track', self._download_track)
            print(type)
        elif type is 'a':
            #self._download_all_user_tracks(self.urlin)
            print(type)
        elif type is 'p':
            self._download_all_of_user(item, 'playlist', self._download_playlist)
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
        self.notifyProgress2.emit('Hello {0.username}!'.format(current_user).encode('ascii', errors='ignore').decode('ascii', errors='replace'), 999)
        logger.newline()
        return current_user
    
    
    def _download_all_user_tracks(self, user):
        """
        Find track & repost of the user
        """
        #global offset
        item = self._get_item(user)
        logger.info('Hello ID {0.id}!'.format(item))
        url = 'https://api.sndcdn.com/e1/users/{0.id}/sounds.json?limit=1&offset={1}&client_id={2}'.format(item, 0, scdl_client_id)
        print(url)
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
            self._parse_url(this_url, '0', 't')
            print('parsed')
            url = 'https://api.sndcdn.com/e1/users/{0.id}/sounds.json?limit=1&offset={1}&client_id={2}'.format(item, self._offset, scdl_client_id)
            response = urllib.request.urlopen(url)
            data = response.read()
            text = data.decode('utf-8')
            json_data = json.loads(text)
    
    
    def _download_all_of_user(self, user, name, download_function):
        """
        Download all items of an user. Can be playlist or track, or whatever handled by the download function.
        """
        user = self._get_item(user)
        logger.info('Retrieving the {1}s of user {0.username}...'.format(user, name))
        items = client.get_all('/users/{0.id}/{1}s'.format(user, name))
        total = len(items)
        s = '' if total == 1 else 's'
        logger.info('Retrieved {2} {0}{1}'.format(name, s, total))
        for counter, item in enumerate(items, 1):
            try:
                logger.info('{0} n°{1} of {2}'.format(name.capitalize(), counter, total))
                download_function(item, 0)
            except Exception as e:
                logger.exception(e)
        logger.info('Downloaded all {2} {0}{1} of user {3.username}!'.format(name, s, total, user))
    
    
    def _download_my_stream(self, user, name, download_function, token):
    
        offset=0
        url = 'https://api.soundcloud.com/me/activities/tracks/affiliated?limit=152&oauth_token={0}'.format(self.token)
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode('utf-8')
        json_data = json.loads(text)
        while json_data and offset <=150:
            this_url = json_data['collection'][offset]['origin']['uri'] # 0=offset
            type = json_data['collection'][offset]['type']
            """logger.info('Type:{0}'.format(type))"""
            date_track = json_data['collection'][offset]['created_at']
            offset += 1
            logger.info('Track n°{0}'.format(offset))
            self.notifyProgress2.emit('Track n°{0}'.format(offset), 999)
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
            url = url + '&limit=150&oauth_token={0}'.format(self.token)
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
        print(playlist.tracks)
        print(enumerate(playlist.tracks, 1))
        
        invalid_chars = '\/:*?|<>"'
        playlist_name = playlist.title.encode('utf-8', 'ignore').decode('utf-8')
        playlist_name = ''.join(c for c in playlist_name if c not in invalid_chars)
    
        if not os.path.exists(playlist_name):
            os.makedirs(playlist_name)
        os.chdir(playlist_name)
    
        for counter, track_raw in enumerate(playlist.tracks, 1):
            mp3_url = self._get_item(track_raw['permalink_url'])
            logger.info('Track n°{0} / {1}'.format(counter, track_raw in enumerate(playlist.tracks, 1)))
            self._download_track(mp3_url, '0', playlist.title)
    #TODO : problem with lenght of playlist. it will download even if no more tracks
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
        logger.info('Downloading  {0}'.format(title))
        self.notifyProgress2.emit('Downloading {0}'.format(title), 999)
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
            print('oh yeah')
            u = urlopen(url)
            full_filename= self.pathin + '\\' + filename
            if not os.path.isdir(self.pathin):
                os.mkdir(self.pathin)
            f = open(full_filename, 'wb')
            file_size=int(u.getheader('Content-Length'))
            print("Downloading: {0} Bytes: {1}".format(url, file_size))
            self.notifyProgress2.emit('size: {0} Mb'.format(file_size/1000000), 999)

            file_size_dl = 0
            block_sz = 8196
            while True:
                buffer = u.read(block_sz)
                if not buffer:
                    break

                file_size_dl += len(buffer)
                f.write(buffer)
                p = float(file_size_dl) / file_size
                self.notifyProgress2.emit('fuck', int(p*100))

            f.close()
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
        self._parse_url(self.urlin, 0, self.type)
        self.finished.emit()
        self.sleep(2)
        
       
        
def main():
        app = QtWidgets.QApplication(sys.argv)
        form = ExampleApp()
        form.show()
        app.exec_()
        
        


        
if __name__ == "__main__":
        main()
