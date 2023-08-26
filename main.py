import json
import interface
import database_module


def run():
    
    while True:
    
        command = interface.start_page()

        match command:
            case '1':     # Список всех контактов
                data = database_module.get_all_contacts()
                interface.show_contacts(data)

            case '2': # Поиск контакта
                user_search = interface.search_contact()
                data = database_module.get_contact_info(user_search)
                interface.show_contacts(data)
            
            case '3': # Добавить контакт
                new_contact = interface.add_contact()
                database_module.add_contacts(new_contact)
                interface.done_message()

            case '4': # Изменить 
                data = database_module.get_all_contacts()
                interface.show_contacts(data)
                deal_id = interface.change_contact()
                one_contact = database_module.get_one_contact(deal_id)
                changed_contact = interface.change_contact_content(one_contact)
                if changed_contact['comment'] == 'Ой, я что-то нажал и всё сломалось':
                    database_module.delete_contact(changed_contact['contact_id'])
                else:
                    database_module.change_contact(changed_contact)
            
            case '5': # Импорт
                user_choice = interface.import_contacts()
                if user_choice == 'json':
                    data = import_json('import_phonebook.json')
                    database_module.add_contacts(data)
                    interface.result_mess(True)
                else:
                    interface.error_input()
                
            case '0': # Выход
                interface.bye_mess()
                break
            
            case _:
                interface.error_input()


def change_action(user_answer: dict):
    match user_answer['user_choise']:
        case 1: # завершить
            return
        
        case 2: # изменить
            return

        case 3: # удалить
            return


    
def import_json(path_to_import_json_file):
    data = [] # список словарей который получим при преобразовании      
    with open(path_to_import_json_file, 'r', encoding='UTF-8') as file: #открываем файл на чтение
        data = json.load(file) #загружаем из файла данные в словарь data
        for i in range(0, len(data)): 
            d1 = {'contact_id': ''}
            data[i], d1 = d1, data[i]
            data[i].update(d1)
    return data

run()