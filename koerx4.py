import pygame,sys
## 
pygame.init()
screen = pygame.display.set_mode([640,480])
pygame.display.set_caption("Koerakari")
loomapilt = pygame.image.load("koer.png") #128x128
teksti_font = pygame.font.Font(None, 20)
allkirjad= ["Pontu","Muki","Kolla","Pitsu"]

pildisuurus = loomapilt.get_rect().size
print pildisuurus
def joonista(pilt,tekst, asukoht):
    screen.blit(pilt,(asukoht[0],asukoht[1]))
    tekst_pildina = teksti_font.render(tekst, 1, [0, 0, 200])
    screen.blit(tekst_pildina, [asukoht[0]+pildisuurus[0]/2-12, asukoht[1]+pildisuurus[0]])
while True :
    screen.fill([255,255,255])
    for i in range(4):
        for j in range(5):
##        screen.blit(loomapilt,(i*128-64,240-64))
##        tekst_pildina = teksti_font.render(allkirjad[i-1], 1, [0, 0, 200])
##        screen.blit(tekst_pildina, [i*128-10, 300])
            joonista(loomapilt,allkirjad[i-1],(i*pildisuurus[0],j*pildisuurus[1]))
    pygame.display.flip()
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)


