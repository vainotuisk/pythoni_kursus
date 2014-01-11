import pygame, sys
pygame.init()
ekraan = pygame.display.set_mode([800, 600])
ekraan.fill([255, 255, 255])
pilt = pygame.image.load("koer.png")
pildisuurus = pilt.get_rect().size
x = y = 0 # algsed koordinaadid
ekraan.blit(pilt, (x, y)) # Joonistame pildi koordinaatidega (x, y)
while True:
    ekraan.fill([255, 255, 255])
    ekraan.blit(pilt, (x - pildisuurus[0]/2,y - pildisuurus[1]/2))
    pygame.display.flip()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        # Kui sündmuseks on hiire liikumine,...
        elif i.type == pygame.MOUSEMOTION:
            # ... siis muudame pildi koordinaate sisaldavaid muutujaid x ja y 
##            x+pildisuurus[0]/2, y+pildisuurus[1]/2 = i.pos 
            x, y = i.pos 
