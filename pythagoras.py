import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Создаю графический интерфейс 

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
root.geometry("500x400")

# Загружаем фон
bg_image = Image.open("5.jpg")
bg_image = bg_image.resize((500, 400))  # Подгоняем размер под окно
bg = ImageTk.PhotoImage(bg_image)

# Создаем метку с фоном
bg_label = tk.Label(root, image=bg)
bg_label.place(relwidth=1, relheight=1)

# Создаю логотип
root.iconbitmap("6.ico")

# Стили
label_style = {"bg": "#000000", "fg": "white", "font": ("Arial", 12, "bold")}  # Прозрачный фон, белый текст
entry_style = {"bg": "#000000", "fg": "white", "insertbackground": "white", "bd": 2, "relief": "ridge"}  # Черный фон, белый текст
button_style = {"bg": "#333333", "fg": "white", "font": ("Arial", 12, "bold"), "bd": 2, "relief": "ridge"}  # Темная кнопка

# Поля ввода
tk.Label(root, text="Введите имя:", **label_style).pack(pady=5)
name_entry = tk.Entry(root, **entry_style)
name_entry.pack(pady=5)

tk.Label(root, text="Дата рождения (дд.мм.гггг):", **label_style).pack(pady=5)
birth_entry = tk.Entry(root, **entry_style)
birth_entry.pack(pady=5)

tk.Label(root, text="Email:", **label_style).pack(pady=5)
email_entry = tk.Entry(root, **entry_style)
email_entry.pack(pady=5)

# Кнопка расчета
calc_button = tk.Button(root, text="Рассчитать", command=calculate_pythagoras, **button_style)
calc_button.pack(pady=10)

root.mainloop()