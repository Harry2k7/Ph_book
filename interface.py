import time
import art
from art import *  # библиотека для работы с ascii артом


def error_input():
    print('Ошибка!' + art("error"))
    print('Пожалуйста введите команду соответствующую пункту меню.')
    time.sleep(1)


def done_message():
    print('Выполнено!' + art("cat4"))


main_menu = \
    '   *** Меню телефонного справочника ***\n\
    1. Просмотр списка контактов\n\
    2. Поиск контакта\n\
    3. Добавление нового контакта\n\
    4. Изменение или удаление контакта\n\
    5. Импорт контактов\n\
    0. Выход из приложения'


def start_page():  # стартовая страница
    print(main_menu)
    print(50 * "═")
    print()
    command = input('Введите номер команды: >  ')
    print(50 * "_")
    return command


def show_contacts(data):  # 1 in menu
    if data != []:
        print('Список контактов:')
        for item in range(len(data)):
            a = data[item]['contact_id']
            b = data[item]['surname']
            c = data[item]['name']
            d = data[item]['patronymic']
            e = data[item]['phone']
            f = data[item]['comment']
            print(f'{a}) {b} {c} {d} | {e} | {f} |')
    else:
        print('Список контактов пуст')


def search_contact():
    search_request = input('Введите данные для поиска: ')
    print(50 * "=")
    return search_request


def add_contact():
    print('Добавление контакта')
    print(50 * "-")
    contact_surname = input('Введите фамилию: ')  
    contact_name = input('Введите имя: ') 
    contact_patronymic = input('Введите отчество: ') 
    contact_number = input('Введите номер телефона: ')
    commentary = input('Комментарий: ')
    contact = [{'contact_id': '', 'surname': contact_surname, 'name': contact_name, 'patronymic': contact_patronymic, 'phone': contact_number,
                'comment': commentary}, ]
    return contact  # возвращение списка словаря


def change_contact():
    print('Изменить контакт:')
    print(50 * "~")
    contact_id = input('Выберите контакт для внесения изменений: ')
    return int(contact_id)


def change_contact_content(one_contact):
    while True:
        menu_command = input('Что необходимо сделать?\n 1 - Изменить содержание \n 2 - Удалить контакт\n')
        if menu_command == '1':
            print('Изменить содержание контакта:')
            while True:
                submenu_command = input(
                    'Что необходимо изменить?\n 1 - Изменить фамилию \n 2 - Изменить имя\n 3 - Изменить отчество\n 4 - Изменить номер телефона\n 5 - Изменить комментарий\n')
                match submenu_command:
                    case '1':  # Изменить фамилию
                        print('Введите фамилию: ')
                        one_contact['surname'] = input()
                        done_message()
                        break
                    case '2':  # Изменить имя
                        print('Введите имя: ')
                        one_contact['name'] = input()
                        done_message()
                        break
                    case '3':  # Изменить отчество
                        print('Введите отчество: ')
                        one_contact['patronymic'] = input()
                        done_message()
                        break
                    case '4':  # Изменить номер телефона
                        print('Введите номер телефона: ')
                        one_contact['phone'] = str(input())
                        done_message()
                        break
                    case '5':  # Изменить комментарий
                        print('Введите комментарий: ')
                        one_contact['comment'] = input()
                        done_message()
                        break
                    case _:
                        error_input()
            break
        elif menu_command == '2':
            one_contact['comment'] = 'Ой, я что-то нажал и всё сломалось'  # удаление по ID
            done_message()
            break
    return one_contact


def bye_mess():  # 0 in menu
    print('Работа завершена!')


def import_contacts():
    print('Импорт контактов: ')
    import_type = 'json'
    return import_type


def result_mess(done):
    if done:
        done_message()
    else:
        print('Произошла ошибка при выполнении операции!' + art("error"))