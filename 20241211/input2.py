import funcs
import input2def

filename="input2"
matrix=funcs.beolvas(filename)
#print(matrix)
(nevek, szamlista)=input2def.feldolgoz(matrix, " ")
print(nevek)
print(szamlista)

# Hány kókuszgolyót készített Gizella?
i=0
while i<len(nevek) and not(nevek[i]=="Gizella"):
    i+=1
#gizellaindex=i
s=0
for j in range(len(szamlista[i])):
    s+=szamlista[i][j]
print(f"Gizella {s} db kókuszgolyót készített")

# Az első napon hány kókuszgolyó készült?
napindex=0
s=0
for i in range(len(szamlista)):
    s+=szamlista[i][napindex]
print(f"Az első napon {s} db kókuszgolyó készült")

# Ki készítette szerdán a legtöbb kókuszgolyót?
napindex=2

maxertek=szamlista[0][napindex]
maxindex=0
for i in range(1,len(szamlista)):
    if szamlista[i][napindex]>maxertek:
        maxertek=szamlista[i][napindex]
        maxindex=i
print(f"Szerdán a legtöbbet {nevek[maxindex]} készítette")