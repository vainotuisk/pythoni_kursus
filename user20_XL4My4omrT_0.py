nimi = input ("Mis su nimi? ")
vanus = input("Mis su vanus? ")
print "Tere " + nimi + "! Oled " + vanus + " aastat vana."
vanus = int(vanus)
sobravanus = input("Sobra vanus: ")
sobravanus = int(sobravanus)
kokku = str(vanus + sobravanus)
print "Sober on " + str(sobravanus) +". Kokku olete " + kokku + " aastat vanad."
if sobravanus < 18:
    print ("Sober on alaealine.")
    if sobravanus < 6:
        print ("oled koolieelik") 
elif(sobravanus > 40):
    print("Sober on vanur.")

    