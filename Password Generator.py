import random

def opc():
    try:
        long = int(input('Напишите длину пароля. пароль должен быть больше 3 : '))
        if long <= 3:
            long = 4
    except ValueError:
        print('Только цифры')
        while True:
            try:
                long = int(input('Напишите длину пароля. пароль должен быть больше 3 : '))
                if long <= 3:
                    long = 4
                    break
                elif long > 3:
                    break
            except ValueError:
                print('Только цифры')
    with_num = input('Пароль будет с цифрами? y or n: ').lower()
    with_letters = input('Пароль будет с буквами? y or n: ').lower()
    if with_num == 'y' or with_num == 'n' and with_letters == 'y' or with_num == 'n':
        return long, with_num == 'y', with_letters == 'y'
    else:
        while with_num != 'y' and with_num != 'n' and with_letters != 'y' and with_num != 'n':
            print('Только y or n')
            with_num = input('Пароль будет с цифрами? y or n: ').lower()
            with_letters = input('Пароль будет с буквами? y or n: ').lower()
    return long, with_num == 'y', with_letters == 'y'


def password_generator():
    long, with_num, with_letters = opc()
    password = ''
    password_list = []
    generate_it_again = 'y'
    while generate_it_again == 'y':
        if with_num and with_letters:
            for i in range(long):
                j = random.randint(0, 1)
                j_ = random.randint(0, 1)
                if j == 1:
                    x = random.randint(48, 57)
                else:
                    x = random.randint(97, 122)
                if j_ == 1:
                    password = password + chr(x).upper()
                else:
                    password = password + chr(x)

        elif with_letters:
            for i in range(long):
                j = random.randint(0, 1)
                x = random.randint(97, 122)
                if j == 1:
                    password = password + chr(x).upper()
                else:
                    password = password + chr(x)
        elif with_num:
            for i in range(long):
                x = random.randint(48, 57)
                password = password + chr(x)

        password_list.append(password)
        print(password, 'текущий пароль. сгенерировать заново?')
        print(f'Предыдущие пароли:', ', '.join(password_list))
        generate_it_again = input('сгенерировать заново? y or n: ')
        if generate_it_again == 'n':
            return ', '.join(password_list)
        elif generate_it_again == 'y':
            new_setting = input('Изменить настройки? y or n')
            if new_setting == 'y':
                password = ''
                long, with_num, with_letters = opc()
            else:
                password = ''
        else:
            print('Только y or n')
            generate_it_again = input('сгенерировать заново с текущими настройками? y or n')


print(password_generator())


