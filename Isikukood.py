ikoodid = []  # список верных кодов
arvud = []  # список неверных кодов

haiglad = {
    range(1, 11): "Kuressaare Haigla",
    range(11, 20): "Tartu Ülikooli Naistekliinik, Tartumaa, Tartu",
    range(21, 221): "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla",
    range(221, 271): "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)",
    range(271, 371): "Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla",
    range(371, 421): "Narva Haigla",
    range(421, 471): "Pärnu Haigla",
    range(471, 491): "Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla",
    range(491, 521): "Järvamaa Haigla (Paide)",
    range(521, 571): "Rakvere, Tapa haigla",
    range(571, 601): "Valga Haigla",
    range(601, 651): "Viljandi Haigla",
    range(651, 701): "Lõuna-Eesti Haigla (Võru), Põlva Haigla"
}

def kontrollnumber(code):  # вычисляем контрольный номер
    astme_kaal1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    astme_kaal2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

    sum1 = sum(int(code[i]) * astme_kaal1[i] for i in range(10))
    ule_osa1 = sum1 % 11

    if ule_osa1 != 10:
        return ule_osa1

    sum2 = sum(int(code[i]) * astme_kaal2[i] for i in range(10))
    ule_osa2 = sum2 % 11

    return ule_osa2 if ule_osa2 != 10 else 0

def hoiused(number):  # место рождения
    for range_key, place in haiglad.items():
        if number in range_key:
            return place
    return "Неизвестное место"

def isikukood(code):  # проверяем корректность кода
    if len(code) != 11 or not code.isdigit():
        return False

    if int(code[0]) not in range(1, 7):
        return False

    aastal = 1800 + ((int(code[0]) - 1) // 2) * 100
    year = aastal + int(code[1:3])
    month = int(code[3:5])
    day = int(code[5:7])

    try:
        from datetime import datetime
        datetime(year, month, day)
    except ValueError:
        return False

    lnumber = int(code[7:10])
    control = kontrollnumber(code)

    return control == int(code[10])

while True:
    code = input("Введите Isikukood или 'STOP' для выхода: ")
    if code.strip().upper() == "STOP":
        break

    if isikukood(code):
        gender = "женщина" if int(code[0]) % 2 == 0 else "мужчина"
        aastal = 1800 + ((int(code[0]) - 1) // 2) * 100
        year = aastal + int(code[1:3])
        month = int(code[3:5])
        day = int(code[5:7])
        lnumber = int(code[7:10])
        place = hoiused(lnumber)

        ikoodid.append(code)
        print(f"Это {gender}, его/ее день рождения {day:02}.{month:02}.{year}, место рождения {place}.")
    else:
        arvud.append(code)
        print("Некорректный Isikukood.")

# Сортировка и вывод результатов
    ikoodid_sorted = sorted(ikoodid)
    arvud_sorted = sorted(arvud)

    print("\nКорректные коды:", ikoodid_sorted)
    print("Некорректные коды:", arvud_sorted)