#подключаем библиотеки
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

screen.fill((200, 200, 200))
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
    
def drawcat(x, y, size):
    '''
    this function draws cat    
    ''' 
    ellipse(screen, GREY, (x, y, 4*size, size)) #telo kota
    ellipse(screen, GREY, (x-size/10, y-size/2, 1.1*size, size/1.2)) #golova kota
    ellipse(screen, WHITE, (x-size/40, y-size/4, 0.36*size, 0.26*size)) #glaza kota
    ellipse(screen, WHITE, (x+size/2, y-size/4, 0.36*size, 0.26*size))
    ellipse(screen, BLACK, (x+size/10, y-size/5, 0.2*size, 0.1*size))
    ellipse(screen, BLACK, (x+size/1.55, y-size/5, 0.2*size, 0.1*size))
    arc(screen, BLACK, (x+size/4, y+size/15, size/2, size/2), -5.5, -4, 1) #rot kota
    surface = pygame.Surface((3*size,size)) #hvost
    surface.set_colorkey([0, 0, 0])
    ellipse(surface, GREY, (0, 0, 3*size, size/2))
    surface2 = pygame.transform.rotate(surface, 45)
    screen.blit(surface2, (x+size*3, y-1.5*size))  

    surface = pygame.Surface((3*size,size)) #1 noga
    surface.set_colorkey([0, 0, 0])
    ellipse(surface, GREY, (0, 0, 1.5*size, 0.4*size))
    surface3 = pygame.transform.rotate(surface, 40)
    screen.blit(surface3, (x-0.5*size, y-0.5*size))

    surface = pygame.Surface((3*size,size)) #2 noga
    surface.set_colorkey([0, 0, 0])
    ellipse(surface, GREY, (0, 0, 1.5*size, 0.4*size))
    surface3 = pygame.transform.rotate(surface, -30)
    screen.blit(surface3, (x+2.4*size, y+0.7*size))

    polygon(screen, GREY, [(x+0*size, y-0.3*size), (x-0*size, y-0.5*size), (x+0.1*size, y-0.4*size)]) #yshi
    polygon(screen, GREY, [(x+1*size, y-0.2*size), (x+0.9*size, y-0.5*size), (x+0.8*size, y-0.4*size)])

def drawigly(x, y, size):
    '''
    This function draw igly
    '''
    surface = pygame.Surface((3*size,size))
    surface.set_colorkey([0, 0, 0])
    ellipse(surface, YELLOW, (0, 0, 3*size, 7*size))
    screen.blit(surface, (x-0.5*size, y-1*size))
    for i in range (size//15):
        line(screen, RED, [x+5*i, (y-10*i)], [x-5*i+2*size, (y-10*i)], 2)
    rect(screen, BLACK, (x+0.75*size, y-0.92*size, 0.5*size, 0.3*size), 5)

#draw iglys
drawigly(100, 700, 100)
drawigly(250, 600, 300)
drawigly(600, 500, 200)
drawigly(0, 450, 250)

# draw eskimoses
drawEskimos(600, 850, 80, 150)
drawEskimos(800, 600, 170, 190)
drawEskimos(450, 700, 140, 100)
drawEskimos(300, 900, 30, 50)

#draw cats
drawcat(100, 800, 50)
drawcat(200, 600, 30)
drawcat(300, 500, 40)
drawcat(20, 550, 20)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()
