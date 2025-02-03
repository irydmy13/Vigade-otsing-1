import random
import string

users = [] #список пользователей
passwords = [] #список паролей

#Создать пароль из 12 символов (случайный)
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
        any(c.isupper() for c in password) and
        any(c in ".,:;!_*-+()/#¤%&" for c in password))

#Регистрация нового пользователя
def registration():
    username=input("Введите логин: ")
    if username in users:
        print("Логин уже существует!")
        return

#Генерация пароля
    a=input("Сгенерировать пароль автоматически? (да/нет): ")
    if a.lower() =='да':
        password = create_pswd()
        print(f"Ваш пароль: {password}")
    else:
        while True:
            password = input("Введите пароль: ")
            if validate_pswd(password):
                break
            print("Пароль должен содержать цифры, буквы в нижнем и верхнем регистре и спецсимволы!")

    users.append(username)
    passwords.append(password)
    print("Регистрация прошла успешно!")

#Авторизация пользователя
def login():
    username=input("Введите логин: ")
    if username not in users:
        print("Пользователь не найден!")
        return

    password=input("Введите пароль: ")
    if passwords[users.index(username)] == password:
        print("Успешный вход!")
    else:
        print("Неправильный пароль!")

#Изменить логин/пароль
def editing():
    username=input("Введите ваш логин: ")
    if username not in users:
        print("Пользователь не найден!")
        return

    index = users.index(username)
    new_username = input("Введите новый логин: ")
    if new_username and new_username not in users:
        users[index] = new_username
        print("Логин успешно изменён!")

    new_password = input("Введите новый пароль: ")
    if new_password:
        while not validate_pswd(new_password):
            print("Пароль должен содержать цифры, спецсимволы, буквы нижнего и верхнего регистра!")
            new_password = input("Введите новый пароль: ")
        passwords[index] = new_password
        print("Пароль успешно изменён!")

#Востановить пароль
def reset_pswd():
    username = input("Введите логин: ")
    if username not in users:
        print("Пользователь не существует!")
        return

    index = users.index(username)
    new_password = create_pswd()
    passwords[index] = new_password
    print(f"Ваш новый пароль: {new_password}")
