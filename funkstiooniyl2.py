#coding=UTF-8
# yl lk http://www.progetiiger.ee/content/06-funktsioonid-e-alamprogrammid
linnad = ['Pariis','London', 'Madrid','Stockholm','Oslo','Brüssel']
def linnadefunk(linn):
	mitu = len(linn)
#	print mitu
#	print(linn)
	for i in range(mitu):
		print "Üks linnadest on " + linn[i]
linnadefunk(linnad)