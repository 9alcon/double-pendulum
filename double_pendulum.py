from math import cos, pi, sin
import pygame
import time
import random


pygame.init()
height = 600
width = 1000
win = pygame.display.set_mode((width, height))
r1 = r2 = 175#length of the rod
m1 = m2 = 15#mass 1 and 2
a1 = random.uniform(0, 2*pi)
a2 = random.uniform(0, 2*pi)
#a1 and a2 are the angles of r1 and r2 respectively
o = (width/2, 200)#origin
a1v = 0
a2v = 0
#angular acceleration
g = 1#gravitational constant
trail_limit = 400 #the max points that should be in trail list

trail = list()

run = True
#run loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #pop the first element of the list to keep it small
    if len(trail) > len(trail):
        trail.pop(0)
    #math from https://www.myphysicslab.com/pendulum/double-pendulum-en.html
    num1 = -g * (2 * m1 + m2) * sin(a1)
    num2 = -m2 * g * sin(a1 - 2 * a2)
    num3 = -2 * sin(a1 - a2) * m2
    num4 = a2v * a2v * r2 + a1v * a1v * r1 * cos(a1 - a2)
    den = r1 * (2 * m1 + m2 - m2 * cos(2 * a1 - 2 * a2))
    a1a = (num1 + num2 + num3 * num4) / den

    num1 = 2 * sin(a1 - a2)
    num2 = (a1v * a1v * r1 * (m1 + m2))
    num3 = g * (m1 + m2) * cos(a1)
    num4 = a2v * a2v * r2 * m2 * cos(a1 - a2)
    den = r2 * (2 * m1 + m2 - m2 * cos(2 * a1 - 2 * a2))
    a2a = (num1 * (num2 + num3 + num4)) / den
    
    #updating the position based on the angle
    x1 = r1 * sin(a1) + width/2
    y1 = r1 * cos(a1) + o[1]
    x2 = x1 + r2 * sin(a2)
    y2 = y1 + r2 * cos(a2)
    #updating the velocity and position
    a1v += a1a
    a2v += a2a
    a1 += a1v
    a2 += a2v
    
    #drawing everything
    win.fill((255, 255, 255))
    trail.append((x2, y2))
    if len(trail) > 1:
        for i in range(0,len(trail)-1):
            pygame.draw.line(win, (100, 100, 100), trail[i], trail[i+1], 2)
    pygame.draw.line(win, (0, 0, 0), o, (x1, y1), 3)
    pygame.draw.circle(win, (0, 0, 0), (x1, y1), m1, 0)
    pygame.draw.line(win, (0, 0, 0), (x1, y1), (x2, y2), 3)
    pygame.draw.circle(win, (0, 0, 0), (x2, y2), m2, 0)
    pygame.display.update()
    time.sleep(0.0250)
    
