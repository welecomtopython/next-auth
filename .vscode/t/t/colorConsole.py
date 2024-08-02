import colorama
from colorama import Fore, Back, Style

# Initialize colorama
colorama.init()

# Print text in different colors
print(Fore.RED + 'This text is red')
print(Fore.GREEN + 'This text is green')
print(Fore.BLUE + 'This text is blue')
print(Fore.YELLOW + 'This text is yellow')

# Reset to default color
print(Style.RESET_ALL)

# Print text with background color
print(Back.CYAN + 'This text has a cyan background')

# Reset to default background
print(Style.RESET_ALL)

# Combine foreground and background colors
print(Fore.BLACK + Back.WHITE + 'This text is black with white background')

# Reset to default colors
print(Style.RESET_ALL)
