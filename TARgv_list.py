spisok=[] #������ ������
numbers=[1,2,3,4,5]
abc=['Abc','B','C'] #������ �� ���� ��� ������
slovo="Programmeerimine"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)
while True:
  print("1-�������� ����� � ������ ")
  print("2-������� ������\n3-�������� ����� �� i-������� ")
  print("4-������� ������� ")
  valik=int(input())
  if valik==1:
   a=input("������� ����� ")
   slovo_list.append(a)
   print(f"�������� ����� {a} ������ ", slovo_list)
  elif valik==2:
   slovo_list.extend(abc)
   print(slovo_list)
  elif valik==3:
   a=input("����� �����, ������� ������ �������� ")
   i=int(input("����� ����� �������, ���� ������ �������� ����� "))
   slovo_list.insert(i-1,a) #0,1,2...
   print(slovo_list)
  elif valik==4:
   a=input("����� �����, ������� ������ ������� ")
   n=slovo_list.count(a)
   if n>0:
    for i in range(n):
     slovo_list.remove(a)
   else:
    print("����� ����� ���")
   print(slovo_list)
