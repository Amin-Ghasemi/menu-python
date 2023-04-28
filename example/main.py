from menu import Menu

items = ['option 0', 'option 1', 'option 2', 'option 3', 'option 4', 'EXIT']

menu = Menu(items)

output_panel = menu.load_menu()

if output_panel == 0:
    print(f'You Selected Option -> {output_panel}')
elif output_panel == 1:
    print(f'You Selected Option -> {output_panel}')
elif output_panel == 2:
    print(f'You Selected Option -> {output_panel}')
else:
    exit()
