import pygame, sys
from pygame.locals import *
from math import pi



def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((500,400),0,32)

    WHITE = (255,255,255)
    BLUE = (0,0,255)

    y = 100
    x = 100
    velocity = 0
    acceleration = 0.1


    radius = 50
    # Just to place the circle in the center later on
    top_left_corner = (DISPLAY.get_width()/2 - radius/2, DISPLAY.get_height()/2 - radius/2)
    outer_rect = pygame.Rect(top_left_corner, (radius, radius))

    countdown = 10  # seconds
    angle_per_second = 2*pi / countdown
    angle = 0
    dt = 0  # dt is the time since the last clock.tick call in seconds.
    time = 0
    

    while True:

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            
        time += dt
        angle += angle_per_second * dt

        DISPLAY.fill(WHITE)
        # pygame.draw.rect(DISPLAY, BLUE, (x, y, 50, 50))
        # y = y - velocity
        # velocity += acceleration

        pygame.draw.arc(DISPLAY, "white", outer_rect, angle-0.2, angle, 10)

            
        pygame.display.update()
        pygame.time.delay(10)

main()