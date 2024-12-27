#ules 1
N = int(input("Введите количество чисел для ввода: "))

if N > 0:
    M = max(int(input(f"Введите число {i + 1}: ")) for i in range(N)) #M-максимальное
    print(f"Максимальное число: {M}")
else:
    print("Количество чисел должно быть больше 0.")

#ules 2
while True:
    A = int(input("Введите целое число: "))
    if A == 13:
        print(77)
    else:
        print(A)

#ules 3
start = 10 #км
days = 7

summ = 0
current_distance = start

for _ in range(days):
    summ += current_distance
    current_distance += current_distance * (10 / 100)

print(f"Суммарный путь за {days} дней: {summ:.2f} км")

#ules 4
M = float(input(f"Введите длину ткани: метров "))

while M > 0:
    a = float(input(f"Введите длину требуемого куска ткани: метров "))
    
    if a > M:
        print(f"Недостаточно ткани! Осталось только {M:.2f} метров.")
        s = input("Хотите выкупить остаток ткани? (да/нет): ").strip().lower()
        if s == "да":
            print(f"Вы выкупили остаток ткани длиной {M:.2f} метров.")
            M = 0
        else:
            print("Переход к следующему покупателю.")
    else:
        M -= a
        print(f"Кусок длиной {a:.2f} метров отрезан. Осталось {M:.2f} метров.")

print("Ткань закончилась.")

#ules 5  
print("Найти площадь трапеции!") #S=(a+b)h/2  a и b — длины оснований трапеции, h — высота трапеции.

while True:
    a=float(input("Введите длину трапеции а = "))
    b=float(input("Введите длину трапеции b = "))
    h=float(input("Введите высоту трапеции h = "))

    if a<=0 or b<=0 or h<=0:
        print("Все числа должны быть положительными!")
    else:
        S=(a+b)*h/2
        print(f"Площадь трапеции S = {S: .2f}")
#R выбор продолжения
    R = input("Хотите вычислить площадь еще одной трапеции? (да/нет): ").strip().lower()
    if R == "нет":
         print("До свидания!")
         break

#ules 6

q=int(input("Введите любое целое число: "))
if q % 3 == 0:
    print(f"Число {q} делится без остатка на 3.")
else:
    print(f"Число {q} не делится без остатка на 3.")
