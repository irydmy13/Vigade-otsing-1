import random

#задание 1
j = 0
for i in range(15):
    number=input(f"Введите число {i + 1}: ")
    try:
        i=int(number)
        j+= 1
    except:
        print("Ошибка")
print(f"Количество целых чисел среди введенных: {j}")


#задание 2
while True:
    try:
        A=int(input("Sisesta A:"))
        break
    except:
        print("On valja naturaalne arv")
summa=0
if A>0:
    for i in range(1,A+1,1):
        summa+=i #summa=summa+i
        print(f"{i}. samm summa={summa}")
    print(f"Vastus {summa}")


#задание 3
p=1
for j in range(8):
    while True:
        try:
            arv=float(input(f"Sisesta {j+1} arv:"))
            break
        except:
            print("On valja arv")
    if arv>0: 
        p*=arv
    else:
        print("Число должно быть больше 0")
    print(f"{j+1}. samm korrutis= {p}")
print(f"Lopptulemus on {p}")


#задание 4
for i in range(10,21,1):
    print(i**2, end=";")
print()


#задача 5
N = int(input("Введите количество чисел: "))
negative = 0
for i in range(N):
    number = float(input(f"Введите число {i + 1}: "))
    if number < 0:
        negative+=number
print(f"Сумма отрицательных чисел: {negative}")

#задача 7
print(f"Выводим на экран числа, кратные К из промежутка [А,В]")
A = int(input("Введите начало промежутка А: "))
B = int(input("Введите конец промежутка В: "))
K = int(input("Введите число К: "))
print(f"Числа, кратные {K}, из промежутка [{A}, {B}]:")
for number in range(A, B + 1):
    if number % K == 0:
        print(number, end="; ")


#задача 15
for read in range(10):
    for rida in range(10):
        print(rida, end=" ")
    print()
print()


#задача 16
for j in range(1,10):
    for i in range(1,10):
        if i==j:
            print(j, end=" ")
        else:
             print("0", end=" ")
        print("0", end=" ")
    print()


#задача 17
j=2
for i in range(1, 10):
    a=j*i
    print(f"{j}*{i}={a}")


# #задача 28
a = random.randint(1, 100)
print("Компьютер задумал число от 1 до 100. Попробуйте отгадать!")
attempts = 0

while True:
    user_guess = int(input("Ваше предположение: "))
    attempts += 1
    if user_guess < a:
        print("Загаданное число больше.")
    elif user_guess > a:
        print("Загаданное число меньше.")
    else:
        print(f"Поздравляем! Вы угадали число {a} с {attempts} попытки.")
        break
