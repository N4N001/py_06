import re
heslo="test"
if len(heslo)<6: 
    print("Heslo je příliš krátké! Nejméně 6 znaků.")
if len(heslo)>16:
    print("Heslo je příliš dlouhé! Nejvíce 16 znaků.")
x=re.findall("[0-9]", heslo)
if not x:
    print("Heslo musí obsahovat čísla!")
y=re.findall("$", heslo)
y=re.findall("#", heslo)
y=re.findall("@", heslo)
if not y:
    print("Heslo musí obsahovat speciální znak $, nebo #, nebo @!")
z=re.findall("[A-Z]", heslo)
if not z:
    print("Heslo musí obsahovat velké písmeno")
a=re.findall("[a-z]", heslo)
if not a:
    print("Heslo musí obsahovat malé písmeno")
else: 
    print("Vaše heslo je v pořádku!")
input("Stiskni klávesu ENTER pro ukončení programu")