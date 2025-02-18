import MyModule

while True:
    print("\n1. Регистрация")
    print("2. Авторизация")
    print("3. Изменение логина/пароля")
    print("4. Восстановление пароля")
    print("5. Выход")

    a = input("Выберите действие:")
    if a == '1':
        MyModule.registration()
    elif a == '2':
        MyModule.login()
    elif a == '3':
        MyModule.editing()
    elif a == '4':
        MyModule.reset_pswd()
    elif a == '5':
       print("Выход из программы.")
       break
    else:
        print("Неверный ввод, попробуйте снова.")
