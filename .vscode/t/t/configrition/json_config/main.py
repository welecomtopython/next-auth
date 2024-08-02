import weakref

class MyClass:
    def __init__(self, value):
        self.value = value
    def __del__(self):
        print(f'{self} is being deleted')

obj = MyClass(10)
weak_ref = weakref.ref(obj)

print(weak_ref)      # <weakref at 0x...; to 'MyClass' at 0x...>
print(weak_ref())    # <__main__.MyClass object at 0x...>
