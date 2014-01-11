## Maria Gaiduki näide
import pygame, sys
pygame.init()
from math import * 

#muutujad akna laiuse(w) ja kõrguse(h) hoidmiseks
w = 1000
h = 600

ekraan = pygame.display.set_mode([w,h])
pygame.display.set_caption("Animatsioon")
ekraan.fill([255,255,255])

x = 50
y = 50
animeeri = True
suund = 1             #kordaja, millele vastavalt, kas liidetakse või lahutatakse y-koordinaadist 5

while animeeri == True:
    pygame.time.delay(20)
    #kustutame eelneva objekti
    pygame.draw.circle(ekraan, [255, 255, 255],[x,y],50,0)

    if y >= h and suund == 1: #kontrollime koordinaate ja kas pall liigub alla
        suund = -1
    if y <= 0 and suund == -1:  #kontrollime koordinaate ja kas pall liigub üles
        suund = 1

    #arvutame uue y-koordinaadi
    y = y + 5*suund
    
    #joonistame
    pygame.draw.circle(ekraan, [0, 0, 0],[x,y],50,0)
    pygame.display.update()

    #kontrollime, kas katkestada animatsioon
    for j in pygame.event.get():
        if j.type == pygame.KEYDOWN:    #kas on vajutatud suvalist klahvi klaviatuuril
            animeeri = False
    

pygame.display.flip()

#kontrollime, kas vajutati
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit(0)
