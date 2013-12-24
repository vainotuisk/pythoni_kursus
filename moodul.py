import random, math,pygame
juhuarv = random.randint(0,10)
# print juhuarv
for i in range(10):
    juhuarv = random.randint(0,10)
    print "Juhuarv "+str(i)+ " on " + str(juhuarv)

# listiga jarjendiga
arvud =[]
for i in range(10):
    arvud.append(random.randint(0,10))
print arvud
print "==== math moodul: ======="
print round(math.pi,2)
print "==== pygame moodul: ======="
