import pygame, sys
pygame.init()
print "==== pygame moodul: ======="
ekraan = pygame.display.set_mode([800, 600])
# Aknasse "ekraan" joonistatud roheline ristkülik asukohaga x = 50, y = 50, 
# laiusega 150, kõrgusega 80, kontuuriga 0 (e. seest üleni täidetud)
pygame.draw.rect(ekraan, [0, 225, 0], [150, 150, 350, 350], 0)
# Lilla joon punktide (50, 150) ja (300, 200) vahel laiusega 2
pygame.draw.line(ekraan, [255, 0, 204], [50, 150], [300, 200], 2)
# Punane ring asukohaga x = 250, y = 190, raadiusega 45, kontuuriga 4 (seest tühi)
pygame.draw.circle(ekraan, [255, 0, 0], [250, 90], 25, 4)
pygame.display.flip()
while True:
   for i in pygame.event.get():
       if i.type == pygame.QUIT:
           sys.exit()
           
