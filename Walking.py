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
        return pygame.draw.circle(screen, self.color, self.pos, self.radius1,2)


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

gx,gy = random.randint(7+radius,633-radius),random.randint(7+radius,473-radius)
while (gx in range(111-radius,529+radius)) and (gy in range(71-radius,409+radius)):
    gx,gy = (random.randint(7+radius,633-radius),random.randint(7+radius,473-radius))

rx,ry = (random.randint(127+radius,513-radius),random.randint(87+radius,393-radius))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            green_data.close()
            red_data.close()
            exit()
    screen.fill((0, 0, 0))
    boundaries()
    print('reached')
    gx,gy = gx+random.randint(-7,7),gy+random.randint(-7,7)
    while ((gx not in range (7+radius,633-radius)) or (gy not in range(7+radius,473-radius))) or ((gx in range(111-radius,529+radius)) and (gy in range(71-radius,409+radius))):
        gx,gy = gx+random.randint(-7,7),gy+random.randint(-7,7)
    green = point((0,200,0),screen,gx,gy,radius)
    green.generate()
    green.generate1()
    green_data.write(f'{gx},{gy}\n')
    print('reached 2')
    rx,ry = rx+random.randint(-7,7),ry+random.randint(-7,7)
    while (rx not in range(127+radius,513-radius)) or (ry not in range(87+radius,393-radius)):
        rx,ry = rx+random.randint(-7,7),ry+random.randint(-7,7)
    print('reached 3')
    red = point((255,0,0),screen,rx,ry,radius)
    red_data.write(f'{rx},{ry}\n')
    red.generate()
    red.generate1()
    clock.tick(fps)
    pygame.display.update()