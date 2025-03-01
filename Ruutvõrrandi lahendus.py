import tkinter as tk
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import os

#Создание окна
aken = tk.Tk()
aken.title("Решение квадратного уравнения")
aken.geometry("400x200")

#Фон
if os.path.exists("2.jpg"):
    bg_image = Image.open("2.jpg").resize((400, 200))
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    bg_label = tk.Label(aken, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)  #Фон занимает весь экран

#Поля ввода вместо коэффициентов
sisestus_a = tk.Entry(aken, font=("Arial", 14), width=5)
sisestus_a.place(x=20, y=30)

silt_x2 = tk.Label(aken, text=" * x² + ", font=("Arial", 14), bg="#dfefff")
silt_x2.place(x=75, y=30)

sisestus_b = tk.Entry(aken, font=("Arial", 14), width=5)
sisestus_b.place(x=130, y=30)

silt_x = tk.Label(aken, text=" * x + ", font=("Arial", 14), bg="#dfefff")
silt_x.place(x=185, y=30)

sisestus_c = tk.Entry(aken, font=("Arial", 14), width=5)
sisestus_c.place(x=240, y=30)

silt_eq = tk.Label(aken, text=" = 0", font=("Arial", 14), bg="#dfefff")
silt_eq.place(x=295, y=30)

#Функция для решения уравнения
def lahenda():
    if not sisestus_a.get() or not sisestus_b.get() or not sisestus_c.get():
        sisestus_a.config(bg="lightcoral" if not sisestus_a.get() else "white")
        sisestus_b.config(bg="lightcoral" if not sisestus_b.get() else "white")
        sisestus_c.config(bg="lightcoral" if not sisestus_c.get() else "white")
        vastus_silt.config(text="Все поля должны быть заполнены!", bg="yellow")
        return
    
    try:
        a = float(sisestus_a.get())
        b = float(sisestus_b.get())
        c = float(sisestus_c.get())
    except ValueError:
        vastus_silt.config(text="Введите корректные числа!", bg="yellow")
        return
    
    if a == 0:
        vastus_silt.config(text="Коэффициент a не может быть равен нулю!", bg="yellow")
        return
    
    d = b**2 - 4*a*c
    
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        vastus_silt.config(text=f"D = {d}\nX1 = {x1:.2f}\nX2 = {x2:.2f}", bg="lightgreen")
    elif d == 0:
        x = -b / (2 * a)
        vastus_silt.config(text=f"D = {d}\nX = {x:.2f}", bg="lightgreen")
    else:
        vastus_silt.config(text="Нет действительных корней", bg="lightcoral")

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
nupp_lahenda.place(x=110, y=70)

nupp_graafik = tk.Button(aken, text="График", command=joonista_graafik, font=("Arial", 14), bg="lightblue")
nupp_graafik.place(x=200, y=70)

#Вывод решения
vastus_silt = tk.Label(aken, text="Решение", font=("Arial", 14), bg="lavender", width=40)
vastus_silt.place(x=20, y=120)

aken.mainloop()
