from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk

global D, x1, x2, x

def Solve():
    try:
        a = float(entryA.get())
        b = float(entryB.get())
        c = float(entryC.get())

        global D, x1, x2, x
        D = b**2 - 4 * a * c

        if D > 0:
            x1 = round((-b + (D**0.5)) / (2 * a), 2)
            x2 = round((-b - (D**0.5)) / (2 * a), 2)
            label5.configure(text=f"D > 0 --> 2 корня: \n x1 = {x1}\n x2 = {x2}")
        elif D == 0:
            x = round(-b / (2 * a), 2)
            label5.configure(text=f"D = 0 --> 1 корень: \n x = {x}")
        else:
            label5.configure(text="Решений нет")
        
    except:
        messagebox.showerror("Ошибка", "Введите корректные числа!")

def DrawGraph():
    try:
        a = float(entryA.get())
        b = float(entryB.get())
        c = float(entryC.get())

        x = np.linspace(-20, 20, 100)
        y = a * x**2 + b * x + c

        plt.figure()
        plt.plot(x, y, label=f"{a}x² + {b}x + {c}")
        plt.axhline(0, color="black", linewidth=0.5)
        plt.axvline(0, color="black", linewidth=0.5)
        plt.grid()
        plt.legend()
        plt.title("График квадратного уравнения")
        plt.show()
    except:
        messagebox.showerror("Ошибка", "Введите корректные числа!")

def check_input(event=None):
    """ Проверяет, пустые ли поля, и меняет их цвет. """
    if entryA.get().strip() == "":
        entryA.config(bg="red")
    else:
        entryA.config(bg="#ffe6f0")

    if entryB.get().strip() == "":
        entryB.config(bg="red")
    else:
        entryB.config(bg="#ffe6f0")

    if entryC.get().strip() == "":
        entryC.config(bg="red")
    else:
        entryC.config(bg="#ffe6f0")

root = Tk()
root.geometry("900x400")
root.resizable(False, False)
root.title("Решение квадратного уравнения")

original_image = Image.open(r"3.jpg")
resized_image = original_image.resize((900, 400))
bgimage = ImageTk.PhotoImage(resized_image)

labelBG = Label(root, image=bgimage)
labelBG.place(x=0, y=0)

label1 = Label(root, text="Решение квадратного уравнения", font=("Arial", 20), bg="#ffccff")
label1.pack(pady="20")

# Создаём контейнер для формулы
formula_frame = Frame(root, bg="white")
formula_frame.place(x=120, y=180)

entryA = Entry(formula_frame, font=("Arial", 30), bg="#ffe6f0", width=3, justify=CENTER)
entryA.grid(row=0, column=0)
entryA.bind("<KeyRelease>", check_input)

label2 = Label(formula_frame, font=("Arial", 30), text="x² +", bg="white")
label2.grid(row=0, column=1)

entryB = Entry(formula_frame, font=("Arial", 30), bg="#ffe6f0", width=3, justify=CENTER)
entryB.grid(row=0, column=2)
entryB.bind("<KeyRelease>", check_input)

label3 = Label(formula_frame, font=("Arial", 30), text="x +", bg="white")
label3.grid(row=0, column=3)

entryC = Entry(formula_frame, font=("Arial", 30), bg="#ffe6f0", width=3, justify=CENTER)
entryC.grid(row=0, column=4)
entryC.bind("<KeyRelease>", check_input)

label4 = Label(formula_frame, font=("Arial", 30), text="= 0", bg="white")
label4.grid(row=0, column=5)

button1 = Button(root, text="Решить", font=("beer money", 20), command=Solve, bg="lightgreen")
button1.place(x=650, y=140)

button2 = Button(root, text="График", font=("Arial", 20), command=DrawGraph, bg="lightblue")
button2.place(x=650, y=220)

label5 = Label(root, text="Ответ...", bg="#ddccff", font=("Arial", 14), compound="center")
label5.place(x=120, y=290, width=600, height=90)
########################################################################
lbl=Label(f1, text="", font="", fg="", bg="")
lbl.grid(row=0, column=0, columnspan=7)

lbl_vastus=Label(f1, text="", height=4, width=60, bg="")
lbl_vastus.grid(row=2, column=0, columnspan=7)

lbl_a=Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=3)
lgl_a.grid(row=1, column=0)
x2=Label(f1, text="")
x2.grid(row=1, column=2)


root.mainloop()
