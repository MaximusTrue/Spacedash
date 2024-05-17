import pygame, sys
from pygame.locals import *



def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((1000, 600),0,32)

    WHITE = (255,255,255)
    BLUE = (0,0,255)
    
    #Ball Constants
    radius = 12
    velocity = pygame.Vector2()
    velocity.xy = 2.5, 2.5
    acceleration = 0.1
    clock = pygame.time.Clock()
    running = True
    dt = 0

    #Player Constants
    playerVel = pygame.Vector2()
    playerVel.xy = 0, 0
    
    ball_pos = pygame.Vector2(DISPLAY.get_width() / 2, DISPLAY.get_height() / 2)
    player_pos = pygame.Vector2(DISPLAY.get_width() / 8, DISPLAY.get_height() / 2)


    while True:

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

        # Background
        DISPLAY.fill("green")
        
        # Ball
        pygame.draw.circle(DISPLAY, "white", (ball_pos.x, ball_pos.y), radius)

        # Moving Ball
        ball_pos.x += velocity.x
        ball_pos.y += velocity.y

        if(ball_pos.x + radius > DISPLAY.get_width()):
            velocity.x = -2.5
        if(ball_pos.x - radius < 0):
            velocity.x = 2.5
        if(ball_pos.y + radius > DISPLAY.get_height()):
            velocity.y = -2.5
        if(ball_pos.y - radius < 0):
            velocity.y = 2.5

        # Player
        pygame.draw.rect(DISPLAY, "white", (player_pos.x, player_pos.y, 10, 50))

        # Move player up and down
        if keys[K_w]:
            player_pos.y -= 3
        if keys[K_s]:
            player_pos.y += 3
        
        # Player collision with walls 
        if player_pos.y < 0:
            player_pos.y = 0
        if player_pos.y + 50 > DISPLAY.get_height():
            player_pos.y = DISPLAY.get_height() - 50


        # Collision with player
        # TODO: If ball hits top/bottom of player, it will bounce of the top/bottom of the player continuning in the same direction
        if ball_pos.x - radius < player_pos.x + 10 and ball_pos.x - radius > player_pos.x and ball_pos.y + radius > player_pos.y and ball_pos.y - radius < player_pos.y + 50:
            velocity.x = 2.5
        # if ball_pos.x + radius < player_pos.x + 5 and ball_pos.y 

        # Scored
        if ball_pos.x - radius < 0:
            ball_pos.x = DISPLAY.get_width() / 2
            ball_pos.y = DISPLAY.get_height() / 2

        if keys[K_SPACE]:
            velocity.xy = -0.25, velocity.y * 0.1
        
        # Update the display    
        pygame.display.update()
        pygame.time.delay(10)

main()