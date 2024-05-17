import pygame, sys
from pygame.locals import *



def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((500,400),0,32)

    WHITE = (255,255,255)
    BLUE = (0,0,255)

    y = 100
    x = 100
    velocity = 0
    acceleration = 0.1

    

    while True:

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

            DISPLAY.fill(WHITE)
            pygame.draw.rect(DISPLAY, BLUE, (x, y, 50, 50))
            y = y - velocity
            velocity += acceleration

            
            pygame.display.update()
            pygame.time.delay(10)

main()