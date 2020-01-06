#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 17:33:56 2020

@author: jav
"""

import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

print('[1] Inicio del programa')
run = True

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= vel
        print('Press LEFT')
        
    if keys[pygame.K_RIGHT]:
        x += vel
        print('Press RIGHT')
        
    if keys[pygame.K_UP]:
        y -= vel
        print('Press UP')
        
    if keys[pygame.K_DOWN]:
        y += vel
        print('Press DOWN')
        
    win.fill((0,0,0))    
    pygame.draw.rect(win, (255,0,0), (x,y,width,height))
    pygame.display.update()

print('[2] Saliendo del programa')
pygame.quit()
