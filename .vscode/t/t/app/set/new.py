import os

__path: str = os.path.abspath(__file__)

__hom: set = os.path.expanduser('~')
__var: str = __path.split('\\')[:-3]
root = '\\'.join(__var)

__bin = __path.split('\\')[:-1]
root_bin = '\\'.join(__bin)
print(os.listdir(str(f'{root}/src/py')))
def getname():

    name_prject=str(input("Whait is Name Project : "))

    language_prog=str(input(f"Whait is language progrming {os.listdir(str(f'{root}/src'))}: "))

    if not language_prog in os.listdir(str(f'{root}/src')):
        print(f"{language_prog} in not in {os.listdir(str(f'{root}/src'))}")
        getname()

    any_type=str(input(f"Whait is any type or inside folder {os.listdir(str(f'{root}/src/{language_prog}'))} : "))

    return {'name_prject':name_prject,'language_prog':language_prog,'any_type':any_type}


def New():...


# print(getname())