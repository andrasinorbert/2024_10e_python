
l=[3,4,5,6,7]

s=0
for i in range(len(l)):
    s+=l[i]

print(s)

def osszeadja_a_lista_elemeit(lista):
    s=0
    for i in range(len(lista)):
        s+=lista[i]
    return s

l=[3,4,5,6,7]
osszeg=osszeadja_a_lista_elemeit(l)
print(osszeg)

l=[3,4,5,6,7]

c=0
for i in range(len(l)):
    if l[i]%2==0:
        c+=1
print(f"A páros számok darabszáma: {c}")

def paros_szamok_darabszama(lista):
    c=0
    for i in range(len(lista)):
        if lista[i]%2==0:
            c+=1
    return c

l=[3,4,5,6,7]
darab=paros_szamok_darabszama(l)
print(f"A páros számok darabszáma: {darab}")