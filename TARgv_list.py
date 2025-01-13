spisok=[] #пустой список
numbers=[1,2,3,4,5]
abc=['Abc','B','C'] #список из букв или текста
slovo="Programmeerimine"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)
while True:
  print("1-добавить букву в список ")
  print("2-склеить списки\n3-добавить букву на i-позицию ")
  print("4-удалить элемент ")
  valik=int(input())
  if valik==1:
   a=input("Введите букву ")
   slovo_list.append(a)
   print(f"Добавили новый {a} список ", slovo_list)
  elif valik==2:
   slovo_list.extend(abc)
   print(slovo_list)
  elif valik==3:
   a=input("Введи букву, которую хочешь добавить ")
   i=int(input("Введи номер позиции, куда хочешь добавить букву "))
   slovo_list.insert(i-1,a) #0,1,2...
   print(slovo_list)
  elif valik==4:
   a=input("Введи букву, которую хочешь удалить ")
   n=slovo_list.count(a)
   if n>0:
    for i in range(n):
     slovo_list.remove(a)
   else:
    print("Такой буквы нет")
   print(slovo_list)
