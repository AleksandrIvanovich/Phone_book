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

checking_for_correctness_name()

# lenght_user_name = 20 
# name_str = 'имя'          
# name = (checking_for_correctness_name(name_str,lenght_user_name))

# lenght_user_surname = 40 
# name_str = 'фамилию'
# surname = (checking_for_correctness_name(name_str,lenght_user_surname))

# print(f'{name} {surname}')

