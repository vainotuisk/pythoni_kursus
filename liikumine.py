import pygame,sys
## drupal
pygame.init()
ekraan = pygame.display.set_mode([640,480])
pygame.display.set_caption("Koerakari")
pilt= pygame.image.load("koer.png") #128x128
ildisuurus = pilt.get_rect().size
x=0
y=0
for i in range (74):
    ekraan.fill([255,255,255])
    pygame.time.delay(20)
##    pygame.draw.rect(ekraan, [0, 0, 0], [x, y, 50, 50], 0) 
    y = y + 5    
    ekraan.blit(pilt, (x, y))
    pygame.display.flip()

while True:    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)


