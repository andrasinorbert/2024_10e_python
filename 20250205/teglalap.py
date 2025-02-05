class Teglalap:
    def __init__(self, _oldal1, _oldal2):
        self.oldal1 = _oldal1
        self.oldal2 = _oldal2
    
    def kerulet(self):
        return 2 * (self.oldal1 + self.oldal2)
    
    def terulet(self):
        return self.oldal1 * self.oldal2
    
    def atlo(self):
        return (self.oldal1**2 + self.oldal2**2)**0.5
        
class Negyzet(Teglalap):
    def __init__(self, _oldal):
        super().__init__(_oldal, _oldal)