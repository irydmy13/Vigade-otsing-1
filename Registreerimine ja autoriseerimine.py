import MyModule

while True:
    print("\n1. Регистрация")
    print("\n2. Авторизация")
    print("\n3. Изменение логина/пароля")
    print("\n4. Восстановление пароля")
    print("\n5. Выход")

    a=input("Выберите действие:")
    if a=='1':
        MyModule.registration()
    elif a =='2':
        MyModule.login()
    elif a =='3':
        MyModule.editing()
    elif a =='4':
        MyModule.reset_pswd()
    elif a =='5':
       print("Выход из программы.")
       break
    else:
        print("Неверный ввод, попробуйте снова.")
