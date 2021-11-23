# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 13:07:26 2021

@author: jp
"""

import pygame

pygame.init()

screen = pygame.display.set_mode((400, 600))

paddle1=pygame.Rect(100,100,50,10)
paddle2=pygame.Rect(300,500,50,10)


while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.draw.rect(screen,(100,100,100),paddle1)
    pygame.draw.rect(screen,(100,100,100),paddle2)
    
    pygame.display.update()