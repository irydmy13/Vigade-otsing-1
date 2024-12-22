

#ЗАДАНИЕ В ПРОЦЕССЕ РАБОТЫ
import random

print("Добро пожаловать в проверку знаний по математике!")
print("Выберите уровень сложности: 1(лёгкий), 2(средний), 3(сложный)")

while True:
    try:
        level = int(input("Введите уровень сложности 1, 2 или 3:"))
        if level in [1, 2, 3]:
            break
        else:
            print("Пожалуйста, выберите 1, 2 или 3.")
    except ValueError:
        print("Введите число 1, 2 или 3.")

while True:
    try:
        num_ques = int(input("Сколько примеров вы хотите решить?"))
        if num_ques > 0:
            break
        else:
            print("Введите положительное число.")
    except ValueError:
        print("Введите целое число.")

        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operations = ['+', '-']
    elif level == 2:
        num1 = random.randint(1, 50)    
        num2 = random.randint(1, 50)
        operations = ['+', '-', '*']
    else:  # level 3
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operations = ['+', '-', '*', '/']

    operation = random.choice(operations)

    if operation == '/':
        num1 = num1 * num2 #Избегаем деления на 0 и делаем целочисленные примеры
        question = f"{num1} / {num2}"
        correct_answer = num1 // num2
    else:
        question = f"{num1} {operation} {num2}"
        correct_answer = eval(question)

    return question, correct_answer

def main():
    print("Добро пожаловать в тест по математике!")
    print("Выберите уровень сложности: 1 (легкий), 2 (средний), 3 (сложный)")

    while True:
        try:
            level = int(input("Введите уровень сложности (1, 2 или 3): "))
            if level in [1, 2, 3]:
                break
            else:
                print("Пожалуйста, выберите 1, 2 или 3.")
        except ValueError:
            print("Введите число 1, 2 или 3.")

    while True:
        try:
            num_questions = int(input("Сколько примеров вы хотите решить? "))
            if num_questions > 0:
                break
            else:
                print("Введите положительное число.")
        except ValueError:
            print("Введите целое число.")

    score = 0

    for i in range(num_questions):
        question, correct_answer = generate_question(level)
        print(f"Пример {i + 1}: {question} = ?")

        while True:
            try:
                user_answer = int(input("Ваш ответ: "))
                break
            except ValueError:
                print("Введите число.")

        if user_answer == correct_answer:
            print("Правильно!")
            score += 1
        else:
            print(f"Неправильно. Правильный ответ: {correct_answer}")

    percentage = (score / num_questions) * 100
    print(f"Вы решили {score} из {num_questions} примеров правильно ({percentage:.2f}%).")

    if percentage < 60:
        grade = 2
    elif 60 <= percentage < 75:
        grade = 3
    elif 75 <= percentage < 90:
        grade = 4
    else:
        grade = 5

    print(f"Ваша оценка: Hinne {grade}")

if __name__ == "__main__":
    main()
