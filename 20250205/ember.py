class Ember:
    def __init__(self, _nev:str, _kor:int):
        self.nev = _nev
        self.kor = _kor
        
    def getNev(self):
        return self.nev
    
    def getKor(self):
        return self.kor
    
    def setNev(self, ujNev:str):
        self.nev = ujNev
        
    def setKor(self, ujKor:int):
        self.kor = ujKor
        
    def eszik(self):
        print(f"{self.nev} eszik")
    
    def iszik(self):
        print(f"{self.nev} iszik")
        
class Tanulo(Ember):
    def __init__(self, _nev:str, _kor:int, _kretaID:int):
        super().__init__(_nev, _kor)
        self.kretaID=_kretaID
        
    def getKretaID(self):
        return self.kretaID
    
    def setKretaID(self, ujID):
        self.kretaID=ujID
        
    def tanul(self):
        print(f"{self.nev} tanul")
        
    def jatszik(self):
        print(f"{self.nev} játszik")

class Munkas(Ember):
    def __init__(self, _nev:str, _kor:int, _ber:int):
        super().__init__(_nev, _kor)
        self.ber = _ber
        
    def getBer(self)->int:
        return self.ber
    
    def setBer(self, ujBer:int):
        self.ber = ujBer
    
    def dolgozik(self):
        print(f"{self.nev} dolgozik")