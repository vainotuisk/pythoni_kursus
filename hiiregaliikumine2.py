import pygame, sys
pygame.init()
ekraan = pygame.display.set_mode([800, 600])
ekraan.fill([255, 255, 255])
pilt = pygame.image.load("koer.png")
x = y = 0 # algsed koordinaadid
ekraan.blit(pilt, (x, y)) # Joonistame pildi koordinaatidega (x, y)
while True:
    ekraan.fill([255, 255, 255])
    ekraan.blit(pilt, (x,y))
    pygame.display.flip()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        # Kui sündmuseks on hiireklõps,...
        elif i.type == pygame.MOUSEBUTTONDOWN:
            # ... siis muudame pildi koordinaate sisaldavaid muutujaid x ja y 
            x, y = i.pos 
