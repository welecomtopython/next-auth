import  json
import os

import datetime
import time

__path: str = os.path.abspath(__file__)
__var: str = __path.split('\\')[:-3]
rootdir =os.path.expanduser('~')

NAME = os.getcwd()
NAME = NAME.split('\\')[-1]
class FileConfing:
    def __init__(self,name=NAME , type:str="",language="",start="",path="",inside="",description="", main="",version='1.0.0'):
        with open("Docs.config.json",'w')as f:

            json.dump(self.file(
                type=type,
                language=language,
                start=start,
                path=path,
                inside=inside,
                description=description,
                main=main,
                version=version,
                name=name
                ),f,indent=2,)
        self.loggin()

        os.system('cat Docs.config.json')
    def file(self,
             type=""
             ,language="",
             start=".",
             path="",
             inside="",
             description="",
             main="",
             version='1.0.0',
             name=NAME):


        return {"name":name,
                "version":version,
                "description": description,
                "main": main,
                "type":type,
                "language":language,
                "scripts": {
                    "start": start},
                "author": {
                    "rootdir": "/",
                    "outdir": "/",
                    "which": False,
                },
                "configpath":{
                    "path":path,
                    "inside":inside
                }

                }

    def loggin(self):
        time.sleep(2)
        if not os.path.isdir(f"{rootdir}/docs.config/bin"):
            os.system(f"cd /d {rootdir}/docs.config && mkdir bin && cd /d bin && mkdir logging ")
        name=str(f"{datetime.date.today()}_{self.__reade_file_json()}")
        os.system(f"cd /d {rootdir}/docs.config/bin/logging && mkdir {name}")






    def __reade_file_json(self):
        with open('Docs.config.json','r')as R_F:
            name=json.load(R_F,)
            return name['name']




