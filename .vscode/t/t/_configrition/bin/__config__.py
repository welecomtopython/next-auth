import configparser
import os
import ctypes
from threading import Thread
import time
import datetime
import numpy as np
from enum import Enum

class Path(Enum):
    __path:str=os.path.abspath(__file__)

    __hom:set=os.path.expanduser('~')
    __var:str=__path.split('\\')[:-3]
    root='\\'.join(__var)

    __bin=__path.split('\\')[:-1]
    root_bin='\\'.join(__bin)

#
print(Path.root.value)

class Config:

    def __init__(self):

        self.root=Path.root.value


        """map config >>
        1 add dir src
        2 add crent work dirctory
        [repo]

        js = ['config.json', 'library', 'porject', 'Refernsec']
        py = ['config.json', 'library', 'porject', 'Refernsec']

        [CWD]
        dir = D:\Src\bin

        [status]
        defult=falsa

        """
        pass
    def criet_config(self,**kwargs):
        """ 1read file global and get self.PATH Src """
        configFilePath =f'{self.root}/global_config.ini'
        r_config = configparser.ConfigParser()

        r_config.read(configFilePath)

        PATH =self.root
        print(n for n in os.listdir(f'{PATH}\src'))
        """ 2cobdtin loop in src add ary is dir"""
        globa=[n for n in os.listdir(f'{PATH}\src') if os.path.isdir(f'{PATH}\src\{n}')]


        w_config = configparser.ConfigParser()
        my_dict = {}
        for name in globa :
            my_dict[name] = os.listdir(f'{PATH}/src/{name}') # Add key-val


        w_config['repo']=my_dict
        w_config['CWD']={
            "dir":os.getcwd(),
            "item":os.listdir(os.getcwd())
        }
        w_config['status']={
        "defulte": False,
        "remote":False,

        }
        w_config['root']={
            "rootdir":'.',
            'outdir':"/"

        }


        with open('.src/config.ini', 'w') as configfile:
          w_config.write(configfile)
    def add_bin(self,):

        """ 1read file global and get self.PATH Src """
        configFilePath = r'../global_config.ini'
        r_config = configparser.ConfigParser()

        r_config.read(configFilePath)

        PATH=self.root

        def check_prep(path):
            if not os.path.exists(path):
                os.makedirs(path)
                FILE_ATTRIBUTE_HIDDEN = 0x02
                ret = ctypes.windll.kernel32.SetFileAttributesW(path, FILE_ATTRIBUTE_HIDDEN)
        check_prep('.src')
        with open(f'{PATH}\data\dir_info','r')as f :
            C=f.read()

            os.system(C)



    def run(self):
        self.add_bin()
        self.criet_config()


#
