import pygame,sys
##
e_laius = 640
e_korgus = 480
pygame.init()
ekraan = pygame.display.set_mode([e_laius,e_korgus])
pygame.display.set_caption("Põrkav koer")
pilt= pygame.image.load("koer.png") #128x128

pildisuurus = pilt.get_rect().size
x=0
y=0
konst = -5
for j in range(7):
    konst = - konst
    for i in range (74):
        
            ekraan.fill([255,255,255])
            pygame.time.delay(20)
            y = y + konst
            ekraan.blit(pilt, (x, y))
            pygame.display.flip()

while True:    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)


