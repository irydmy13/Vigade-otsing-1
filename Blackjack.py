# Объединённый модуль: сначала оплата, затем игра Blackjack

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import tkinter as tk
import requests
import json
import base64
import webbrowser
from tkinter import messagebox
from datetime import datetime
import random
import string
import smtplib
from email.mime.text import MIMEText
import re
import os
from PIL import Image, ImageTk
import itertools
from datetime import datetime

# --- EveryPay данные ---
API_URL = "https://igw-demo.every-pay.com/api/v4/payments/oneoff"
API_AUTH = "ZTM2ZWI0MGY1ZWM4N2ZhMjo3YjkxYTNiOWUxYjc0NTI0YzJlOWZjMjgyZjhhYzhjZA=="
API_USERNAME = "e36eb40f5ec87fa2"
ACCOUNT_NAME = "EUR3D1"
CUSTOMER_URL = "https://maksmine.web.app/makse"

payment_reference = ""
user_email = ""
user_balance = 0.0

# --- Определяем карточные масти и значения ---
SUITS = ["♥", "♦", "♣", "♠"]
CARD_VALUES = {2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "A"}

# --- Функция для генерации nonce ---
def generate_nonce(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# --- Функция отправки email с подтверждением оплаты ---
def saada_email(to_email, payment_reference):
    global amount
    amount = amount_entry.get().strip()
    sender = "glebdranitsyn@gmail.com"
    password = "oeid ycrk uwit tnpk"
    msg = MIMEMultipart("Loome kirja koos pildiga")
    msg["Subject"] = "Подтверждение оплаты"
    msg["From"] = f"2XBET<{sender}>"
    msg["To"] = to_email
    html = f"""
    <html>
    <body>
    <h1>Приветствуем!</h1>
    <h2>Ваша оплата на сумму: {amount} EUR, успешно прошла.</h2>
    <p>Спасибо! Желаем удачной игры! <br><br>С Уважением, Ваш 2XBET!</p>
    <img src="cid:casino">
    </body>
    </html>
    """
    msg.attach(MIMEText(html, "html"))
    with open("2XBET.png", "rb") as f:
        image = MIMEImage(f.read())
        image.add_header("Content-ID", "<casino>")
        msg.attach(image)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print("Ошибка отправки электронной почты:", e)

# --- Функция логирования платежей ---
def logi_makse(payment_reference, status):
    with open("maksete_logi.txt", "a", encoding="utf-8") as file:
        file.write(f"{datetime.now()} - {payment_reference} - {status}\n")

# --- Функция валидации email ---
def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

# --- Функция запуска окна игры после успешной оплаты ---
def start_blackjack(balance):
    root = tk.Tk()
    root.iconbitmap("game.ico")  # Логотип окна игры (файл game.ico должен быть рядом с кодом)
    game = BlackjackGame(root, balance)
    root.mainloop()

# --- Функция проверки платежа и запуска игры ---
def kontrolli_makset():
    global payment_reference, user_email
    if not payment_reference:
        messagebox.showerror("Ошибка", "Сначала нужно создать платёж.")
        return
    status_url = f"https://igw-demo.every-pay.com/api/v4/payments/{payment_reference}?api_username={API_USERNAME}"
    headers = {"Authorization": f"Basic {API_AUTH}"}
    response = requests.get(status_url, headers=headers)
    if response.status_code == 200:
        makse_info = response.json()
        seisund = makse_info.get("payment_state")
        amount = float(makse_info.get("initial_amount", 0))
        logi_makse(payment_reference, seisund)
        if seisund == "settled":
            saada_email("glebdranitsyn@gmail.com", payment_reference)
            saada_email(user_email, payment_reference)
            messagebox.showinfo("Платеж подтвержден!", "Платеж прошел успешно. Давайте откроем игру!")
            app.destroy()  # Закрываем окно оплаты
            start_blackjack(amount)  # Запускаем окно игры
        else:
            messagebox.showinfo("Статус платежа", f"Статус: {seisund}")
    else:
        messagebox.showerror("Ошибка", f"Не удалось проверить платёж: {response.text}")

# --- Функция создания платежа ---
def create_payment():
    global payment_reference, user_email
    amount = amount_entry.get().strip()
    user_email = email_entry.get().strip()
    if not amount or not amount.replace(".", "", 1).isdigit():
        messagebox.showerror("Ошибка", "Введите корректную сумму")
        return
    if not validate_email(user_email):
        messagebox.showerror("Ошибка", "Введите корректный e-mail")
        return
    data = {
        "api_username": API_USERNAME,
        "account_name": ACCOUNT_NAME,
        "amount": amount,
        "order_reference": str(random.randint(100000, 999999)),
        "nonce": generate_nonce(),
        "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "customer_url": CUSTOMER_URL
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {API_AUTH}"
    }
    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    if response.status_code == 201:
        payment_info = response.json()
        payment_reference = payment_info["payment_reference"]
        payment_link = payment_info["payment_link"]
        messagebox.showinfo("Оплата", f"Перенаправляем вас на оплату.\nСсылка: {payment_link}")
        webbrowser.open(payment_link)
    else:
        messagebox.showerror("Ошибка", f"Не удалось создать платёж: {response.status_code}\n{response.text}")

# --- Интерфейс окна оплаты ---
app = tk.Tk()
app.title("Добро пожаловать в Blackjack от 2XBET")
app.geometry("500x500")

# Загрузка GIF для фона окна оплаты
gif_path = "21-fon-forma.gif"
gif_image = Image.open(gif_path)
frames = [ImageTk.PhotoImage(gif_image.copy().convert('RGBA')) for _ in range(gif_image.n_frames)]
frames = itertools.cycle(frames)
def update_gif():
    if not bg_label.winfo_exists():
        return
    frame = next(frames)
    bg_label.config(image=frame)
    app.after(100, update_gif)
bg_label = tk.Label(app)
bg_label.place(relwidth=1, relheight=1)
update_gif()

app.iconbitmap("21-logo.ico")  # Иконка окна оплаты

# Стили для оплаты
label_style = {"bg": "#000000", "fg": "white", "font": ("Monotype Corsiva", 20, "bold")}
entry_style = {"bg": "#000000", "fg": "white", "insertbackground": "white", "bd": 3, "relief": "ridge", "font": ("Monotype Corsiva", 16, "bold")}
button_style = {"bg": "#333333", "fg": "white", "font": ("Monotype Corsiva", 16, "bold"), "bd": 2, "relief": "ridge"}

# Элементы окна оплаты
tk.Label(app, text="Введите сумму:", **label_style).place(x=100, y=50)
amount_entry = tk.Entry(app, **entry_style)
amount_entry.place(x=100, y=100, width=300, height=30)
tk.Label(app, text="Введите ваш email:", **label_style).place(x=100, y=150)
email_entry = tk.Entry(app, **entry_style)
email_entry.place(x=100, y=200, width=300, height=30)
create_payment_button = tk.Button(app, text="Пополнить", command=create_payment, **button_style, wraplength=200, justify='center')
create_payment_button.place(x=40, y=250, width=140, height=60)
check_payment_button = tk.Button(app, text="Начать игру", command=kontrolli_makset, **button_style, wraplength=130, justify='center')
check_payment_button.place(x=200, y=250, width=140, height=60)
exit_button = tk.Button(app, text="Выход", command=app.destroy, **button_style, wraplength=130, justify='center')
exit_button.place(x=360, y=250, width=80, height=60)

# --- Класс игры Blackjack с улучшенным интерфейсом ---
class BlackjackGame:
    def __init__(self, root, initial_balance):
        self.root = root
        self.root.title("Blackjack Game | 2XBET")
        self.root.geometry("700x600")
        self.user_balance = initial_balance

        # Фоновое изображение для игры
        try:
            bg_image = Image.open("casino.png")
            self.bg_photo = ImageTk.PhotoImage(bg_image.resize((800,600)))
            self.background_label = tk.Label(self.root, image=self.bg_photo)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print("Не удалось загрузить фон:", e)
            self.root.configure(bg="#004400")

        # Главный контейнер, разделенный на левую (управление игрой) и правую (история) части
        self.main_frame = tk.Frame(self.root, bg="#000000")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Левая часть: элементы управления игрой
        self.left_frame = tk.Frame(self.main_frame, bg="#000000", width=777)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)  # только по высоте
        self.left_frame.pack_propagate(False)

        # Правая часть: панель истории
        self.history_frame = tk.Frame(self.main_frame, bg="#000000", bd=4, relief=tk.RIDGE)
        self.history_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)

        # Фреймы в левой части
        self.top_frame = tk.Frame(self.left_frame, bg="#000000", bd=4, relief=tk.RIDGE)
        self.top_frame.pack(side=tk.TOP, fill=tk.X, pady=10)
        self.middle_frame = tk.Frame(self.left_frame, bg="#000000", bd=4, relief=tk.RIDGE)
        self.middle_frame.pack(side=tk.TOP, fill=tk.X, pady=5)
        self.button_frame = tk.Frame(self.left_frame, bg="#000000", bd=4, relief=tk.RIDGE)
        self.button_frame.pack(side=tk.TOP, fill=tk.X, pady=5)
        self.result_frame = tk.Frame(self.left_frame, bg="#000000", bd=4, relief=tk.RIDGE)
        self.result_frame.pack(side=tk.TOP, fill=tk.X, pady=5)
        self.cards_frame = tk.Frame(self.left_frame, bg="#004400", bd=4, relief=tk.RIDGE)
        self.cards_frame.pack(side=tk.TOP, fill=tk.X, pady=5)

        # Шрифты и цвета
        label_font = ("Papyrus", 18, "bold")
        label_font_small = ("Papyrus", 14, "bold")
        btn_font = ("Papyrus", 14, "bold")
        label_color = "#FFD700"
        entry_bg = "#333333"
        entry_fg = "#FFD700"
        btn_bg = "#444444"
        btn_fg = "#FFD700"

        # Верхний фрейм: ввод имени и кнопка Выход
        self.name_label = tk.Label(self.top_frame, text="Введите ваше имя:", font=label_font, bg="#000000", fg=label_color)
        self.name_label.pack(side=tk.LEFT, padx=5)
        self.name_entry = tk.Entry(self.top_frame, font=label_font_small, bg=entry_bg, fg=entry_fg, width=15)
        self.name_entry.pack(side=tk.LEFT, padx=5)
        self.exit_button = tk.Button(self.top_frame, text="Выход", command=self.root.destroy, font=btn_font, bg=btn_bg, fg=btn_fg, width=12)
        self.exit_button.pack(side=tk.RIGHT, padx=5)

        # Средний фрейм: баланс и подсказка
        self.balance_label = tk.Label(self.middle_frame, text=f"Ваш баланс: {self.user_balance:.2f} €", font=label_font_small, bg="#000000", fg=label_color)
        self.balance_label.pack(side=tk.LEFT, padx=10)
        self.label = tk.Label(self.middle_frame, text="Нажмите 'Начать игру'", font=label_font_small, bg="#000000", fg="#FFDEAD")
        self.label.pack(side=tk.LEFT, padx=10)

        # Фрейм кнопок игры
        self.start_button = tk.Button(self.button_frame, text="Начать игру", command=self.start_game, font=btn_font, bg=btn_bg, fg=btn_fg, width=12)
        self.start_button.pack(side=tk.LEFT, padx=5)
        self.hit_button = tk.Button(self.button_frame, text="Взять карту", command=self.hit, state=tk.DISABLED, font=btn_font, bg=btn_bg, fg=btn_fg, width=12)
        self.hit_button.pack(side=tk.LEFT, padx=5)
        self.stand_button = tk.Button(self.button_frame, text="Остановиться", command=self.stand, state=tk.DISABLED, font=btn_font, bg=btn_bg, fg=btn_fg, width=12)
        self.stand_button.pack(side=tk.LEFT, padx=5)
        self.history_button = tk.Button(self.button_frame, text="История", command=self.toggle_history, font=btn_font, bg=btn_bg, fg=btn_fg, width=12)
        self.history_button.pack(side=tk.LEFT, padx=5)

        # Фрейм результата
        self.result_label = tk.Label(self.result_frame, text="", font=("Papyrus", 16, "bold"), bg="#000000", fg="#FFD700")
        self.result_label.pack()

        # Фрейм для карт
        self.player_canvas = tk.Canvas(self.cards_frame, width=650, height=120, bg="#006600", highlightthickness=2, highlightbackground="#FFD700")
        self.player_canvas.pack(pady=5)
        self.computer_canvas = tk.Canvas(self.cards_frame, width=650, height=120, bg="#006600", highlightthickness=2, highlightbackground="#FFD700")
        self.computer_canvas.pack(pady=5)

        # Панель истории (справа)
        self.history_text = tk.Text(self.history_frame, height=20, width=30, state=tk.DISABLED, font=("Papyrus", 12), bg="#333333", fg="#FFD700")
        self.history_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.scrollbar = tk.Scrollbar(self.history_frame, command=self.history_text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.history_text.configure(yscrollcommand=self.scrollbar.set)
        self.history_visible = True

        # Проверка баланса
        if self.user_balance < 1:
            self.start_button.config(state=tk.DISABLED)
            self.label.config(text="Недостаточно средств для игры.", fg="red")


    # --------------- Методы игры ---------------
    def start_game(self):
        """Запуск новой партии. Очищаем предыдущие карты и раздаем новые."""
        if not self.name_entry.get().strip():
            self.label.config(text="Пожалуйста, введите своё имя!", fg="red")
            return
        if self.user_balance < 1:
            self.label.config(text="Недостаточно средств для игры.", fg="red")
            return

        # Очистка Canvas и списка карт компьютера
        self.player_canvas.delete("all")
        self.computer_canvas.delete("all")
        self.computer_cards = []

        self.user_balance -= 1
        self.balance_label.config(text=f"Ваш баланс: {self.user_balance:.2f} €")

        # Генерация и перемешивание колоды
        self.deck = [(value, suit) for value in CARD_VALUES for suit in SUITS]
        random.shuffle(self.deck)

        # Раздача начальных карт
        self.player_cards = [self.get_card(), self.get_card()]
        self.computer_cards = [self.get_card(), self.get_card()]

        self.update_cards()

        self.hit_button.config(state=tk.NORMAL)
        self.stand_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)

        # Проверка мгновенного блэкджека
        if sum(self.get_card_values(self.player_cards)) == 21:
            self.end_game("Блэкджек! Игрок выиграл!", "Победа")

    def get_card(self):
        """Берём карту из колоды."""
        return self.deck.pop() if self.deck else None

    def get_card_values(self, cards):
        """Возвращаем список номиналов карт."""
        return [card[0] for card in cards if card]

    def update_cards(self):
        """Обновляем отображение карт игрока и сумму очков."""
        player_sum = sum(self.get_card_values(self.player_cards))
        self.label.config(text=f"Сумма ваших очков: {player_sum}")
        self.draw_cards(self.player_cards, self.player_canvas)

    def draw_cards(self, cards, canvas, start_x=10, start_y=10, card_width=60, card_height=100, spacing=10):
        """Рисуем карты на заданном Canvas."""
        canvas.delete("all")
        x = start_x
        for value, suit in cards:
            text_color = "red" if suit in ["♥", "♦"] else "black"
            canvas.create_rectangle(x, start_y, x + card_width, start_y + card_height,
                                    fill="#FFFFFF", outline="#FFD700", width=2)
            text = f"{CARD_VALUES[value]} {suit}"
            canvas.create_text(x + card_width/2, start_y + card_height/2,
                               text=text, fill=text_color, font=("Papyrus", 16, "bold"))
            x += card_width + spacing

    def hit(self):
        """Добавляем карту игроку и обновляем отображение."""
        card = self.get_card()
        if card:
            self.player_cards.append(card)
            self.update_cards()
            if sum(self.get_card_values(self.player_cards)) > 21:
                self.end_game("Игрок проиграл! Перебор.", "Поражение")

    def stand(self):
        """Ход компьютера: раздаем карты до 17 и определяем победителя."""
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        while sum(self.get_card_values(self.computer_cards)) < 17:
            card = self.get_card()
            if card:
                self.computer_cards.append(card)
            else:
                break
        self.draw_cards(self.computer_cards, self.computer_canvas)
        self.determine_winner()

    def determine_winner(self):
        """Определяем победителя и формируем итоговое сообщение с именем игрока."""
        player_sum = sum(self.get_card_values(self.player_cards))
        computer_sum = sum(self.get_card_values(self.computer_cards))
        player_name = self.name_entry.get().strip() or "Игрок"
        result_text = f"{player_name}: {player_sum} | Компьютер: {computer_sum}\n"
        if computer_sum > 21 or player_sum > computer_sum:
            result_text += f"{player_name} выиграл!"
            result = "Победа"
        elif player_sum < computer_sum:
            result_text += "Компьютер выиграл!"
            result = "Поражение"
        else:
            result_text += "Ничья!"
            result = "Ничья"
        self.end_game(result_text, result)

    def end_game(self, message, result):
        """Завершаем игру: выводим сообщение и сохраняем результат."""
        self.result_label.config(text=message)
        if self.user_balance >= 1:
            self.start_button.config(state=tk.NORMAL)
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.save_result(result)

    def save_result(self, result):
        """Сохраняем результат игры в файл."""
        player_name = self.name_entry.get().strip() or "Игрок"
        with open("tulemused.txt", "a", encoding="utf-8") as file:
            file.write(f"{player_name} - {result} (Очки: {sum(self.get_card_values(self.player_cards))})\n")

    def show_history(self):
        """Отображаем историю игр в правой части окна."""
        if not os.path.exists("tulemused.txt"):
            history = "История отсутствует."
        else:
            with open("tulemused.txt", "r", encoding="utf-8") as file:
                history = file.read()
        self.history_text.config(state=tk.NORMAL)
        self.history_text.delete(1.0, tk.END)
        self.history_text.insert(tk.END, history)
        self.history_text.config(state=tk.DISABLED)

    def toggle_history(self):
        if self.history_visible:
            self.history_frame.pack_forget()
            self.history_visible = False
            self.history_button.config(text="История")
        else:
            self.history_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)
            self.history_visible = True
            self.history_button.config(text="История")
            self.show_history() 

# ------------------ Запуск окна оплаты ------------------ #
app.mainloop()
