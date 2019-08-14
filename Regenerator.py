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



regen = input('Do you want to regenerarte the simulation?(Y/N)')
if regen.upper() == 'Y':
    pygame.init()
    screen = pygame.display.set_mode((640,480),0,32)

    clock = pygame.time.Clock()
    coordinates = []
    basic = open('Basic_file.txt','r')
    basic1 = basic.readlines()
    data = [int(each) for each in basic1]
    green_co = open('Green Data File.txt','r')
    green_co1 = green_co.readlines()
    for eachline in green_co1:
        x1 = eachline.split(',')
        x = [int(each) for each in x1]
        coordinates.append(x)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
       
        for each in range(data[0]):
            for x,y in coordinates:
                screen.fill((0, 0, 0))
                boundaries()
                green = point((0,200,0),screen,x,y,data[3])
                green.generate()
                green.generate1()
                clock.tick(data[2])
                pygame.display.update()
        
        
        
        