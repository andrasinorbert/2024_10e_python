class Adatsor:
    def __init__(self, nev:str, szamlista:list[int]):
        self.nev=nev
        self.szamok=szamlista
    
    def __str__(self):
        return f"{self.nev} {self.szamok}"
    
    def osszeg(self):
        return sum(self.szamok)
    
    def atlag(self):
        return self.osszeg()/len(self.szamok)
    
class AdatsorLista:
    def __init__(self):
        self.lista=[]
    
    def hozzaad(self, adatsor:Adatsor):
        self.lista.append(adatsor)
    
    def getIndexByName(self, name):
        i=0
        while i<len(self.lista) and self.lista[i].nev!=name:
            i=i+1
        if i<len(self.lista):
            return i
        else:
            return None
    
    def getElementByIndex(self, index):
        return self.lista[index]
