#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                circle(screen, RED, event.pos, 50)
                pygame.display.update()
            elif event.button == 3:
                circle(screen,  BLUE, event.pos, 50)
                pygame.display.update()

pygame.quit()


# In[51]:


import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

expa = 0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    '''рисует новый шарик '''
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def click(event):
    '''delete ball if click on ball'''
    global expa
    print(x, y, r) #coordinate of new ball
    print(event.pos)
    eventx = event.pos[0]
    eventy = event.pos[1]
    print('текущий счет:', expa)
    if (eventx-x)**2 + (eventy-y)**2 <= r**2:
        expa = expa + 1 
        screen.fill(BLACK)
        
        
    
    
    
    

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                circle(screen, RED, event.pos, randint(10, 40))
                pygame.display.update()
                print('coordinate of new ball,', 'coordinate of click')
                click(event)
            elif event.button == 3:
                circle(screen,  BLUE, event.pos, randint(5, 25))
                pygame.display.update()
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()


# In[86]:


import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 4
screen = pygame.display.set_mode((1200, 900))

A=[0, 0, 0] #массив хранящий координаты шариков и их радиус
B=[]
for i in range (50):
    B.append(A)
expa = 0
k = 0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    '''рисует новый шарик '''
    global x, y, r, k
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    B[k] = [x, y, r]
    k = k + 1



    

def click(event):
    '''delete ball if click on ball'''
    global expa   
    eventx = event.pos[0]
    eventy = event.pos[1]
    for A in B:       
        if (eventx-A[0])**2 + (eventy-A[1])**2 <= A[2]**2:
            expa = expa + 1 
            circle(screen, BLACK, (A[0], A[1]), A[2])
    print('текущий счет:', expa)    
     
        
        
    
    
    
    

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    
    
    for A in B:
        A[0] = A[0] + 1
        A[1] = A[1] + 1
        print(B)
        circle(screen, RED, (A[0], A[1]), A[2])
    pygame.display.update()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                
                
                pygame.display.update()
                
                click(event)
            elif event.button == 3:
                circle(screen,  BLUE, event.pos, randint(5, 25))
                pygame.display.update()

    
            
        
        
    new_ball()
    pygame.display.update()
    '''screen.fill(BLACK)'''

pygame.quit()


# In[137]:


import pygame
import numpy as np
from pygame.draw import *
from random import randint
pygame.init()

FPS = 240
screen = pygame.display.set_mode((1200, 900))
 #массив хранящий координаты шариков и их радиус
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

x = randint(100, 1100)
y = randint(100, 900)
r = randint(10, 100)
a = randint(0, 360)
color = COLORS[randint(0, 5)]
circle(screen, color, (x, y), r)

A=[x, y, r]




    

     
        
        
    
    
    
    

pygame.display.update()
clock = pygame.time.Clock()
finished = False

n = 0
k = 0

while not finished:
    circle(screen, BLACK, (A[0], A[1]), r)
    clock.tick(FPS)
    if (0 <= A[0] <= 1200) and (0 <= A[1] <= 900):
        k += 0
    else:
        if n == 0:
            n = 1
        else:
            n = 0
    if n == 0:
        A[0] += int(2*np.cos(a))
        A[1] += int(2*np.sin(a))
    else:
        A[0] -= int(2*np.cos(a))
        A[1] -= int(2*np.sin(a))
    
    
    circle(screen, color, (A[0], A[1]), r)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                
                
                pygame.display.update()
                
                click(event)
            elif event.button == 3:
                circle(screen,  BLUE, event.pos, randint(5, 25))
                pygame.display.update()

    pygame.display.update()
    '''screen.fill(BLACK)'''

pygame.quit()


# In[ ]:





# In[ ]:




