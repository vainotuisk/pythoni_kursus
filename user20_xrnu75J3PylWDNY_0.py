# ülesanne
arv = input("Mis arv?")
arv = int(arv)
if arv < 0:
    print "Arv " + str(arv)+" on negatiivne."
elif arv >0:
    print "Arv " + str(arv)+" on positiivne."
else:
    print "Arv " + str(arv)+" pole positiivne ega negatiivne."