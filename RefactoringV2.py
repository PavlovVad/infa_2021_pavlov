import pygame
from pygame.draw import *


pygame.init()


FPS = 30
screen = pygame.display.set_mode((1000, 1000))


WHITE=(255, 255, 255)
GREY=(200, 200, 200)
YELLOW=(255, 255, 0)
BLACK=(0, 0, 0)
RED=(255, 0, 0)
GREEN=(128, 128, 0)
BROWN=(101, 67, 33)
LIGHTGREY=(220, 220, 220)
DARKGREY=(150, 150, 150)

screen.fill(GREY)


rect(screen, WHITE, (0, 450, 1000, 750))


def drawEskimos(x, y, width, height):
    """
    This function draws eskimos in clothes holding a stick whose center is in point (x, y)
    Whose height is counted from the bottom of the body to the top
    and whose width is counted from the left end of the body to its right end
    """
    ellipse(screen, GREEN, (x - width/2, y - height/2, width, 2*height))
    rect(screen, WHITE, (x - width/2, y + height/2, width, 2*height))
    ellipse(screen, GREEN, (x - width/3, y + 2*height/3, width/4, height/2))
    ellipse(screen, GREEN, (x + width/6, y + 2*height/3, width/4, height/2))
    ellipse(screen, GREEN, (x - width/2, y +  25*height/24, width/3, height/6))
    ellipse(screen, GREEN, (x + width/4, y +  25*height/24, width/3, height/6))
    rect(screen, BROWN, (x - width/2, y + height/2, width, height/3))
    rect(screen, BROWN, (x - width/12, y - height/2, width/6, height))
    ellipse(screen, LIGHTGREY, (x - 5*width/12, y - 11*height/12, 5*width/6, 2*height/3))
    circle(screen, DARKGREY, (x, y - 7*height/12), width/3)
    ellipse(screen, LIGHTGREY, (x - width/4, y - 5*height/6, width/2, height/2))
    line(screen, BLACK, [x - width/5, y - 2*height/3], [x - width/12, y - 7*height/12])
    line(screen, BLACK, [x + width/5, y - 2*height/3], [x + width/12, y - 7*height/12])
    lines(screen, BLACK, False, [(x - width/6, y - height/2), (x - width/12, y - 13*height/24), (x + width/12, y - 13*height/24), (x + width/6, y - height/2)])
    ellipse(screen, GREEN, (x - 3*width/4, y - height/6, 2*width/3, height/3))
    ellipse(screen, GREEN, (x + width/12, y - height/6, 2*width/3, height/3))
    line(screen, BLACK, [x - 2*width/3, y - 11*height/12], [x - 2*width/3, y + 7*height/6])
    
    
    
drawEskimos(800, 600, 170, 190)




#kot
ellipse(screen, GREY, (200, 800, 160, 40)) #telo kota
ellipse(screen, GREY, (195, 775, 50, 40)) #golova kota

# glaza kota
ellipse(screen, WHITE, (200, 790, 15, 10))
ellipse(screen, WHITE, (220, 790, 15, 10))

ellipse(screen, BLACK, (205, 790, 10, 5))
ellipse(screen, BLACK, (225, 790, 10, 5))

arc(screen, BLACK, (210, 805, 20, 30), -5.5, -4, 1) #rot kota

#rotate ellipse

surface = pygame.Surface((800,1000))
surface.set_colorkey([0, 0, 0])

ellipse(surface, GREY, (60, 390, 120, 25))

surface2 = pygame.transform.rotate(surface, 45)

screen.blit(surface2, (10, 10))



arc(screen, BLACK, (80, 400, 400, 340), 0, 3.14, 2) #igly


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()
