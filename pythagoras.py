import tkinter as tk
from tkinter import messagebox

def calculate_pythagoras():
    name = name_entry.get()
    birth_date = birth_entry.get()
    email = email_entry.get()
    
    if not name or not birth_date or not email:
        messagebox.showerror("Ошибка", "Заполните все поля!")
        return
    
    messagebox.showinfo("Успех", f"Данные получены!\nИмя: {name}\nДата рождения: {birth_date}\nEmail: {email}")

# Создание окна
root = tk.Tk()
root.title("Квадрат Пифагора")
root.geometry("400x300")

# Поля ввода
tk.Label(root, text="Введите имя:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Дата рождения (дд.мм.гггг):").pack()
birth_entry = tk.Entry(root)
birth_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

# Кнопка расчета
calc_button = tk.Button(root, text="Рассчитать", command=calculate_pythagoras)
calc_button.pack()

root.mainloop()

