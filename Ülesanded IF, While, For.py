# #ules 1
# N = int(input("Введите количество чисел для ввода: "))

# if N > 0:
#     M = max(int(input(f"Введите число {i + 1}: ")) for i in range(N)) #M-максимальное
#     print(f"Максимальное число: {M}")
# else:
#     print("Количество чисел должно быть больше 0.")

# #ules 2
# while True:
#     A = int(input("Введите целое число: "))
#     if A == 13:
#         print(77)
#     else:
#         print(A)

# #ules 3
# start = 10 #км
# days = 7

# summ = 0
# current_distance = start

# for _ in range(days):
#     summ += current_distance
#     current_distance += current_distance * (10 / 100)

# print(f"Суммарный путь за {days} дней: {summ:.2f} км")

# #ules 4
# M = float(input(f"Введите длину ткани: метров "))

# while M > 0:
#     a = float(input(f"Введите длину требуемого куска ткани: метров "))
    
#     if a > M:
#         print(f"Недостаточно ткани! Осталось только {M:.2f} метров.")
#         s = input("Хотите выкупить остаток ткани? (да/нет): ").strip().lower()
#         if s == "да":
#             print(f"Вы выкупили остаток ткани длиной {M:.2f} метров.")
#             M = 0
#         else:
#             print("Переход к следующему покупателю.")
#     else:
#         M -= a
#         print(f"Кусок длиной {a:.2f} метров отрезан. Осталось {M:.2f} метров.")

# print("Ткань закончилась.")