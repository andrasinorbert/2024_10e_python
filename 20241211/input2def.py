def sorfeldolgozo(szoveg:str, elvalasztoChar:str=" "):
    # 'Géza 1 2 3 4 5\n'
    sor=szoveg.strip()
    sor2=sor.split(elvalasztoChar)
    name=sor2[0]
    szamoklista=[]
    for i in range(1,len(sor2)):
        szamoklista.append(int(sor2[i]))
    
    return name, szamoklista

def feldolgoz(sorok:list[str], elvalasztoChar:str=" "):
    nevek=[]
    szamoklista=[]
    for i in range(len(sorok)):
        egysor=sorfeldolgozo(sorok[i], elvalasztoChar)
        nevek.append(egysor[0])
        szamoklista.append(egysor[1])
    return nevek, szamoklista