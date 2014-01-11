import pygame,sys
## 
pygame.init()
screen = pygame.display.set_mode([640,480])
loomapilt = pygame.image.load("koer.png") #128x128
while True :
    screen.fill([255,255,255])
    for i in range(1,5):
        screen.blit(loomapilt,(i*128-64,240-64))
##pygame.display.flip()

    pygame.display.flip()
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()


