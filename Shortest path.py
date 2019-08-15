def shortest_path(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    if dx>0:
        x1+=1
    if dx<0:
        x1-=1
    if dy>0:
        y1+=1
    if dy<0:
        y1-=1
    return x1,y1
import pygame
from pygame.locals import *
import random 
from sys import exit

class point:
    
    def __init__(self,color,surface,x,y,radius = 0):
        self.color = color
        self.surface = surface
        self.pos = (x,y)
        self.radius = 7
        self.radius1 = 7+radius

            
    
    def generate(self):
        return pygame.draw.circle(screen, self.color, self.pos, self.radius)

    def generate1(self):
        return pygame.draw.circle(screen, self.color, self.pos, self.radius1,1)

def boundaries():
    pygame.draw.rect(screen,(0,0,255),(0,0,640,480),2)    
    pygame.draw.line(screen, (0,0,255), [520, 80], [120, 80], 2)
    pygame.draw.line(screen, (0,0,255), [400, 400], [120, 400], 2)
    pygame.draw.line(screen, (0,0,255), [120, 400], [120, 80], 2)
    pygame.draw.line(screen, (0,0,255), [520, 400], [520, 80], 2)
    
pygame.init()
screen = pygame.display.set_mode((640,480),0,32)

clock = pygame.time.Clock()

fps = (int(input('Enter the FPS:')))
radius = 0

gx,gy = random.randint(7+radius,633-radius),random.randint(7+radius,473-radius)
while (gx in range(111-radius,529+radius)) and (gy in range(71-radius,409+radius)):
    gx,gy = (random.randint(7+radius,633-radius),random.randint(7+radius,473-radius))

rx,ry = (random.randint(127+radius,513-radius),random.randint(87+radius,393-radius))

for x in range(400,520):
    if abs(x-gx) == min([abs(gx-each) for each in range(400,520)]):
        dest = x
print(dest)

flag = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.fill((0,0,0))
    boundaries()
    green = point((0,200,0),screen,gx,gy,radius)
    green.generate()
    red = point((255,0,0),screen,rx,ry,radius)
    red.generate()
    if gx==dest and gy==400:
        flag=1
    if flag==0:
        gx,gy = shortest_path(gx,gy,dest,400)
    else:
        gx,gy = shortest_path(gx,gy,rx,ry)
    clock.tick(fps)
    pygame.display.update()