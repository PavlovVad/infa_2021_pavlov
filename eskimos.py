import pygame
from pygame.draw import *

# In[71]:
'''
#smile

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
WHITE=(255, 255, 255)
GREY=(128, 128, 128)
screen.fill(GREY)
YELLOW=(255, 255, 0)
BLACK=(0, 0, 0)
RED=(255, 0, 0)

circle(screen, YELLOW, (200, 200), 150)
circle(screen, RED, (270, 150), 26)
circle(screen, RED, (130, 150), 22)

circle(screen, BLACK, (270, 150), 10)
circle(screen, BLACK, (130, 150), 10)

polygon(screen, BLACK, [(50,70), (150,120),
                               (150,140), (50,90)])

polygon(screen, BLACK, [(250,140), (250,120),
                               (320,60), (320,80)])

rect(screen, BLACK, (150, 280, 100, 20))




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

'''
# In[28]:


import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 1000))
WHITE=(255, 255, 255)
GREY=(200, 200, 200)
screen.fill(GREY)
YELLOW=(255, 255, 0)
BLACK=(0, 0, 0)
RED=(255, 0, 0)
BROWN=(128, 128, 0)

rect(screen, WHITE, (0, 450, 1000, 750))

ellipse(screen, BROWN, (580, 850, 50, 80)) #Nogi
ellipse(screen, BROWN, (650, 850, 50, 80))

ellipse(screen, BROWN, (560, 905, 60, 30))
ellipse(screen, BROWN, (650, 900, 60, 30))

arc(screen, BLACK, (80, 400, 400, 340), 0, 3.14, 2) #igly

arc(screen, BROWN, (550, 700, 170, 320), 0, 3.14, 85)#Eskimos

ellipse(screen, (220, 220, 220), (560, 600, 160, 150)) #Golova

ellipse(screen, BROWN, (510, 750, 80, 30)) #ryki
ellipse(screen, BROWN, (680, 750, 80, 30))


#kot
ellipse(screen, GREY, (200, 800, 160, 40)) #telo kota
ellipse(screen, GREY, (195, 775, 50, 40)) #golova kota


#rotate ellipse

surface = pygame.Surface((800,1000))
surface.set_colorkey([0, 0, 0])

ellipse(surface, GREY, (60, 390, 120, 25))

surface2 = pygame.transform.rotate(surface, 45)

screen.blit(surface2, (10, 10))

# glaza kota
ellipse(screen, WHITE, (200, 790, 15, 10))
ellipse(screen, WHITE, (220, 790, 15, 10))

ellipse(screen, BLACK, (205, 790, 10, 5))
ellipse(screen, BLACK, (225, 790, 10, 5))

arc(screen, BLACK, (210, 805, 20, 30), -5.5, -4, 1) #rot kota

circle(screen, (150, 150, 150), (636, 675), 60)
ellipse(screen, (225, 225, 225), (595, 650, 80, 70))
line(screen, BLACK, [600, 680], [620, 690])
line(screen, BLACK, [670, 680], [640, 690])
arc(screen, BLACK, (620, 700, 30, 40), -6, -3.5, 1)

line(screen, BLACK, [520, 670], [520, 920]) # palka




rect(screen, (101, 67, 33), (550, 850, 170, 40)) #Odejda

rect(screen, (101, 67, 33), (625, 750, 20, 100)) 






pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()

