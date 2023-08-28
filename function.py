def find_data():
    print('Введите имя файла: ')
    file_name = input()
    data = open(file_name + '.txt', 'r', encoding='utf-8')
    for line in data:
        print(line)
    data.close()

def new_data():
    print('Введите название нового файла: ')
    new_file_name = str(input())
    data = open(new_file_name + '.txt', 'w', encoding='utf-8')
    print('Введите ФИО и номер телефона(+7) через пробел: ')
    original_data = input()
    data.write(original_data)
    data.close()


def correction_data():
    print('Введите имя файла: ')
    file_name = input()
    data = open(file_name + '.txt', 'r', encoding='utf-8')
    print(data.read())
    data.close()

    data = open(file_name + '.txt', 'w', encoding='utf-8')
    print('Введите НОВЫЕ! ФИО и номер телефона(+7) через пробел: ')
    original_data = input()
    data.write(original_data)
    data.close()

def search_data(): # поиск контактов 
    print("Введите параметр поика\n 1 - Фамилия\n 2 - Имя\n 3 - Отчество\n 4 - Номер телефона")
    search = input()
    option = None
    if search == '1':
        print("Ведите Фамилию")
        option = input()
    elif search == '2':
        print("Ведите Имя")
        option = input()
    elif search == '3':
        print("Ведите Номер телефона")
        option = input()
    return search, option
    
# def delete_data(): # удаление данных
#     search_key = input("Введите имя или фамилию для удаления: ")
#     deleted = False

#     for contact in contacts:
#         if search_key.lower() in contact["last_name"].lower() or search_key.lower() in contact["first_name"].lower():
#             contacts.remove(contact)
#             deleted = True

#     if deleted:
#         print("Контакт успешно удален.")
#     else:
#         print("Контакт с указанным именем или фамилией не найден.")