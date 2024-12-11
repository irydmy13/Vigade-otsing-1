from math import * #исправила порядок слов

print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => ")) #добавила преобразование в число float, исправила некорректно написаные кавычки
S=a**2
print("Ruudu pindala", round(S, 2)) #добавила округление до сотых
P=4*a
print("Ruudu ümbermõõt", round(P, 2)) #некорректно написаны кавычки, добавила округление до сотых
di=a*sqrt(2) #исправила sqr на sqrt, убрала "math"
print("Ruudu diagonaal", round(di,2))
print()

print("Ristküliku karakteristikud") #лишняя скобка, убрала
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #добавила float
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #добавила float
S=b*c
print("Ristküliku pindala", round(S, 2)) #кавычки, добавила округление до сотых
P=2*(b+c) #добавила знак умножения перед скобками
print("Ristküliku ümbermõõt", round(P, 2)) #добавила округление до сотых
di=sqrt(b**2+c**2) #убрала math.
print("Ristküliku diagonaal", round(di, 2)) #скобки не хватало, добавила округление до сотых
print()

print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) #некорректные кавычки, лишняя скобка, добавила float  
d=2*r #добавила знак умножения
print("Ringi läbimõõt", round(d, 2)) #добавила запятую, округление до сотых
S=pi*r**2  #исправила pi() на pi, и r*2 на r**2 для корректной формулы площади круга
print("Ringi pindala", round(S, 2)) #добавила округление до сотых
C=2*pi*r #знак умножения, исправила pi() на pi
print("Ringjoone pikkus", round(C, 2)) #не хватало одной скобки, добавила округление до сотых