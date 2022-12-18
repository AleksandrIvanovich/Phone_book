import json

# Создаём новый файл .json, если не найдет с указанным именем.
def create_json():
    """
    Функция проверяет, существует ли файл phone_file.json, если нет, то создаёт
    и располагает там пустой список json_data = [].
    """
    json_data = []
    with open('phone_file.json', 'w') as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))

# Добавляем в список файла новый контакт. Надо сделать русский язык!
def add_to_json(contact):
    """
    Функция добавляет в массив файла новый контакт
    Args:
        Создаём объект json, функция считывает 
        его под видом переменной contact и добавляет в список в файле phone_file.json
    """
    card = json.load(open('phone_file.json', encoding = 'utf-8'))
    card.append(contact)
    with open("phone_file.json", "w", encoding = 'utf-8') as file:
        return json.dump(card, file, indent=4, ensure_ascii=False)

contact_1 = {
    "id": 1,
    "sec_name": 'Тюрин', 
    "first_name": 'Роман',
    "tel_number": '+71238760789',
    "address": 'Нижний Новгород'
}

contact_2 = {
    "id": 2,
    "sec_name": 'Глазунов', 
    "first_name": 'Григорий',
    "tel_number": '+71938760789',
    "address": 'Ахтубинск'
}

contact_3 = {
    "id": 3,
    "sec_name": 'Чернов', 
    "first_name": 'Владимир',
    "tel_number": '+71238760789',
    "address": 'Муром'
}


# Считываем записанный файл и возвращаем список
def read_file_list():
    """
    Функция считывает из файла объекты json 
    и выводит их в виде списка.
    Returns:
        _type_: _description_
    """
    with open("phone_file.json", "r", encoding = 'utf-8') as read:

        # return print('\n'.join(map(str, json.load(read_file))))
        # return '\n'.join(map(str, json.load(read_file)))
        return json.load(read)
    
# print(read_file_list())
# print(type(read_file()))

#Поиск значения id в последнем заведённом контакте
def search_last_id():
    """
    Возвращает значение id в последнем заведённом контакте

    Returns:
        _type_: _description_
    """
    with open("phone_file.json", "r", encoding = 'utf-8') as file:
        cards = json.load(file)
        dict_card = cards[-1:]
        last_id = dict_card[0]
        last_id_2 = last_id['id']
    return last_id_2

# print(search_last_id())


def checking_for_correctness_name(arg1: str, lenght_str: int):
    
    # lenght_user_name = 20 
    name_str = 'имя'          
    # name = (checking_for_correctness_name(name_str,lenght_user_name))

    # lenght_user_surname = 40 
    name_str = 'фамилию'
    # surname = (checking_for_correctness_name(name_str,lenght_user_surname))

    while True:
        try:  
            arg1 = list(input(f'Введите {name_str}\n'))
            if len(arg1) > lenght_str:
                print('Вы вели слишком много символов')  
            else:  
                return (''.join(arg1)).capitalize()     
        except:  
            print('Вы ввели не строку!')
    
# tel_number = list(input('Введите номер телефона в формате +|Код страны|xxx|xxxxxxx|:\n'))

#Проверка корректности введённого номера телефона
def checking_for_correctness_of_input(arg: str) -> str:
    lenght_tel = len(arg)
    plus = arg[:1:lenght_tel-1]
    body_number = ''.join(arg[1:])
    result_str = ''
    if plus[0] != '+':
        print("Ошибка ввода! Начните вводить с '+'")  
    elif body_number.isdigit() != True:
        print("Ошибка ввода! Вы ввели не цифру!")
    elif len(body_number) > 17:
        print('Вы ввели слишком много цифр')
    else:
        result_str = ''.join(arg) 
    return result_str

 
# print(checking_for_correctness_of_input(tel_number))


def check_name(name) -> True:
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    a_2 = list(alphabet)
    i = name #list(input("Введите фамилию: "))
    for j in range(0, len(i)):
        if i[j] in a_2:
            j+=1
        else:
            # print('Вводить можно только русские буквы')
            return False


#Выводит на экран приглашение к заполнению данных и вводит в базу
def contact_input():
    """
    Просит пользователя ввести фамилию, имя, телефон и город,
    а потом заносит в базу данных

    """
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    a_2 = list(alphabet)
    id = search_last_id()+1 
    sec_name = str(input("Введите фамилию: "))
    if check_name(sec_name) == True:
        first_name = str(input("Введите имя: "))
        # tel_number = str(input("Введите номер телефона: "))
        tel_number = list(input('Введите номер телефона в формате +|Код страны|xxx|xxxxxxx|:\n'))
        address = str(input("Введите адрес: "))
        contact_n ={ 
                "id": id,
                "sec_name": sec_name, 
                "first_name": first_name,
                "tel_number": tel_number,
                "adress": address
            }

        return add_to_json(contact_n)
    else: 
        print('Вводить можно только русские буквы')

contact_input() #Выводит на экран приглашение к заполнению данных и вводит в базу


# create_json()

# add_to_json(contact_1) #Добавляем заданную карточку
# add_to_json(contact_2)
# add_to_json(contact_3)

# contact_input() #Выводит на экран приглашение к заполнению данных и вводит в базу

#Ищем по имени или фамилии. Выводит карточку полностью
def search_name(name):
    with open("phone_file.json", "r", encoding = 'utf-8') as file:
        cards = json.load(file)
        for i in range(0, len(cards)):
            if name == cards[i]['sec_name'] or name == cards[i]['first_name']:
                print(str(cards[i]))
                # print('\n'.join(map(str, (cards[i])))) #Показывает только ключ
                # print('\n'.join(str(cards[i]))) #Выстраивает в столбик все символы карточки

# search_name('Уваров')


