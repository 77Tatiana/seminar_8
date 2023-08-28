from function import find_data, new_data, correction_data, search_data, delete_contact

def main_menu():
    print('Выберите, какую команду необходимо выполнить:\n'
        '1 - найти запись\n'
        '2 - новая запись\n'
        '3 - редактирование записи\n'
        '4 - удаление записи\n'
        '5 - выйти из программы\n')

    while True:
        mode = int(input('Введите номер команды (1-5): '))
        if mode not in [1, 2, 3, 4, 5]:
            print('Неверный номер, попробуйте еще раз ')
        elif mode == 1:
            find_data()
        elif mode == 2:
            new_data()
        elif mode == 3:
            correction_data()
        elif mode == 4:
            delete_data()
        elif mode == 5:
            print('До свидания!')
            return
main_menu()    