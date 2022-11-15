from random import randrange


cislo=randrange(1,11)
tip=-1
while int(cislo)!=int(tip):
    tip=input("Kolik je číslo?")
    if int(cislo)==int(tip):
        print("Ano, správně. Číslo je",cislo)
    if int(cislo)>int(tip):
        print("Ne, číslo je větší")
    if int(cislo)<int(tip):
        print("Ne, číslo je menší")
input("Stiskni klávesu ENTER pro ukončení programu")