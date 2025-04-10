filename="input4.txt"

f=open(filename, encoding="utf-8")
sorok=f.readlines()
f.close()

print(sorok) # ['1 2 3 4 5\n', '2 3 4 5 6\n', '3 4 5 6 7']

nevek=[]
matrix=[]
for i in range(len(sorok)):
    egysor=sorok[i] # '1 2 3 4 5\n'
    feleslegmentesitett_szoveg=egysor.strip() # '1 2 3 4 5'
    szokozonkent_bontva=feleslegmentesitett_szoveg.split(" ")
    print(szokozonkent_bontva) # ['1', '2', '3', '4', '5']
    szamok=[]
    for j in range(1,len(szokozonkent_bontva)):
        szam=int(szokozonkent_bontva[j])
        szamok.append(szam)
    print(szamok) # [1, 2, 3, 4, 5]
    nevek.append(szokozonkent_bontva[0])
    matrix.append(szamok)
print(matrix) # [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
print(nevek)
# rövidebben

nevek=[]
matrix=[]
for i in range(len(sorok)):
    szokozonkent_bontva=sorok[i].strip().split(" ")
    szamok=[]
    for j in range(1,len(szokozonkent_bontva)):
        szamok.append(int(szokozonkent_bontva[j]))
    matrix.append(szamok)
    nevek.append(szokozonkent_bontva[0])
print(matrix) # [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]]
print(nevek)

# függvényként
def beolvas(filename):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()

    nevek=[]
    matrix=[]
    for i in range(len(sorok)):
        szokozonkent_bontva=sorok[i].strip().split(" ")
        szamok=[]
        for j in range(1,len(szokozonkent_bontva)):
            szamok.append(int(szokozonkent_bontva[j]))
        matrix.append(szamok)
        nevek.append(szokozonkent_bontva[0])
    return nevek,matrix

filename="input4.txt"
x,y=beolvas(filename)
print(y)
print(x)