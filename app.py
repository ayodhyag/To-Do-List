user_input = 'random'
data = []

def show_menu():
    print('-----------------')
    print('     MENU :      ')
    print('1. Add an Item')
    print('2. Mark as Done')
    print('3. View Items')
    print('4. Exit')
    print('-----------------')

while user_input != '4':

    show_menu()
    print('')
    user_input = input('Enter your choice: ')

    if user_input == '1':
        item = input('What is to be done? ')
        print('-----------------')
        data.append(item)
        print('added item: ', item)
    
    elif user_input =='2':
        item = input('What is to be marked as done? ')
        print('-----------------')
        if item in data:
            data.remove(item)
            print('Removed item: ', item)
        else:
            print('Item does not exist in the list')
   
    elif user_input =='3':
        print('List of To-do Items:')
        for item in data:
            print(item)
   
    elif user_input =='4':
        print('goodbye')
    
    else:
        print('please enter one of 1,2,3 or 4')