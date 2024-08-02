class Add:
    def __init__(self, args):

        print(f"{self.__class__.__name__} initialized with args:", args)

class Config:
    def __init__(self, args):

        print(f"{self.__class__.__name__} initialized with args:", args)

class Get:
    def __init__(self, args):

        print(f"{self.__class__.__name__} initialized with args:", args)

class Init:
    def __init__(self, args):
        print(f"{self.__class__.__name__} initialized with args:", args)

class Set:
    def __init__(self, args):

        print(f"{self.__class__.__name__} initialized with args:", args)

    def set(self):
        print("Set method called")

class App(Add, Config, Get, Init, Set):
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
app_instance = App("Add")
