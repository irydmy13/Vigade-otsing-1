my_list = [] #Пустой список 

my_list.append("Математика") #Список из придметов
my_list.append("Физика")
print("После добавления предметов:", my_list)

my_list.extend(["История", "География", "Физкультура"]) #Расширение списка с помощью другого
print("После расширения:", my_list)

# Вставляем элемент на определенную позицию
my_list.insert(2, "Рисование")
print("После вставки предметов:", my_list)

# Удаляем элемент по значению
my_list.remove("Физика")
print("После удаления предмета:", my_list)

# Удаляем последний элемент и возвращаем его
removed_item = my_list.pop()
print("Удаленный элемент:", removed_item)
print("После удаления последнего элемента:", my_list)

# Получаем индекс первого вхождения элемента
index = my_list.index("apple")
print("Индекс 'apple':", index)

# Подсчитываем количество определенных элементов
count = my_list.count("apple")
print("Количество 'apple' в списке:", count)

# Сортируем список
my_list.sort()
print("После сортировки:", my_list)

# Разворачиваем список
my_list.reverse()
print("После разворота:", my_list)

# Копируем список
copied_list = my_list.copy()
print("Копия списка:", copied_list)

# Очищаем список
my_list.clear()
print("После очистки:", my_list)

# Работа со строками
text = "Hello, World!"
print("\nРабота со строками:")
print("Исходный текст:", text)
print("Длина строки:", len(text))
print("Строка в верхнем регистре:", text.upper())
print("Строка в нижнем регистре:", text.lower())
print("Замена слова:", text.replace("World", "Python"))
print("Проверка, начинается ли строка с 'Hello':", text.startswith("Hello"))
print("Проверка, заканчивается ли строка на '!':", text.endswith("!"))

