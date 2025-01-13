my_list = [] #������ ������ 

my_list.append("����������") #������ �� ���������
my_list.append("������")
print("����� ���������� ���������:", my_list)

my_list.extend(["�������", "���������", "�����������"]) #���������� ������ � ������� �������
print("����� ����������:", my_list)

# ��������� ������� �� ������������ �������
my_list.insert(2, "���������")
print("����� ������� ���������:", my_list)

# ������� ������� �� ��������
my_list.remove("������")
print("����� �������� ��������:", my_list)

# ������� ��������� ������� � ���������� ���
removed_item = my_list.pop()
print("��������� �������:", removed_item)
print("����� �������� ���������� ��������:", my_list)

# �������� ������ ������� ��������� ��������
index = my_list.index("apple")
print("������ 'apple':", index)

# ������������ ���������� ������������ ���������
count = my_list.count("apple")
print("���������� 'apple' � ������:", count)

# ��������� ������
my_list.sort()
print("����� ����������:", my_list)

# ������������� ������
my_list.reverse()
print("����� ���������:", my_list)

# �������� ������
copied_list = my_list.copy()
print("����� ������:", copied_list)

# ������� ������
my_list.clear()
print("����� �������:", my_list)

# ������ �� ��������
text = "Hello, World!"
print("\n������ �� ��������:")
print("�������� �����:", text)
print("����� ������:", len(text))
print("������ � ������� ��������:", text.upper())
print("������ � ������ ��������:", text.lower())
print("������ �����:", text.replace("World", "Python"))
print("��������, ���������� �� ������ � 'Hello':", text.startswith("Hello"))
print("��������, ������������� �� ������ �� '!':", text.endswith("!"))

