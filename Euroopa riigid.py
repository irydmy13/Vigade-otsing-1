import random

# Чтение данных из файла и загрузка их в словарь
with open('riigid_pealinnad.txt', 'r', encoding='utf-8') as file:
    countries_and_capitals = {}  # Словарь для хранения страны и её столицы
    for line in file:
        country, capital = line.strip().split('-')  # Разделяем строку на страну и столицу
        countries_and_capitals[country] = capital  # Заполняем словарь

# Функция для отображения столицы по названию страны
def get_capital_by_country():
    country = input("Введите название страны: ")  # Запрашиваем у пользователя страну
    print(countries_and_capitals.get(country, "Эта страна не найдена в словаре."))  # Выводим столицу или сообщение об ошибке

# Функция для отображения страны по названию столицы
def get_country_by_capital():
    capital = input("Введите название столицы: ")  # Запрашиваем у пользователя столицу
    for country, cap in countries_and_capitals.items():
        if cap == capital:  # Ищем столицу и выводим страну
            print(country)
            return
    print("Эта столица не найдена в словаре.")  # Если столица не найдена

# Функция для добавления новой пары страна-столица
def add_new_entry():
    country = input("Введите название новой страны: ")  # Запрашиваем страну
    capital = input("Введите столицу этой страны: ")  # Запрашиваем столицу
    countries_and_capitals[country] = capital  # Добавляем новую пару в словарь
    print(f"Страна {country} и столица {capital} добавлены в словарь.")

# Функция для исправления ошибки в словаре
def correct_entry():
    country = input("Введите страну, которую хотите исправить: ")  # Запрашиваем страну для исправления
    if country in countries_and_capitals:  # Проверяем, есть ли эта страна в словаре
        new_capital = input(f"Введите правильную столицу для {country}: ")  # Запрашиваем новую столицу
        countries_and_capitals[country] = new_capital  # Заменяем старую столицу на новую
        print(f"Столицу для {country} изменили на {new_capital}.")
    else:
        print(f"Страна {country} не найдена в словаре.")  # Если страна не найдена в словаре

# Функция для теста на знания стран и столиц
def knowledge_test():
    correct_answers = 0
    total_questions = 5  # Количество вопросов в тесте

    for _ in range(total_questions):
        question_type = random.choice(['country', 'capital'])  # Случайным образом выбираем тип вопроса

        if question_type == 'country':
            country = random.choice(list(countries_and_capitals.keys()))  # Случайная страна
            answer = input(f"Какая столица у страны {country}? ")  # Спрашиваем столицу
            if answer.lower() == countries_and_capitals[country].lower():  # Проверяем ответ
                print("Правильно!")
                correct_answers += 1
            else:
                print(f"Неправильно! Правильный ответ: {countries_and_capitals[country]}")
        else:
            capital = random.choice(list(countries_and_capitals.values()))  # Случайная столица
            answer = input(f"Какая страна имеет столицу {capital}? ")  # Спрашиваем страну
            country = [k for k, v in countries_and_capitals.items() if v == capital][0]  # Находим страну по столице
            if answer.lower() == country.lower():  # Проверяем ответ
                print("Правильно!")
                correct_answers += 1
            else:
                print(f"Неправильно! Правильный ответ: {country}")

    print(f"Вы ответили правильно на {correct_answers} из {total_questions} вопросов.")
    print(f"Ваш результат: {correct_answers * 100 / total_questions:.2f}%")  # Выводим процент правильных ответов

# Основное меню программы
while True:
    print("\nВыберите опцию:")
    print("1 - Отобразить столицу по названию страны")
    print("2 - Отобразить страну по названию столицы")
    print("3 - Добавить новую пару страна-столица")
    print("4 - Исправить ошибку в словаре")
    print("5 - Проверить знания")
    print("0 - Выйти")

    choice = input("Ваш выбор: ")

    if choice == '1':
        get_capital_by_country()  # Выбор отображения столицы по стране
    elif choice == '2':
        get_country_by_capital()  # Выбор отображения страны по столице
    elif choice == '3':
        add_new_entry()  # Добавление новой пары страна-столица
    elif choice == '4':
        correct_entry()  # Исправление ошибки
    elif choice == '5':
        knowledge_test()  # Тест на знание столиц и стран
    elif choice == '0':
        break  # Выход из программы
    else:
        print("Неверный выбор. Попробуйте снова.")  # Если введен неверный выбор
