rea_nr = 7
read = []
f = open("luuletus.txt","r")
for rida in f:
	read.append(rida)
print read
print read[rea_nr - 1] 
f.close()
