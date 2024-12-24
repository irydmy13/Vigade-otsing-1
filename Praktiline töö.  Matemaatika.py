import random

print("Добро пожаловать в проверку знаний по математике!")

while True:
    try:
        level = int(input("Введите уровень сложности 1, 2 или 3: "))
        if level in [1, 2, 3]:
            break
        else:
            print("Пожалуйста, выберите 1, 2 или 3.")
    except ValueError:
        print("Введите число 1, 2 или 3.")

while True:
    try:
        num_ques = int(input("Сколько примеров вы хотите решить? "))
        if num_ques > 0:
            break
        else:
            print("Введите положительное число.")
    except ValueError:
        print("Введите целое число.")

correct_count = 0
incorrect_count = 0 #Инициализация счетчиков

for _ in range(num_ques):
    if level == 1:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operations = ['+', '-']
    elif level == 2:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        operations = ['+', '-', '*']
    else:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operations = ['+', '-', '*', '/']

    operation = random.choice(operations) #Выбор случайной операции

    if operation == '/':
        num1 = num1 * num2
        question = f"{num1} / {num2}"
        correct_answer = num1 // num2
    elif operation == '+':
        question = f"{num1} + {num2}"
        correct_answer = num1 + num2
    elif operation == '-':
        question = f"{num1} - {num2}"
        correct_answer = num1 - num2
    elif operation == '*':
        question = f"{num1} * {num2}"
        correct_answer = num1 * num2

    while True:
        try:
            user_answer = int(input(f"Решите: {question} = "))
            if user_answer == correct_answer:
                print("Правильно!")
                correct_count += 1  #Увеличиваем счетчик правильных ответов
            else:
                print(f"Неправильно. Правильный ответ: {correct_answer}.")
                incorrect_count += 1  #Увеличиваем счетчик неправильных ответов
            break
        except ValueError:
            print("Введите числовой ответ.")

print("\nРезультаты тестирования:")
print(f"Правильных ответов: {correct_count}")
print(f"Неправильных ответов: {incorrect_count}")
print(f"Ваш результат: {correct_count}/{num_ques}")

score_percentage = (correct_count / num_ques) * 100 #Подсчет процента правильных ответов
if score_percentage < 60:
    grade = 2
elif 60 <= score_percentage < 75:
    grade = 3
elif 75 <= score_percentage < 90:
    grade = 4
else:
    grade = 5

print(f"Процент правильных ответов: {score_percentage:.2f}%")
print(f"Ваша оценка: {grade}")
