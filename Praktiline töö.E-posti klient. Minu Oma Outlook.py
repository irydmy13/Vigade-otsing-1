import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import smtplib
import ssl
from email.message import EmailMessage
import imghdr
import json
import os

# Константы
SAVE_FILE = "draft.json"
LOG_FILE = "sent_emails.log"
ATTACHMENTS = []

# Функция выбора файлов
def vali_pilt():
    file_paths = filedialog.askopenfilenames(filetypes=[("Images & Files", "*.*")])
    if file_paths:
        global ATTACHMENTS
        ATTACHMENTS.extend(file_paths)
        update_attachments_label()

# Обновление метки вложений
def update_attachments_label():
    l_lisatud.config(text="\n".join(ATTACHMENTS) if ATTACHMENTS else "Нет вложений")

# Очистка формы
def clear_form():
    email_box.delete(0, tk.END)
    teema_box.delete(0, tk.END)
    kiri_box.delete("1.0", tk.END)
    ATTACHMENTS.clear()
    update_attachments_label()

# Предварительный просмотр письма
def preview_email():
    preview_text = f"""
    📧 Кому: {email_box.get()}
    📌 Тема: {teema_box.get()}
    📄 Сообщение:
    {kiri_box.get("1.0", tk.END)}
    📎 Вложения: {", ".join(ATTACHMENTS) if ATTACHMENTS else "Нет"}
    """
    messagebox.showinfo("Предварительный просмотр", preview_text)

# Автосохранение черновика
def save_draft():
    draft = {
        "email": email_box.get(),
        "subject": teema_box.get(),
        "body": kiri_box.get("1.0", tk.END),
        "attachments": ATTACHMENTS
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(draft, f)

# Загрузка черновика
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

# Отправка письма
def saada_kiri():
    kellele = email_box.get().split(",")  # Поддержка нескольких получателей
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

    # Добавление вложений
    for file_path in ATTACHMENTS:
        with open(file_path, "rb") as f:
            file_data = f.read()
            file_type = imghdr.what(None, file_data) or "octet-stream"
        msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=os.path.basename(file_path))

    # Отправка письма
    try:
        progress_bar.start()
        context = ssl.create_default_context()
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        messagebox.showinfo("Успех", "Письмо отправлено!")

        # Сохранение лога
        with open(LOG_FILE, "a") as log:
            log.write(f"To: {msg['To']}\nSubject: {msg['Subject']}\n\n{kiri}\n{'-'*50}\n")

    except Exception as e:
        messagebox.showerror("Ошибка", str(e))
    finally:
        server.quit()
        progress_bar.stop()

# Переключение темы
def toggle_theme():
    new_theme = "clam" if theme_var.get() else "alt"
    style.theme_use(new_theme)

# Создание окна
root = tk.Tk()
root.title("E-kirja saatmine")
root.geometry("550x500")

# Стилизация
style = ttk.Style()
style.theme_use("clam")

theme_var = tk.BooleanVar()
ttk.Checkbutton(root, text="Темный режим", variable=theme_var, command=toggle_theme).grid(row=0, column=2, padx=10)

# Метки и поля
ttk.Label(root, text="EMAIL:").grid(row=1, column=0, sticky="w", padx=10)
email_box = ttk.Entry(root, width=50)
email_box.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="TEEMA:").grid(row=2, column=0, sticky="w", padx=10)
teema_box = ttk.Entry(root, width=50)
teema_box.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(root, text="LISA:").grid(row=3, column=0, sticky="w", padx=10)
l_lisatud = ttk.Label(root, text="Нет вложений", width=50, relief="sunken", anchor="w")
l_lisatud.grid(row=3, column=1, padx=10, pady=5)

ttk.Label(root, text="KIRI:").grid(row=4, column=0, sticky="nw", padx=10)
kiri_box = tk.Text(root, width=50, height=5)
kiri_box.grid(row=4, column=1, padx=10, pady=5)

# Кнопки
ttk.Button(root, text="LISA PILT", command=vali_pilt).grid(row=5, column=0, padx=10, pady=5)
ttk.Button(root, text="ПРЕДВАРИТЕЛЬНЫЙ ПРОСМОТР", command=preview_email).grid(row=5, column=1, padx=10, pady=5)

ttk.Button(root, text="СОХРАНИТЬ ЧЕРНОВИК", command=save_draft).grid(row=6, column=0, padx=10, pady=5)
ttk.Button(root, text="ЗАГРУЗИТЬ ЧЕРНОВИК", command=load_draft).grid(row=6, column=1, padx=10, pady=5)

ttk.Button(root, text="ОЧИСТИТЬ", command=clear_form).grid(row=7, column=0, padx=10, pady=5)
ttk.Button(root, text="SAADA", command=saada_kiri).grid(row=7, column=1, padx=10, pady=5)

# Прогресс-бар
progress_bar = ttk.Progressbar(root, mode="indeterminate")
progress_bar.grid(row=8, column=1, sticky="ew", padx=10, pady=5)

root.mainloop()
