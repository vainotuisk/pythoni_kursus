import pygame,sys
x = y = 200

x1 = y1 = 0

e_laius = 640
e_korgus = 480
viivitus = 50
intervall = 20
pygame.init()
ekraan = pygame.display.set_mode([e_laius,e_korgus])
pygame.display.set_caption("Põrkav koer")
pilt = pygame.image.load("koer.png") #128x128
kass = pygame.image.load("kass.png") #128x128
samm = 5
pygame.key.set_repeat(viivitus,intervall)
while True:
    if abs(x - x1) <5 and abs(y - y1) < 5: # kui kattuvad osaliselt
        x = y = 200
        x1 = y1 = 0
    ekraan.fill([255, 255, 255])
    ekraan.blit(pilt, (x%e_laius,y%e_laius))
    ekraan.blit(kass, (x1%e_laius,y1%e_laius))
    pygame.display.flip()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        # Kui sündmuseks on klahvi allavajutamine...
        elif i.type == pygame.KEYDOWN: 
            # ... ja klahviks on nooleklahv üles liikumiseks,...
            if i.key == pygame.K_UP: 
                # ... siis vähendame y-koordinaati
                y = y - samm 
            elif i.key == pygame.K_DOWN:
                y = y + samm
            elif i.key == pygame.K_LEFT:
                x = x - samm
            elif i.key == pygame.K_RIGHT:
                x = x + samm
                # siit algab kassi liigutamine
            if i.key == pygame.K_w: 
                # ... siis vähendame y-koordinaati
                y1 = y1 - samm 
            elif i.key == pygame.K_z:
                y1 = y1 + samm
            elif i.key == pygame.K_a:
                x1 = x1 - samm
            elif i.key == pygame.K_s:
                x1 = x1 + samm    
while True:    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)
