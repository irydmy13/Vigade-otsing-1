import time

users = {} #База данных для хранения пользователей

def send_email_confirmation(email):
    """ Отправка письма для подтверждения email. """
    print(f"На email '{email}' отправлено письмо для подтверждения.")
    time.sleep(1)
    return True  # Предположим, что подтверждение всегда успешно

def registration():
    """ Процесс регистрации нового пользователя. """
    print("Регистрация:")
    while True:
        name = input("Введите ваше имя: ")
        email = input("Введите email: ")
        password = input("Введите пароль: ")

        if email in users:
            print("Этот email уже зарегистрирован, попробуйте другой.")
            continue

        print("Письмо для подтверждения отправлено на ваш email.")
        confirmed = send_email_confirmation(email)

        if confirmed:
            print("Email подтвержден успешно!")
            users[email] = {"name": name, "password": password}
            print("Регистрация завершена!")
            return True
        else:
            print("Email не подтвержден. Повторите регистрацию.")
            continue

def login():
    """
    Процесс авторизации пользователя.
    """
    print("Авторизация:")
    attempts = 3
    while attempts > 0:
        email = input("Введите email: ")
        password = input("Введите пароль: ")

        if email in users and users[email]["password"] == password:
            print("Успешная авторизация!")
            print("Перенаправление на главный экран...")
            return True
        else:
            attempts -= 1
            print(f"Неверные данные. Осталось попыток: {attempts}")
            if attempts == 0:
                print("Превышено количество попыток. Попробуйте позже.")
                return False

def main():
    """
    Основной процесс программы, который запускает логику блок-схемы.
    """
    print("Добро пожаловать на веб-страницу!")
    while True:
        registered = input("Вы зарегистрированы? (yes/no): ").lower()
        if registered == "yes":
            success = login()
            if success:
                break  #Завершение программы после успешного входа
        elif registered == "no":
            registration()
        else:
            print("Пожалуйста, введите 'yes' или 'no'.")

    print("Конец программы.")

if __name__ == "__main__":
    main()
