# colorama_demo.py
from colorama import init, Fore, Back, Style
import keyboard
from time import sleep
from os import system

# Initializes Colorama
init(autoreset=True)

options = ['[ 1 ]', '[ 2 ]']

print(f"""{Back.WHITE}{Fore.BLACK}{options[0]}\n{Back.BLACK}{Fore.WHITE}{options[1]}
""")

while True:
    key = keyboard.read_key()
    if key == 'up':
        system("cls")
        print(f"""{Back.WHITE}{Fore.BLACK}{options[0]}\n{Back.BLACK}{Fore.WHITE}{options[1]}""")
    elif key == "down":
        system("cls")
        print(f"""{Back.BLACK}{Fore.WHITE}{options[0]}\n{Back.WHITE}{Fore.BLACK}{options[1]}""")
    
