todo_list = []
options = ['Add tasks', 'View tasks', 'Delete task', 'Quit']

def display_menu(options):
    '''Displays the todo list menu'''

    menu_header = f'{"=" * 10} Todo list {"=" * 10}'
    menu_options = '\nPlease select an option'

    for index, option in enumerate(options):
        menu_options += f'\n{index + 1}) {option}'

    menu_display = f'{menu_header} \n {menu_options} \n'
    print(menu_display)

def display_todo_list():
    '''Displays the todo list'''

    todo_display = ''
    if not todo_list:
        print('\nThere aren\'t any todo list items yet!')

    for index, task in enumerate(todo_list):
        todo_display += f'\n{index + 1}) {task}'

    print(todo_display)

def add_todo_list_item(todo_item):
    '''Adds a todo list item to the todo list'''

    todo_list.append(todo_item.title())

def remove_todo(todo_item):
    '''Removes a todo list item from the todo list'''

    if not todo_item in todo_list:
        print('\nThat todo list item isn\'t in the todo list!')

    if todo_item in todo_list:
        todo_list.remove(todo_item)

def main():
    display_menu(options)

    while True:
        try:
            menu_option_number = int(input('\nPlease enter a menu option number: '))

            if menu_option_number == 1:
                todo_item = input('\nPlease provide the todo you would like to add: ')
                add_todo_list_item(todo_item)
            elif menu_option_number == 2:
                display_todo_list()
            elif menu_option_number == 3:
                removed_todo = input('\nPlease enter the todo item you would like to delete: ').title()
                remove_todo(removed_todo)
            elif menu_option_number == 4:
                exit()
    
        except ValueError:
            print(f'Please select a valid number between 1-{len(options)}')


if __name__ == '__main__':
    main()
