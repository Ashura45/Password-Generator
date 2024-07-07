import random


def generate_it_again():
    pass


def opc():
    long = int(input('Напишите длину пароля: '))
    with_num = input('Пароль будет с цифрами? y or n: ').lower()
    with_letters = input('Пароль будет с буквами? y or n: ').lower()
    if with_num != 'y' or with_num != 'n' and with_letters != 'y' or with_num != 'n':
        return long, with_num == 'y', with_letters == 'y'
    else:
        while with_num != 'y' or with_num != 'n' and with_letters != 'y' or with_num != 'n':
            print('Только y or n')
            with_num = input('Пароль будет с цифрами? y or n: ').lower()
            with_letters = input('Пароль будет с буквами? y or n: ').lower()
    return long, with_num == 'y', with_letters == 'y'


def password_generator():
    long, with_num, with_letters = opc()
    password = ''
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

    return password


print(password_generator())



