
l=[1,2,3,4,5]


def ki(szoveg):
    print(szoveg)

ki("haho")
ki([2,3,4])
valt=654
ki(valt)

print("szia", "Zoli")
print("szia", "Zoli", sep="; ")
l=[1,2,3,4,5]
for i in range(len(l)):
    print(l[i], end=" ")
print()
print("János")


for i in range(10):
    print(i, end=" ") # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(5,10):
    print(i, end=" ") # 5 6 7 8 9
print()

for i in range(2,10,3):
    print(i, end=" ") # 2 5 8
print()

def ki2(*szoveg):
    print(*szoveg)
    
ki2("szia", "Zoli")

def ki3(*args, **kwargs):
    print(kwargs)
    print(*args, **kwargs)

ki3("szia", "Zoli", sep="; ")

l=[1,2,3,4,5]

def osszeg(lista):
    s=0
    for i in range(len(lista)):
        s+=lista[i]
    return s

print(osszeg(l))

def szorzat(lista):
    s=lista[0]
    for i in range(1,len(lista)):
        s*=lista[i]
    return s

print(szorzat(l))

def osszegzes(lista, f):
    s=lista[0]
    for i in range(1,len(lista)):
        s=f(s,lista[i])
    return s

def osszead(x,y):
    return x+y

print(osszegzes(l, osszead))

def szorzas(x,y):
    return x*y

print(osszegzes(l, szorzas))

x= lambda szam1,szam2 : szam1+szam2

print(x(2,3))

print(osszegzes(l, lambda n,m:n*m))

def maxkivalasztas(lista):
    maxertek=lista[0]
    maxindex=0
    for i in range(1,len(lista)):
        if lista[i]>maxertek:
            maxertek=lista[i]
            maxindex=i
    return (maxindex, maxertek)

l2=[2,6,5,9,3]
print(maxkivalasztas(l2))

def minkivalasztas(lista):
    minertek=lista[0]
    minindex=0
    for i in range(1,len(lista)):
        if lista[i]<minertek: # itt változik!
            minertek=lista[i]
            minindex=i
    return (minindex, minertek)

print(minkivalasztas(l2))

def szelsoertekkivalasztas(lista:list,f:function)->tuple[int,int]:
    """_summary_

    Args:
        lista (list): _description_
        f (function): _description_

    Returns:
        tuple[int,int]: _description_
    """
    ertek=lista[0]
    index=0
    for i in range(1,len(lista)):
        if f(lista[i],ertek): # itt változik!
            ertek=lista[i]
            index=i
    return (index, ertek)

def min(szam1, szam2):
    return szam1<szam2

print(szelsoertekkivalasztas(l2,min))

def max(szam1, szam2):
    return szam1>szam2

print(szelsoertekkivalasztas(l2,max))


print(szelsoertekkivalasztas(l2,lambda n1, n2:n1<n2))#min
print(szelsoertekkivalasztas(l2,lambda n1, n2:n1>n2))#max
