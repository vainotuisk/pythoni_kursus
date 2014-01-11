# Topelttsükkel      
# Väino Tuisk        
#

# Konstantidele väärtused
ridu = 20
kohti = 26

# Muutujatele algväärtused
minuRida = 0
minuKoht = 0

# Konsoolilt andmete sisestus koos kontrolliga
while minuRida < 1 or minuRida > ridu:
    minuRida = int(input("Mis rida (1-20)? "))
while minuKoht < 1 or minuKoht > kohti:
    minuKoht = int(input("Mis koht (1-26)? "))

# Maatriksi väljastamine konsoolile
# keskel vahekäik, otsitav koht märgistatud X-ga
for i in range(ridu):
    for j in range(kohti):
        if i == minuRida-1 and j == minuKoht-1:
            print (" X ", end = "")
        else:
            print (" o ", end = "")
        if (j == kohti/2):
                print ("  ", end = "")   
    print ("")
