from distutils.core import setup
import py2exe
import requests.certs

build_exe_options = {"include_files":[(requests.certs.where(),'cacert.pem')]}
data_files = build_exe_options
options = {
                    'py2exe': {
                            'bundle_files': 3,
                            'optimize': 2,
                            'includes': ['sip', 'scdl', 'soundcloud'],
                            'excludes': [],
                            'data_files': [(requests.certs.where(),'cacert.pem')]
                    }
               },

setup(console = ['scdl-qt.py'])