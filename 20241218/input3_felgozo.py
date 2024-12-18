f=open("input3.txt", encoding="utf-8")
sorok=f.readlines()
f.close()

print(sorok)

nevek=[]
matrix=[]
for i in range(len(sorok)):
    sor=sorok[i].strip()
    lista=sor.split(" ")
    print(lista)
    nevek.append(lista[0])
    szamlista=[]
    for j in range(1,len(lista)):
        szam=int(lista[j])
        szamlista.append(szam)
    matrix.append(szamlista)
    
print(nevek)
print(matrix)

keresendonev="Győző"
i=0
while i<len(nevek) and nevek[i]!=keresendonev:
    i+=1
# Ha az i<len(nevek), akkor megtaláltuk

nevindex=i
print(nevindex)
szamai=matrix[nevindex]
print(szamai)

# Keddi nap indexe=1
napindex=1
print(f"{keresendonev} keddi napján {szamai[napindex]} db kókuszgolyót csinált")
