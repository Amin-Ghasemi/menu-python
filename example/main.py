from menu import Menu
from time import sleep

items = ['Option 0', 'Option 1', 'Option 2', 'Option 3', 'Option 4', 'Exit']

while True:
    menu = Menu(items)

    output_panel = menu.load_menu()

    if output_panel == 0:
        print(f'You Selected Option -> {output_panel}')
        sleep(2)

    elif output_panel == 1:
        print(f'You Selected Option -> {output_panel}')
        sleep(2)

    elif output_panel == 2:
        print(f'You Selected Option -> {output_panel}')
        sleep(2)

    elif output_panel == 3:
        print(f'You Selected Option -> {output_panel}')
        sleep(2)

    elif output_panel == 4:
        print(f'You Selected Option -> {output_panel}')
        sleep(2)

    elif output_panel == 5:
        print(f"you exited...")
        menu.while_check[0] = False
        exit()
    else:
        pass
