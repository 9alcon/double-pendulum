from math import cos, pi, sin
import pygame
import time
import random


pygame.init()
height = 600
width = 1000
win = pygame.display.set_mode((width, height))
r1 = r2 = 175
m1 = m2 = 15
a1 = random.uniform(0, 2*pi)
a2 = random.uniform(0, 2*pi)
o = (width/2, 200)
a1v = 0
a2v = 0
g = 1
t = 0
trail_limit = 400

trail = list()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if len(trail) > len(trail):
        trail.pop(0)

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

    x1 = r1 * sin(a1) + width/2
    y1 = r1 * cos(a1) + o[1]
    x2 = x1 + r2 * sin(a2)
    y2 = y1 + r2 * cos(a2)

    a1v += a1a
    a2v += a2a
    a1 += a1v
    a2 += a2v

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
    t += 0.0250
