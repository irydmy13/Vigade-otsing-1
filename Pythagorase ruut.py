import tkinter as tk
import re
import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage
from PIL import Image, ImageTk
from tkinter import messagebox

#Дата рождения (добавляет точки автоматически)
def format_date(event):
    text = birth_entry.get()

#Если поле пустое, выходим из функции
    if not text:
        return
    
    #Оставляем только цифры
    numbers = "".join(filter(str.isdigit, text))
    #Ограничиваем длину до 8 символов (ДДММГГГГ)
    numbers = numbers[:8]
    #Запоминаем текущую позицию курсора
    cursor_position = birth_entry.index(tk.INSERT)

    #Формируем текст с точками
    formatted_text = ""
    for i, char in enumerate(numbers):
        if i in [2, 4]:  #Добавляем точки после 2 и 4 символов
            formatted_text += "."
        formatted_text += char

    #Обновляем текст в поле
    birth_entry.delete(0, tk.END)
    birth_entry.insert(0, formatted_text)


#Расчёт квадрата Пифагора
def calculate_pythagorean_square():
    birth_date = birth_entry.get()
    if not re.match(r"\d{2}\.\d{2}\.\d{4}", birth_date):
        messagebox.showerror("Ошибка", "Введите дату в формате ДД.ММ.ГГГГ!")
        return

    digits = [int(d) for d in birth_date if d.isdigit()]

    first_sum = sum(digits)
    digits.extend([int(d) for d in str(first_sum)])

    if first_sum >= 10:
        second_sum = sum(int(d) for d in str(first_sum))
        digits.extend([int(d) for d in str(second_sum)])

    third_number = abs(first_sum - 2 * digits[0])
    digits.extend([int(d) for d in str(third_number)])

    matrix = [["-" for _ in range(3)] for _ in range(3)]
    positions = {1: (0, 0), 2: (1, 0), 3: (2, 0),
                 4: (0, 1), 5: (1, 1), 6: (2, 1),
                 7: (0, 2), 8: (1, 2), 9: (2, 2)}

    for num in range(1, 10):
        if digits.count(num) > 0:
            row, col = positions[num]
            matrix[row][col] = str(num) * digits.count(num)

    result_text = "\n".join("{:^5} {:^5} {:^5}".format(*row) for row in matrix)
    result_label.config(text=result_text, font=("Courier", 18, "bold"), justify="center")

#Функция отправки сообщения
def send_email():
    recipient = email_entry.get()
    if not recipient:
        messagebox.showerror("Ошибка", "Введите email!")
        return

    sender_email = "kotiukir@gmail.com"
    app_password = "yzps ylch ucij sdyz"

    user_name = name_entry.get()
    user_birthdate = birth_entry.get()
    user_result = result_label.cget("text")

    #Читаем файл характеристик
    try:
        with open("characteristics.txt", "r", encoding="utf-8") as f:
            characteristics_text = f.read()
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось прочитать файл характеристик:\n{e}")
        return

    #Текст письма
    message = f"""\
Имя: {user_name}

Дата рождения: {user_birthdate}

Квадрат Пифагора:
{user_result}

Характеристика:
{characteristics_text}
-- 
С уважением, Ирина!
"""

    try:
        msg = EmailMessage()
        msg.set_content(message)
        msg["Subject"] = "Результаты Квадрата Пифагора"
        msg["From"] = sender_email
        msg["To"] = recipient

        #Отправка письма
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.send_message(msg)

        messagebox.showinfo("Успех", "Письмо отправлено!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось отправить письмо:\n{e}")

#ИНТЕРФЕЙС

root = tk.Tk()
root.title("Квадрат Пифагора")
root.geometry("800x600")

#Загрузка и установка фона
bg_image = Image.open("5.jpg").resize((800, 600))
bg = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg)
bg_label.place(relwidth=1, relheight=1)

#Установка логотипа
root.iconbitmap("6.ico")

#Стили
label_style = {"bg": "#000000", "fg": "white", "font": ("Comic Sans MS", 16, "bold")}
entry_style = {"bg": "#000000", "fg": "white", "insertbackground": "white", "bd": 3, "relief": "ridge", "font": ("Comic Sans MS", 16, "bold")}
button_style = {"bg": "#333333", "fg": "white", "font": ("Comic Sans MS", 14, "bold"), "bd": 2, "relief": "ridge"}

tk.Label(root, text="Введите имя:", **label_style).pack(pady=5)
name_entry = tk.Entry(root, **entry_style)
name_entry.pack(pady=5)

tk.Label(root, text="Дата рождения (дд.мм.гггг):", **label_style).pack(pady=5)
birth_entry = tk.Entry(root, **entry_style)
birth_entry.pack(pady=5)
birth_entry.bind("<KeyRelease>", format_date)

tk.Label(root, text="Email:", **label_style).pack(pady=5)
email_entry = tk.Entry(root, **entry_style)
email_entry.pack(pady=5)

#Метка для вывода результата
result_label = tk.Label(root, text="", **label_style)
result_label.pack(pady=10)

#Функция очистки всех полей
def clear_fields():
    name_entry.delete(0, tk.END)
    birth_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    result_label.config(text="")

#КНОПКИ

button_frame = tk.Frame(root, bg="#000000")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Рассчитать", command=calculate_pythagorean_square, **button_style).pack(side="left", padx=5)
tk.Button(button_frame, text="Отправить на email", command=send_email, **button_style).pack(side="left", padx=5)
tk.Button(button_frame, text="Очистить", command=clear_fields, **button_style).pack(side="left", padx=5)
tk.Button(button_frame, text="Выход", command=root.quit, **button_style).pack(side="left", padx=5)

root.mainloop()
