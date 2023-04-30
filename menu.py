import keyboard
from os import system
from time import sleep
from colorama import init, Fore, Back, Style
from typing import List

init(autoreset=True)

class Menu:
    def __init__(self, list_options:List[str]):
        self.list_options = list_options
        self.selected_option = -1
        self.options = {}
        self.while_check = [True]
        for i in range(len(list_options)):
            self.options[i] = f'     [ {i} ] - {list_options[i]}     '.center(50)

    def load_list_options(self) -> str:
        list_options_str = ''
        for o in self.options:
            if o == self.selected_option:
                list_options_str += f"{Back.LIGHTWHITE_EX}{Fore.BLACK}{self.options.get(o)}{Back.BLACK}{Fore.LIGHTWHITE_EX}\n"
            else:
                list_options_str += f"{Back.BLACK}{Fore.LIGHTWHITE_EX}{self.options.get(o)}{Back.LIGHTWHITE_EX}{Fore.BLACK}\n"
        return list_options_str

    def load_menu(self):
        system("clear")

        print(self.load_list_options())

        help_ = f'{Fore.BLUE}{Back.LIGHTWHITE_EX}Use UP(W) Or Down(S) Botton.'
        print(help_)

        while self.while_check[0]:
            key = keyboard.read_key()
            if key == 'up' or key.lower() == 'w':
                system('clear')
                if self.selected_option < 0:
                    self.selected_option = len(self.list_options)-1
                else:
                    self.selected_option -= 1
                print(self.load_list_options())
                print(help_)
            elif key == "down" or key.lower() == 's':
                system('clear')
                if self.selected_option >= len(self.list_options):
                    self.selected_option = 0
                else:
                    self.selected_option += 1
                print(self.load_list_options())
                print(help_)
            elif key == 'enter':
                # self.while_check[0] = False
                return self.selected_option
            sleep(.2)

        return self.selected_option
