linnad = ['Pariis','London', 'Madrid','Stockholm','Oslo','Bryssel']
teinelist = ["esimene","teine","kolmas"]
sorditud = linnad.sort()
print linnad
linnadearv = len(linnad)
print linnadearv
linnad.append("Tartu")
linnad.append("Paide")
linnad.sort()
linnadearv = len(linnad)
for i in range(linnadearv):
    print i+1,linnad[i]
print ("Meie loendis on " + str(linnadearv) + " linna.") 
