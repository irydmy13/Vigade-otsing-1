import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import smtplib
import ssl
from email.message import EmailMessage
import imghdr
import json
import os

#Константы
SAVE_FILE = "draft.json"
LOG_FILE = "sent_emails.log"
ATTACHMENTS = []
BACKGROUND_IMAGE = "4.jpg"

#Создание окна
root = tk.Tk()
root.title("E-kirja saatmine")
root.geometry("550x500")

#Установка фона
if os.path.exists(BACKGROUND_IMAGE):
    bg_image = Image.open(BACKGROUND_IMAGE).resize((550, 500))
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)

#Функция выбора файлов
def vali_pilt():
    file_paths = filedialog.askopenfilenames(filetypes=[("Images & Files", "*.*")])
    if file_paths:
        global ATTACHMENTS
        ATTACHMENTS.extend(file_paths)
        update_attachments_label()

#Обновление метки вложений
def update_attachments_label():
    l_lisatud.config(text="\n".join(ATTACHMENTS) if ATTACHMENTS else "Нет вложений")

#Очистка формы
def clear_form():
    email_box.delete(0, tk.END)
    teema_box.delete(0, tk.END)
    kiri_box.delete("1.0", tk.END)
    ATTACHMENTS.clear()
    update_attachments_label()

#Предварительный просмотр письма
def preview_email():
    preview_text = f"""
    📧 Кому: {email_box.get()}
    📌 Тема: {teema_box.get()}
    📄 Сообщение:
    {kiri_box.get("1.0", tk.END)}
    📎 Вложения: {", ".join(ATTACHMENTS) if ATTACHMENTS else "Нет"}
    """
    messagebox.showinfo("Предварительный просмотр", preview_text)

#Автосохранение черновика
def save_draft():
    draft = {
        "email": email_box.get(),
        "subject": teema_box.get(),
        "body": kiri_box.get("1.0", tk.END),
        "attachments": ATTACHMENTS
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(draft, f)

#Загрузка черновика
def load_draft():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            draft = json.load(f)
            email_box.insert(0, draft["email"])
            teema_box.insert(0, draft["subject"])
            kiri_box.insert("1.0", draft["body"])
            global ATTACHMENTS
            ATTACHMENTS = draft["attachments"]
            update_attachments_label()

#Отправка письма
def saada_kiri():
    kellele = email_box.get().split(",")
    teema = teema_box.get()
    kiri = kiri_box.get("1.0", tk.END) + "\n\n--\nПодпись пользователя"

    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "kotiukir@gmail.com"
    password = "yzps ylch ucij sdyz"

    msg = EmailMessage()
    msg.set_content(kiri)
    msg["Subject"] = teema
    msg["From"] = sender_email
    msg["To"] = ", ".join(kellele)

    #Добавление вложений
    for file_path in ATTACHMENTS:
        with open(file_path, "rb") as f:
            file_data = f.read()
            file_type = imghdr.what(None, file_data) or "octet-stream"
        msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=os.path.basename(file_path))

    #Отправка письма
    try:
        progress_bar.start()
        context = ssl.create_default_context()
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        messagebox.showinfo("Успех", "Письмо отправлено!")

        #Сохранение лога
        with open(LOG_FILE, "a") as log:
            log.write(f"To: {msg['To']}\nSubject: {msg['Subject']}\n\n{kiri}\n{'-'*50}\n")

    except Exception as e:
        messagebox.showerror("Ошибка", str(e))
    finally:
        server.quit()
        progress_bar.stop()

#Стилизация
style = ttk.Style()
style.theme_use("clam")
style.configure("Pink.TButton", background="#FFC0CB", foreground="black", font=("Arial", 10, "bold"))
style.map("Pink.TButton", background=[("active", "#FF69B4")])  #Цвет при наведении

#Поля и кнопки
ttk.Label(root, text="EMAIL:", background="pink").place(x=20, y=30)
email_box = ttk.Entry(root, width=50)
email_box.place(x=100, y=30)

ttk.Label(root, text="ТЕМА:", background="pink").place(x=20, y=70)
teema_box = ttk.Entry(root, width=50)
teema_box.place(x=100, y=70)

ttk.Label(root, text="ВЛОЖЕНИЯ:", background="pink").place(x=20, y=110)
l_lisatud = ttk.Label(root, text="Нет вложений", width=50, relief="sunken", anchor="w")
l_lisatud.place(x=100, y=110)

ttk.Label(root, text="ПИСЬМО:", background="pink").place(x=20, y=150)
kiri_box = tk.Text(root, width=50, height=5)
kiri_box.place(x=100, y=150)

# Кнопки
ttk.Button(root, text="ДОБАВИТЬ ИЗОБРАЖЕНИЕ", command=vali_pilt, style="Pink.TButton").place(x=50, y=270)
ttk.Button(root, text="ПРЕДВАРИТЕЛЬНЫЙ ПРОСМОТР", command=preview_email, style="Pink.TButton").place(x=250, y=270)

ttk.Button(root, text="СОХРАНИТЬ ЧЕРНОВИК", command=save_draft, style="Pink.TButton").place(x=50, y=310)
ttk.Button(root, text="ЗАГРУЗИТЬ ЧЕРНОВИК", command=load_draft, style="Pink.TButton").place(x=250, y=310)

ttk.Button(root, text="ОЧИСТИТЬ", command=clear_form, style="Pink.TButton").place(x=50, y=350)
ttk.Button(root, text="ОТПРАВИТЬ", command=saada_kiri, style="Pink.TButton").place(x=250, y=350)

# Прогресс-бар
progress_bar = ttk.Progressbar(root, mode="indeterminate")
progress_bar.place(x=100, y=400, width=350)

root.mainloop()
