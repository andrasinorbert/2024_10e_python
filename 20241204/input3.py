"""
1;2;3;4;5
6;7;8;9;10
11;12;13;14;15
"""

file=open("input3")
sorok=file.readlines()
file.close()

print(sorok)

szammatrix=[]
for i in range(len(sorok)):
    sor=sorok[i].strip()
    print(sor)
    sorlista=sor.split(";")
    print(sorlista)
    szamsor=[]
    for i in range(len(sorlista)):
        szam=int(sorlista[i])
        szamsor.append(szam)
    print(szamsor)
    szammatrix.append(szamsor)
    
print(szammatrix)

s=0
for i in range(len(szammatrix)):
    egysor=szammatrix[i]
    for j in range(len(egysor)):
        s+=egysor[j]
print(f"összeg: {s}")

def beolvas(filename:str):
    file=open(filename)
    sorok=file.readlines()
    file.close()
    return sorok

def listaConvertStrToInt(lista:list):
    szamsor=[]
    # [szamsor.append(int(lista[i])) for i in range(len(lista))]
    for i in range(len(lista)):
        szamsor.append(int(lista[i]))
    return szamsor

def strStripSplit(szoveg, elvalasztoChar):
    return szoveg.strip().split(elvalasztoChar)

def szovegMatrixToIntMatrix(matrix:list[list[str]], elvalasztoChar):
    szammatrix=[]
    for i in range(len(matrix)):
        sorlista=strStripSplit(matrix[i], elvalasztoChar)
        szamsor=listaConvertStrToInt(sorlista)
        szammatrix.append(szamsor)
        #szammatrix.append(listaConvertStrToInt(strStripSplit(matrix[i])))
    #[szammatrix.append(listaConvertStrToInt(strStripSplit(matrix[i]))) for i in range(len(matrix))]
    return szammatrix

filename="input3"
sorok=beolvas(filename)
szammatrix=szovegMatrixToIntMatrix(sorok, ";")
print(szammatrix)