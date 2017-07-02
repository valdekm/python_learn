def funkcja():
    print("dupa")

def funkcja2(imie):
    print("Hi " + imie)

funkcja()
costam = raw_input("wpisz cos> ")
funkcja2(costam)

ceny=[1,2,3,4,5]
ceny2=[6,7,8,9,20]

def sumuj(lista):
    suma=0
    for i in lista:
        suma+=i
    #print(str(suma))
    return suma

nowasuma=sumuj(ceny)
print(nowasuma)
print(sumuj(ceny2))
