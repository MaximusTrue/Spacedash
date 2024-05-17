import pygame, sys
from pygame.locals import *



def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((500,400),0,32)

    WHITE = (255,255,255)
    BLUE = (0,0,255)
    
    radius = 15
    velocity = pygame.Vector2()
    velocity.xy = 2.5, 2.5
    acceleration = 0.1
    clock = pygame.time.Clock()
    running = True
    dt = 0
    jump = False
    
    player_pos = pygame.Vector2(DISPLAY.get_width() / 2, DISPLAY.get_height() / 2)


    while True:

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    jump = True

        DISPLAY.fill("green")
        pygame.draw.circle(DISPLAY, "white", (player_pos.x, player_pos.y), radius)

        player_pos.x += velocity.x
        player_pos.y += velocity.y

        if(player_pos.x + radius > DISPLAY.get_width()):
            velocity.x *= -1
        if(player_pos.x - radius < 0):
            velocity.x *= -1
        if(player_pos.y + radius > DISPLAY.get_height()):
            velocity.y *= -1
        if(player_pos.y - radius < 0):
            velocity.y *= -1

        # Now can't hold space to jump, have to press it each time
        if(jump):
            velocity.y = -3
            jump = False

            
        pygame.display.update()
        pygame.time.delay(10)

main()