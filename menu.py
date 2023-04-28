import keyboard
from os import system
from time import sleep
from colorama import init, Fore, Back, Style

init(autoreset=True)

help_ = f'{Fore.BLUE}{Back.WHITE}Use UP(W) Or Down(S) Botton.'

def load_list_options(options:dict, selected_option:int):
    print('\n')
    list_options_str = ''
    for o in options:
        if o == selected_option:
            list_options_str += f"{Back.WHITE}{Fore.BLACK}{options.get(o)}{Back.BLACK}{Fore.WHITE}\n"
        else:
            list_options_str += f"{Back.BLACK}{Fore.WHITE}{options.get(o)}{Back.WHITE}{Fore.BLACK}\n"
    return list_options_str

def main_menu(list_options:list):
    system("clear")

    selected_option = -1
    
    options = {}
    for i in range(len(list_options)):
        options[i] = f'      [ {i} ] - {list_options[i]}'

    print(load_list_options(options, selected_option))
    print(help_)

    while True:
        key = keyboard.read_key()
        if key == 'up' or key.lower() == 'w':
            system('clear')
            if selected_option < 0:
                selected_option = len(list_options)
            else:
                selected_option -= 1
            print(load_list_options(options, selected_option))
            print(help_)
        elif key == "down" or key.lower() == 's':
            system('clear')
            if selected_option > len(list_options):
                selected_option = 0
            else:
                selected_option += 1
            print(load_list_options(options, selected_option))
            print(help_)
        elif key == 'enter':
            break
        sleep(.2)
    return selected_option

items = ['option 0', 'option 1', 'option 2', 'option 3', 'option 4', 'EXIT']

output_panel = main_menu(items)

if output_panel == 0:
    main_menu(items)

elif output_panel == 1:
    for i in range(5):
        print(i)
