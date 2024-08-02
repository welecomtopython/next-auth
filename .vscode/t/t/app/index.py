
# from add import Add
# from config import Config
# from get import Get
# from init import Init
# from set import Set
# from typing import Any

from app import (Add,Config,Get,Init,Set)
class App(Add,Config,Get,Init,Set):
    def __init__(self, args):
        matched = False
        for cls in App.__mro__:  # Skip the App class itself
            if cls.__name__ == args:
                cls.__init__(self, args)
                matched = True
                break
        if not matched:
            print(f"No matching class found for args: {args}")

    # Example usage


app_instance = App("Set")
