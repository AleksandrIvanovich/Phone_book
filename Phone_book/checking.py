def checking_for_correctness_name(arg1: str, lenght_str: int):
    while True:
        try:  
            arg1 = list(input(f'Введите {name_str}\n'))
            if len(arg1) > lenght_str:
                print('Вы вели слишком много символов')  
            else:  
                return (''.join(arg1)).capitalize()     
        except:  
            print('Вы ввели не строку!')
            
lenght_user_name = 20 
name_str = 'имя'          
name = (checking_for_correctness_name(name_str,lenght_user_name))

lenght_user_surname = 40 
name_str = 'фамилию'
surname = (checking_for_correctness_name(name_str,lenght_user_surname))

# print(f'{name} {surname}')

import database 

# def contact_input():
#     """
#     Просит пользователя ввести фамилию, имя, телефон и город,
#     а потом заносит в базу данных

#     """
#     id = 22 #Не придумал, как обратиться к последнему элементу, вытащить значение id и прибавить 1
#     sec_name = str(input("Введите фамилию: "))
#     first_name = str(input("Введите имя: "))
#     tel_number = str(input("Введите номер телефона: "))
#     adress = str(input("Введите адрес: "))
#     contact_n ={ 
#         "id": id,
#         "sec_name": sec_name, 
#         "first_name": first_name,
#         "tel_number": tel_number,
#         "adress": adress
#     }
#     return add_to_json(contact_n)