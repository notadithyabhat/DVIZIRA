import pygame
from pygame.locals import *
import random 
from sys import exit

class point:
    
    def __init__(self,color,surface,x,y,radius = 0):
        self.color = color
        self.surface = surface
        self.pos = (x,y)
        self.radius = 7+radius

            
    
    def generate(self):
        return pygame.draw.circle(screen, self.color, self.pos, self.radius)

def boundaries():
   pygame.draw.rect(screen,(0,0,255),(0,0,640,480),2)    
   pygame.draw.line(screen, (0,0,255), [520, 80], [120, 80], 2)
   pygame.draw.line(screen, (0,0,255), [400, 400], [120, 400], 2)
   pygame.draw.line(screen, (0,0,255), [120, 400], [120, 80], 2)
   pygame.draw.line(screen, (0,0,255), [520, 400], [520, 80], 2)
  
pygame.init()
screen = pygame.display.set_mode((640,480),0,32)

clock = pygame.time.Clock()

green_no = int(input('Enter the number of green points: '))
red_no = int(input('Enter the number of red points: '))
fps = int(input('Enter the FPS: '))
radius = int(input('Enter the radius: '))

basic_data = (green_no,red_no,fps,radius)


data_file = open('Basic_file.txt','w+')
green_data = open('Green Data File.txt','w+')
red_data = open('Red Data File.txt','w+')

for each in basic_data:
    data_file.write(f'{each}\n')
data_file.close()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            green_data.close()
            red_data.close()
            exit()
    screen.fill((0, 0, 0))
    boundaries()
    for each in range(green_no):
        flag=0
        x,y = (random.randint(7+radius,633-radius),random.randint(7+radius,473-radius))
        while (x in range(111-radius,529+radius)) and (y in range(71-radius,409+radius)):
            x,y = (random.randint(7+radius,633-radius),random.randint(7+radius,473-radius))
        green = point((0,200,0),screen,x,y,radius)
        green_data.write(f'{x},{y}\n')
        
        
        green.generate()
    for each in range(red_no):
        x,y = (random.randint(127+radius,513-radius),random.randint(87+radius,393-radius))
        red = point((255,0,0),screen,x,y,radius)
        red_data.write(f'{x},{y}\n')
        red.generate()
    clock.tick(fps)
    pygame.display.update()
    
    