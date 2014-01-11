##  Anneli Bent
##  Topelttsükkel:
##  "Koostada arvude 1 kuni 20 astmete (2 kuni 5) tabel."
##  Marika Anissimov, Urmas Palmaru, Väino Tuisk
print("Koostada arvude 1 kuni 20 astmete (2 kuni 5) tabel.")
print ("Arv\truut\tkuup\tneljas\tviies")
for i in range(1,21):
    print("\n"+str(i)+"\t"),
    for j in range(2,6):
        print(str(i**j)+"\t"),
