"""
1;2;3;4;5
6;7;8;9;10
11;12;13;14;15
"""
import funcs

filename="input1"
szammatrix=funcs.szovegMatrixToIntMatrix(funcs.beolvas(filename), ";")
print(szammatrix)

s=0
for i in range(len(szammatrix)):
    s+=szammatrix[i][0]
print(f"első adatok összege: {s}")