import json

# Функция проверки email
def is_valid_email(email):
    return "@" in email and "." in email

# Ввод данных от пользователя
company_name = input("Sisestage oma ettevõtte nimi: ")

# Проверка email
while True:
    contact_email = input("Sisestage oma isiklik e-mail address: ")
    if is_valid_email(contact_email):
        break
    else:
        print("Viga! Sisestage kehtiv e-posti aadress, milles on '@'.")

data_collection = input("Millised andmed salvestame: ")
data_usage = input("Kuidas andmeid kasutatakse: ")
data_storage_limit = input("Kui kaua andmeid salvestatakse: ")

# Вопрос о куках
while True:
    cookies_consent = input("Kas nõustute küpsiste kasutamisega? (jah/ei): ").strip().lower()
    if cookies_consent in ["jah", "ei"]:
        break
    else:
        print("Palun sisestage 'jah' või 'ei'.")

# Создание словаря с данными
privacy_data = {
    "company_name": company_name,
    "contact_email": contact_email,
    "data_collection": data_collection,
    "data_usage": data_usage,
    "data_storage_limit": data_storage_limit,
    "cookies_consent": "Nõustunud" if cookies_consent == "jah" else "Ei nõustu"
}

# Сохранение в JSON
with open("privacy_template.json", "w", encoding="utf-8") as file:
    json.dump(privacy_data, file, indent=4, ensure_ascii=False)
print("Kõik oli edukalt salvestatud.")

# HTML-шаблон
html_template = """
<!DOCTYPE html>
<html lang="et">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privaatsuspoliitika</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }}
        h1, h2 {{ color: #2c3e50; }}
        p {{ color: #34495e; }}
    </style>
</head>
<body>
    <h1>Privaatsuspoliitika ettevõttele - {company_name}</h1>
    <p><strong>Kontakt:</strong> {contact_email}</p>
    
    <h2>Milliseid andmeid kogume?</h2>
    <p>{data_collection}</p>
    
    <h2>Kuidas andmeid kasutatakse?</h2>
    <p>{data_usage}</p>
    
    <h2>Kui kaua andmeid salvestame?</h2>
    <p>{data_storage_limit}</p>

    <h2>Küpsiste kasutamine</h2>
    <p>{cookies_consent}</p>
</body>
</html>
"""

# Генерация HTML-файла
privacy_policy = html_template.format(**privacy_data)

with open("privacy_policy.html", "w", encoding="utf-8") as file:
    file.write(privacy_policy)
print("HTML fail genereeritud edukalt.")
