import keyboard
from os import system
from time import sleep
from colorama import init, Fore, Back, Style
from typing import List
import shutil
import platform

init(autoreset=True)

class Menu:
    def __init__(self, list_options:List[str]):
        self.list_options = list_options
        self.selected_option = 0
        self.options = {}
        self.while_check = [True]
        self.console_size = shutil.get_terminal_size()
        self.console_width = self.console_size.columns

        for i in range(len(list_options)):
            self.options[i] = f'{list_options[i]}'.center(self.console_width)


    def clear(self):
        if platform.system() == 'Windows':
            system('cls')
        elif platform.system() == 'Linux':
            system('clear')
            system("stty -echo")
        else:
            pass

    def load_list_options(self) -> str:
        list_options_str = ''
        for o in self.options:
            if o == self.selected_option:
                list_options_str += f"{Back.LIGHTWHITE_EX}{Fore.BLUE}{self.options.get(o)}{Back.BLUE}{Fore.LIGHTWHITE_EX}\n"
            else:
                list_options_str += f"{Back.BLUE}{Fore.LIGHTWHITE_EX}{self.options.get(o)}{Back.LIGHTWHITE_EX}{Fore.BLUE}\n"

        return list_options_str

    def load_menu(self):
        self.clear()

        print(self.load_list_options())

        help_ = f'{Fore.LIGHTWHITE_EX}{Back.BLUE}Use Left < Or > Right and Space for Select'
        print(help_)

        while self.while_check[0]:
            key = keyboard.read_key()
            if key == 'left' or key.lower() == 'w':
                self.clear()
                if self.selected_option < 0:
                    self.selected_option = len(self.list_options)-1
                else:
                    self.selected_option -= 1
                print(self.load_list_options())
                print(help_)
            elif key == "right" or key.lower() == 's':
                self.clear()
                if self.selected_option >= len(self.list_options):
                    self.selected_option = 0
                else:
                    self.selected_option += 1
                print(self.load_list_options())
                print(help_)
            elif key == 'space':
                if platform.system() == 'Windows':
                    pass
                elif platform.system() == 'Linux':
                    system("stty -echo")
                else:
                    pass

                return self.selected_option
            sleep(.1)

        return self.selected_option
