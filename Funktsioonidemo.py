#   Programmeerimine huviringis (Python)
#     
#   Funktsiooni mõiste demoülesanne     
#   
#
#   Väino Tuisk
#   27.11.2013
# -*- coding: utf-8 -*-
# Ülesanne
# Koosta programm, mis küsib konsoolil kasutajalt 2 arvu ning seejärel mis tehe nendega teha. 
# Programm väljastab konsoolile tulemuse.

arv1 = float(input("Sisesta 1. arv "))
arv2 = float(input("Sisesta 2. arv "))
tehe = "suvaline"
print("Sisesta + liita, - lahutada, *  korrutada või / jagada ")
while tehe not in "*+-/":
    tehe = input("Mis tehet arvudega teha? ")

#Funktsioonid
def liida(x,y):
    tehe = "Liitmise"
    return tehe,x+y
def lahuta(x,y):
    tehe = "Lahutamise"
    return tehe,x-y
def korruta(x,y):
    tehe = "Korrutamise"
    return tehe,x*y
def jaga(x,y):
    tehe = "Jagamise"
    if(y==0):
        pass
    else:
        return tehe,round(x/y,2)


if tehe == "+":
     vastus = liida(arv1,arv2)
elif tehe == "-":
    vastus = lahuta(arv1,arv2)
elif tehe == "*":
    vastus = korruta(arv1,arv2)
elif tehe == "/":
    vastus = jaga(arv1,arv2)
else:
    print ("Tupik!")

print (vastus[0] + " vastus on: " + str(vastus[1]))


