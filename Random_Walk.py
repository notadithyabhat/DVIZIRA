import pygame
from pygame.locals import*
from sys import exit

class point:
    
    def __init__(self,screen,color):
        self.screen = screen
        self.color = color
        
    def generate(self,x,y):
        return pygame.draw.circle(self.screen,self.color,(x,y),2)
    
    #def generate(self,x,y,radius):
        #return pygame.draw.circle(self.screen,self.color,x,y,2+radius,1)
    
    def move(self,x,y,x2,y2):
            speed_x,speed_y = direction(x,y,x2,y2)
            return x+speed_x,y+speed_y
    
    #def move(self,x,y,x2,y2):
            #speed_x,speed_y = direction(x,y,x2,y2)
            #return pygame.draw.circle(self.screen,self.color,x+speed_x,x+speed_y,2+radius,1) 

import random

def direction(x1,y1,x2,y2):
    N=(0,-1)
    NE=(1,-1)
    E=(1,0)
    SE=(1,1)
    S=(0,1)
    SW=(-1,1)
    W=(-1,0)
    NW=(-1,-1)

    if x2>x1 and y1>y2:                                                              #Destination towards north east
        direction =  random.choice([N,N,N,NE,NE,NE,E,E,E,SE,SE,S,SW,W,NW,NW])
        return direction
    if x2>x1 and y2>y1:                                                              #Destination towards south east
        direction =  random.choice([N,NE,NE,E,E,E,SE,SE,SE,S,S,S,SW,SW,W,NW])
        return direction
    if x1>x2 and y1>y2:                                                              #Destination towards north west
        direction =  random.choice([N,N,N,NE,NE,E,SE,S,SW,SW,W,W,W,NW,NW,NW])
        return direction
    if x1>x2 and y2>y1:                                                              #Destination towards south west
        direction =  random.choice([N,NE,E,SE,SE,S,S,S,SW,SW,SW,W,W,W,NW,NW])
        return direction
    elif y1>y2:                                                                      #Destination towards north
        direction =  random.choice([N,N,N,NE,NE,NE,E,E,SE,S,SW,W,W,NW,NW,NW])
        return direction
    elif y2>y1:                                                                      #Destination towards south
        direction =  random.choice([N,NE,E,E,SE,SE,SE,S,S,S,SW,SW,SW,W,W,NW])
        return direction
    elif x2>x1:                                                                      #Destination towards east 
        direction =  random.choice([N,N,NE,NE,NE,E,E,E,SE,SE,SE,S,S,SW,W,NW])
        return direction
    elif x1>x2:                                                                      #Destination towards west
        direction =  random.choice([N,N,NE,E,SE,S,S,SW,SW,SW,W,W,W,NW,NW,NW])
        return direction

pygame.init()
screen = pygame.display.set_mode((700,700),0,32)

clock = pygame.time.Clock()
GREEN = (0,200,0)
RED = (255,0,0)

green_coordinates = []

green_no = 2
fps = 100
radius = 0
i=0

green = []

for each in range(0,green_no):
    green.append(point(screen,GREEN))
                 
for each in green:
    x,y = random.randint(0,700),random.randint(0,700)
    green_coordinates.append([x,y])
    each.generate(x,y)
print(green_coordinates)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            green_data.close()
            red_data.close()
            exit()
    screen.fill((0, 0, 0))
    green_coordinates[0]=green[0].move(green_coordinates[0][0],green_coordinates[0][1],0,0)
    green[1].generate(green_coordinates[0][0],green_coordinates[0][1])
    green_coordinates[1]=green[1].move(green_coordinates[1][0],green_coordinates[1][1],0,0)
    green[1].generate(green_coordinates[1][0],green_coordinates[1][1])
    clock.tick(fps)
    pygame.display.update()
                 
    
        