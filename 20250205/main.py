from ember import *

a=Ember("Béla", 14)
print(a.nev)
print(a.kor)
a.nev="Béla2"
a.kor=15
print(a.nev)
print(a.kor)
a.eszik()
a.iszik()

t=Tanulo("Gipsz Jakab", 15, 123)
print(t.getNev())
print(t.getKor())
print(t.getKretaID())
t.setKretaID(321)
print(t.getKretaID())
t.tanul()
t.jatszik()
t.eszik()
t.iszik()

m=Munkas("Józsi", 50, 10000)
print(m.getNev())
print(m.getKor())
print(m.getBer())
m.setBer(m.getBer()-1000)
print(m.getBer())
m.dolgozik()