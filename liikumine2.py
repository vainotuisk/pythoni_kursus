import pygame,sys
## 
pygame.init()
ekraan = pygame.display.set_mode([640,480])
pygame.display.set_caption("Koerakari")
pilt= pygame.image.load("koer.png") #128x128
pilt2= pygame.image.load("koer.png") #128x128

pildisuurus = pilt.get_rect().size
x=x1=0
y=0
for i in range (74):
    ekraan.fill([255,255,255])
    pygame.time.delay(20)
    y = y + 5
    x1 = x1 + (572-pildisuurus[0])/76
    ekraan.blit(pilt, (x, y))
    ekraan.blit(pilt2,(x1+pildisuurus[0],y))
    pygame.display.flip()

while True:    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)


