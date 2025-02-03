import random
import string

users = [] #список пользователей
passwords = [] #список паролей

def create_pswd():
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0 + str1 + str2 + str3
    ls = list(str4)
    return ''.join(random.choice(ls) for _ in range(12))

#Проверка пароля на содержание цифры, буквы в нижнем и верхнем регистре и спецсимволы
def validate_pswd(password):
    return (
        any(c.isdigit() for c in password) and
        any(c.islower() for c in password) and
        any(c in ".,:;!_*-+()/#¤%&" for c in password))

#Регистрация нового пользователя
def registration():
    username=input("Введите логин: ")
    if username in users:
        print("Логин уже существует!")
        return

    a=input("Сгенерировать пароль автоматически? (да/нет): ")
    if a.lower() =='да':
        password = validate_pswd()
        print(f"Ваш пароль: {password}")
    else:
        while True:
            password = input("Введите пароль: ")
            if validate_pswd(password):
                break
            print("Пароль должен содержать цифры, буквы в нижнем и верхнем регистре и спецсимволы!")

