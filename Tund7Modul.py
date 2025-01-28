from random import *
# from asyncio import AbstractEventLoop


# def summa3(arv1:int,arv2:int,arv3:int)->int:
#     """Tagastab kolme taisarvu summa

#     :param int arv1: Esimene number
#     :param int arv2: Teine number
#     :param int arv3: Kolmas number
#     :rtype: int

#     """
#     summa=arv1+arv2+arv3
#     return summa

# #ulesanne1
# def arithmetic(a:float, b:float, t:str)->any:
#     """Lihtne kalkulaator.
#     + - liitmine
#     - - lahutamine
#     * - korrutamine
#     / - jagamine
#     :param float a: arv1
#     :param float b: arv2
#     :param str t: atitmeetiline tehing
#     :rtype: var Maaramata tuup(float or str)
#     """
#     if t in ["+","-","*","/"]:
#         if b==0 and t=="/":
#             vastus="DIV/0"
#         else:
#             vastus=eval(str(a)+t+str(b))
#     else:
#         vastus="Tundmatu tehe"

#     return vastus

# #ulesanne2
# def is_year_leap(aasta:int)->bool:

#     """Liigaasta leidmine
#     Tagastab True, kui liigaasts ja False kui on tavaline aasta.
#     :param int asta: aasta number
#     :rtype: bool tagastab loogilises formaadis tulemus
#     """

#     if aasta%4==0:
#         v=True
#     else:
#         v=False
#     return v

# #ulesanne3
# def square_text(a:float)->str:
#     """Ruut

#     :Kirjutage funktsiooni ruut, mis votab 1 argumendi - ruudu 
#     :kulje ja tagastab 3 vaartust: ruudu umbermoot, 
#     :ruudu pindala ja ruudu diagonaal.
    
#     """
#     S=a**2
#     P=4*a
#     d=(2)**(1/2)*a
#     return (f"S: {S}, P: {P}, d: {round(d,2)}")

# #ulesanne4
# def season(param:int)->str:
#     """
#     """
#     if 1<=param<=12:
#         if param in [1,2,12]:
#             v="talv"
#         elif param>2 and param<6:
#             v="kevad"
#         elif 6<=param<=8:
#             v="suvi"
#         else:
#             v="sugis"
#     else:
#         v="!!!!"
#     return v

#ulesanne5


#ulesanne6
def is_prime(a=randint(0,1000))->bool:
    """
    """
    print (a)
    v=True
    for i in range(2,a):
        if a%i==0:
            v=False

    return v

#ulesanne7
def date(paev:int,kuu:int,aasta:int)->bool:
    ""
    ""
    if paev in range(1,31) and kuu in [1,3,5,7,8,10,12]:
        v=True
    elif paev in range(1,29) and kuu==2 and is_year_leap(aasta):
        v=True
    elif paev in range(1,30) and kuu in [2,4,6,9,11]:
        v=True
    else:
        v=False
    return v


