#coding=UTF-8
#Funtksioon teisendab sendid tollideks
def sendid_tollideks(sendid):
	print (str(sendid) + " sentimeetrit on "+str(round(sendid/2.54,2)) + " tolli.")
sendid_tollideks(254)
sendid_tollideks(12.5)