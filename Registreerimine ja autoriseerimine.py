import MyModule

while True:
    print("\n1. �����������")
    print("2. �����������")
    print("3. ��������� ������/������")
    print("4. �������������� ������")
    print("5. �����")

    a = input("�������� ��������:")
    if a == '1':
        MyModule.registration()
    elif a == '2':
        MyModule.login()
    elif a == '3':
        MyModule.editing()
    elif a == '4':
        MyModule.reset_pswd()
    elif a == '5':
       print("����� �� ���������.")
       break
    else:
        print("�������� ����, ���������� �����.")
