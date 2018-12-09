import view

def start():
    route = None
    menu_choice = view.router('main_menu')
    while True:
        route = int(input('Your Choice: '))
        while route not in menu_choice.keys():
            route = int(input('Your Choice: '))
        menu_choice = view.router(menu_choice[route])
