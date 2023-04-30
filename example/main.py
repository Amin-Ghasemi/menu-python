from menu import Menu

items = ['option 0', 'option 1', 'option 2', 'option 3', 'option 4', 'option 5']

menu = Menu(items)

output_panel = menu.load_menu()

if output_panel == 0:
    print(f'You Selected Option -> {output_panel}')

elif output_panel == 1:
    print(f'You Selected Option -> {output_panel}')

elif output_panel == 2:
    print(f'You Selected Option -> {output_panel}')

elif output_panel == 3:
    print(f'You Selected Option -> {output_panel}')

elif output_panel == 4:
    print(f'You Selected Option -> {output_panel}')

elif output_panel == 5:
    print(f"you exited...")
    menu.while_check[0] = False
    exit()
else:
    pass
