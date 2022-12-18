import colorama
from colorama import Fore, Back, Style
colorama.init()

def first_name_f ():

    print(Fore.GREEN)
    first_name_def=input('Введите имя (не более 20 букв) :') 
    return first_name_def

def sec_name_f ():
    print(Fore.YELLOW)
    sec_name_def=input('Введите фамилию (не более 40 букв) :')
    return sec_name_def

def tel_namber_1_f():
    print(Fore.CYAN)
    tel_namber_1_def=input('Введите телефон в виде (+71234567899) :')
    return tel_namber_1_def

def adress_1_f():
    print(Fore.MAGENTA)
    adress_1_def=input('Введите адрес в виде (город улица дом корпус квартира) :')
    return adress_1_def

#проверка
# print()

# first_name=first_name_f()

# sec_name=sec_name_f()

# tel_namber_1=tel_namber_1_f()

# adress_1=adress_1_f()

# print(Style.RESET_ALL)



