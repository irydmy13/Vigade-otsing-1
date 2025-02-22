import tkinter as tk
import math
import numpy as np
import matplotlib.pyplot as plt

#Создание окна
aken = tk.Tk()
aken.title("Решение квадратного уравнения")
aken.geometry("400x200")

#Поля ввода вместо коэффициентов
sisestus_a = tk.Entry(aken, font=("Arial", 14), width=5)
sisestus_a.grid(row=0, column=0)

silt_x2 = tk.Label(aken, text=" * x² + ", font=("Arial", 14))
silt_x2.grid(row=0, column=1)

sisestus_b = tk.Entry(aken, font=("Arial", 14), width=5)
sisestus_b.grid(row=0, column=2)

silt_x = tk.Label(aken, text=" * x + ", font=("Arial", 14))
silt_x.grid(row=0, column=3)

sisestus_c = tk.Entry(aken, font=("Arial", 14), width=5)
sisestus_c.grid(row=0, column=4)

silt_eq = tk.Label(aken, text=" = 0", font=("Arial", 14))
silt_eq.grid(row=0, column=5)

#Функция для решения уравнения
def lahenda():
    if not sisestus_a.get() or not sisestus_b.get() or not sisestus_c.get():
        sisestus_a.config(bg="lightred" if not sisestus_a.get() else "lavender")
        sisestus_b.config(bg="lightred" if not sisestus_b.get() else "lavender")
        sisestus_c.config(bg="lightred" if not sisestus_c.get() else "lavender")
        vastus_silt.config(text="Все поля должны быть заполнены!")
        return
    
    try:
        a = float(sisestus_a.get())
        b = float(sisestus_b.get())
        c = float(sisestus_c.get())
    except ValueError:
        vastus_silt.config(text="Введите корректные числа!")
        return
    
    if a == 0:
        vastus_silt.config(text="Коэффициент a не может быть равен нулю!")
        return
    
    d = b**2 - 4*a*c
    
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        vastus_silt.config(text=f"D = {d}\nX1 = {x1:.2f}\nX2 = {x2:.2f}")
    elif d == 0:
        x = -b / (2 * a)
        vastus_silt.config(text=f"D = {d}\nX = {x:.2f}")
    else:
        vastus_silt.config(text="Нет действительных корней")

#Функция для построения графика
def joonista_graafik():
    if not sisestus_a.get() or not sisestus_b.get() or not sisestus_c.get():
        return
    
    try:
        a = float(sisestus_a.get())
        b = float(sisestus_b.get())
        c = float(sisestus_c.get())
    except ValueError:
        return
    
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    
    plt.figure()
    plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.title("График квадратного уравнения")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

#Кнопки
nupp_lahenda = tk.Button(aken, text="Решить", command=lahenda, font=("Arial", 14), bg="lightgreen")
nupp_lahenda.grid(row=1, column=2)

nupp_graafik = tk.Button(aken, text="График", command=joonista_graafik, font=("Arial", 14), bg="lightblue")
nupp_graafik.grid(row=1, column=3)

#Вывод решения
vastus_silt = tk.Label(aken, text="Решение", font=("Arial", 14), bg="lavender")
vastus_silt.grid(row=2, column=0, columnspan=6, sticky="nsew")

aken.mainloop()