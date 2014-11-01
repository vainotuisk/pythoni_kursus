# -*- coding: utf-8 -*-
##Siinuse graafik
import pygame,sys
from math import *
e_laius = 640
e_korgus = 480
pygame.init()
must =[255,255,255]
ekraan = pygame.display.set_mode([e_laius,e_korgus])
pygame.display.set_caption("Sinusoid")

x=0
y=0
punktX =[]
punktY =[]


for i in range(e_laius):
    punktX.append(i)
    punktY.append(sin(i/10)*50+200)

for i in range(1,e_laius):
    pygame.draw.line(ekraan,must,[punktX[i-1],punktY[i-1]],[punktX[i],punktY[i]])

    pygame.display.flip()

while True:    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)
