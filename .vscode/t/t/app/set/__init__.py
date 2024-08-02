from event import help

import os
from event.config import FileConfing

import sys
HOME: set = os.path.expanduser('~')

HOME="{}/docs.config".format(HOME)

import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

class Set:
    def __init__(self, args):
        print("Set initialized with args:", args)

    def set(self):
        print("Set method called")


    #
    #     if not  args:
    #
    #         print(help.set())
    #         print('-'*50)
    #         print('exit cod 0')
    #         sys.exit(0)
    #     if len(args) == 1:
    #         if args[0]=='new' or '-n':
    #             print('new'*50)
    #             print(args[0])
    #             N=self.getname()
    #             FileConfing(name=N['name_prject'],main=N['language_prog'],path=f"{HOME}/docs.config/{N['language_prog']}")
    #
    #         else:
    #             pass
    #
    #~
    #
    #
    #
    #
    #
    #
    #
    #
    # def getname(self):
    #
    #     name_prject = str(input("Whait is Name Project : "))
    #
    #     language_prog = str(input(f"Whait is language progrming {os.listdir(str(f'{HOME}/src'))}: "))
    #
    #     if not language_prog in os.listdir(str(f'{HOME}/src')):
    #         print(" nem folder not fonund")
    #         print(f"{language_prog}  not in found in  {os.listdir(str(f'{HOME}/src'))}")
    #         self.getname()
    #         print('reucurtio lin 51')
    #
    #     elif language_prog in os.listdir(str(f'{HOME}/src/{language_prog}')):
    #         print('language_prog  lin 54')
    #         any_type = str(input(f"Whait is any type or inside folder {os.listdir(str(f'{HOME}/src/{language_prog}'))} : "))
    #         if not  any_type in os.listdir(str(f'{HOME}/src/{language_prog}')):
    #             os.system(f'cd /d {HOME}/src/{language_prog} && mkdir {any_type}')
    #     else:
    #         any_type = str(input(f"Whait is Newo type or inside folder {os.listdir(str(f'{HOME}/src/{language_prog}'))} : "))
    #         if not any_type in os.listdir(str(f'{HOME}/src/{language_prog}')):
    #             os.system(f'cd /d {HOME}/src/{language_prog} && mkdir {any_type}')
    #
    #     print( {'name_prject': name_prject, 'language_prog': language_prog, 'any_type': any_type})
    #     return  {'name_prject': name_prject, 'language_prog': language_prog, 'any_type': any_type}
