import configparser
import os

prjdir=os.path.dirname(os.path.dirname(__file__))
path=os.path.abspath(os.path.join(prjdir+'\config\\'))
print(path)

class ConfigRead():
    def __init__(self,filename):
        self.filename=filename
        self.filepath=path+self.filename