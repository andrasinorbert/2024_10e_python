def beolvas(filename:str):
    file=open(filename, encoding="utf-8")
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
