import json
import os
import datetime
import time
import numpy as np

import colorama
from colorama import Fore, Back, Style

from st_files import  find_max_extension

__path = os.path.abspath(__file__)
__var = __path.split('\\')[:-3]

rootdir = 'E:\\LOc\\User\\'
print(rootdir)

NAME = os.getcwd()
NAMEf = NAME.split('\\')[-1]


class CVFileConfig:
    def __init__(self, name=NAMEf, type="", language="", start="", path="", inside=None, description="", main="",
                 version='1.0.0', orderdate=None,extension=None):
        if inside is None:
            inside = []
        if orderdate is None:
            orderdate = datetime.date.today()
        if extension is None:
            extension = find_max_extension()['extension']


        self.name = name
        self.type = type
        self.language = language
        self.start = start
        self.path = path
        self.inside = find_max_extension()['files']
        self.description = description
        self.main = main
        self.version = version
        self.orderdate = orderdate
        self.maxextefile=extension

        self.is_exists()
        self.create_package_json()
        self.logging_setup()


    def create_package_json(self):
        data = self.file()
        with open("Docs.package.json", 'w') as f:
            json.dump(data, f, indent=2)

        os.system('type Docs.package.json')
        print(Fore.GREEN + 'has been created  Docs.package.json')

    def file(self):
        return {
            "name": self.name,
            "version": self.version,

            "description": self.description,
            "main": self.main,
            "type": self.type,
            "language": self.language,
            "scripts": {
                "start": self.start,
                "extension":self.maxextefile
            },
            "author": {
                "rootdir": NAME,
                "outdir": "/",
                "which": False,
            },
            "configpath": {
                "path": self.path,
                "inside": self.inside,
                'orderdate': str(self.orderdate),
            }
        }

    def logging_setup(self):
        time.sleep(2)
        config_dirs = [
            os.path.join(rootdir, "docs.config", "bin", "logging"),
            os.path.join(rootdir, "docs.config", "config"),
            os.path.join(rootdir, "docs.config", "data"),
            os.path.join(rootdir, "docs.config", "src")
        ]
        src_types = ['py', 'js', 'MD', 'c#', 'html']

        if not os.path.isdir(config_dirs[0]):
            print('Successfully created dir config')
            for dir_path in config_dirs:
                os.makedirs(dir_path, exist_ok=True)

            for file_type in src_types:
                os.makedirs(os.path.join(config_dirs[-1], file_type), exist_ok=True)

        log_dir_name = f"{datetime.date.today()}_{self.read_file_json()}"
        log_dir_path = os.path.join(config_dirs[0], log_dir_name)
        if not os.path.isdir(log_dir_path):
            os.makedirs(log_dir_path, exist_ok=True)

    def read_file_json(self):
        with open('Docs.package.json', 'r') as R_F:
            data = json.load(R_F)
            return data['name']

    def is_exists(self):
        loc=os.getcwd()
        lis=os.listdir(loc)
        if 'Docs.package.json' in lis:

            print(Fore.RED + 'file Docs.package.json is exists')


            exit()
        else:
            pass


import msvcrt

