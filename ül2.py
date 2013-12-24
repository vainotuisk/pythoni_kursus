# uus ülesanne piimapakist: 
#Küsib kui palju on raha? ja kui palju maksab ostetav asi,
#väljastab kas on piisavalt raha
kotis = int(input("Palju sul raha on? "))
asjahind = int(input("Palju see asi maksab? "))
print kotis,asjahind
   if kotis > asjahind:
       print("Osta!")
    else:
        print("Sul pole piisavalt raha!")
