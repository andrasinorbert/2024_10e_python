def szelsoertekkivalasztas(lista:list,f:bool)->tuple[int,int]:
    """Egy lista utolsó/első min/max értékét adja vissza az f függvény paraméter szerint

    Args:
        lista (list): lista, amely számokat tárol
        f (bool): Egy 2 paraméteres függvény, amely egy bool értékkel tér vissza; a lista egy értékét hasonlítja össze a jelenlegi min/max-szal

    Returns:
        tuple[int,int]: 0. helyen az index-szel, 1. helyen az értékkel
    """
    ertek=lista[0]
    index=0
    for i in range(1,len(lista)):
        if f(lista[i],ertek): # itt változik!
            ertek=lista[i]
            index=i
    return (index, ertek)

print(szelsoertekkivalasztas([1,3,6,4,2],lambda num1,num2:num1<num2))

lista=[]
for i in range(10):
    lista.append(i)
print(lista)

#list comprehension
lista=[]
[lista.append(i) for i in range(10)]
print(lista)

x=10
if x>5:
    y=1
else:
    y=0
print(y)

y=1 if x>5 else 0
print(y)

def megszamlalas(lista,T):
    c=0
    for i in range(len(lista)):
        if T(lista[i]):
            c+=1
    return c

print(megszamlalas([1,2,3,4,5],lambda num: num%2==0))

def megszamlalas2(lista,T):
    c=0
    for i in range(len(lista)):
        c+=1 if T(lista[i]) else 0
    return c

print(megszamlalas2([1,2,3,4,5],lambda num: num%2==0))

def eldontes(lista,T:bool) -> bool:
    i=0
    while i<len(lista) and not(T(lista[i])):
        i+=1
    return i<len(lista)

print(eldontes([1,2,3,4,5], lambda num: num==3))

def eldontes2(lista,T:bool) -> bool:
    i=0
    while i<len(lista) and not(T(lista[i])): i+=1
    return i<len(lista)

print(eldontes2([1,2,3,4,5], lambda num: num==3))