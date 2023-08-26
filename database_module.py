import json

path_to_db = 'phonebook.json'

def get_all_contacts():  # Возвращает весь список контактов из файла phonebook.json
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        data = [data[i] for i in range(0, len(data))]
    return data

def get_one_contact(contact_id_get): # Возвращает один контакт по его contact_id
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)
        one_contact_get = {}
        for i in range(0, len(data)): 
            if contact_id_get == data[i]['contact_id']:
                one_contact_get = data[i]
                break
    return one_contact_get

def get_contact_info(contact_info_get): # Возвращает контакты по вхождению в значение любого из ключей surname, name, patronymic, phone, comment
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы
        data = json.load(file)
        info_contact_get = []

        for i in range(0, len(data)): 
            if  contact_info_get.lower() in data[i]['surname'].lower():
                info_contact_get.append(data[i])
            elif contact_info_get.lower() in data[i]['name'].lower():
                info_contact_get.append(data[i])
            elif contact_info_get.lower() in data[i]['patronymic'].lower():
                info_contact_get.append(data[i])
            elif contact_info_get.lower() in data[i]['phone'].lower():
                info_contact_get.append(data[i])
            elif contact_info_get.lower() in data[i]['comment'].lower():
                info_contact_get.append(data[i])
 
    return info_contact_get

def add_contacts(contacts_new_dict):  # Добавление новых контактов в БД
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы
        data = json.load(file)            
        for i in range(0, len(contacts_new_dict)): 
            contacts_new_dict[i]['contact_id'] = data[len(data)-1]['contact_id'] + 1
            data.append(contacts_new_dict[i])     # Добавляем в список словарей новый контакт   
    with open(path_to_db, 'w', encoding='UTF-8') as file: # Записываем в базу данных обновленный список словарей
        json.dump(data, file, indent=4)

def change_contact(contact_edit):  # Изменение контакта
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)

        for i in range(0, len(data)): # Для изменения контакта c conroct_id = 4, находим в БД словарь с contact_id = 4 и перезаписываем его.
            if contact_edit['contact_id'] == data[i]['contact_id']:
                data[i] = contact_edit
        
    with open(path_to_db, 'w', encoding='UTF-8') as file: # Записываем в базу данных обновленный список словарей
        json.dump(data, file, indent=4)    

def delete_contact(contact_id_delete): # Удаление контакта в БД по его contact_id
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)
                  
        for i in range(0, len(data)): 
            if data[i]['contact_id'] == contact_id_delete: # находим индекс элемента в списке словарей с нужным deal_id
                index_del = i
                break
        data.pop(index_del)   # Удаляем из списка словарь с нужным contact_id
        for i in range(0, len(data)): # Перезаписаваем в каждом словаре списка ключ contact_id
            data[i]['contact_id'] = i+1
    with open(path_to_db, 'w', encoding='UTF-8') as file: # Записываем в базу данных обновленный список словарей
        json.dump(data, file, indent=4)    

def clear_db(path_to_db): # Очистка базы данных
    first_element = [{'id_counter': 0}, ]
    with open(path_to_db, 'w') as file:
        json.dump(first_element, file, indent=4)