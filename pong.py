import pygame, sys
from pygame.locals import *



def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((1000, 600),0,32)
    pygame.display.set_caption("Pong")

    WHITE = (255,255,255)
    BLUE = (0,0,255)
    
    #Ball Constants
    radius = 12
    velocity = pygame.Vector2()
    velocity.xy = 2.5, 2.5
    defaultBallVel = pygame.Vector2()
    defaultBallVel.xy = 2.5, 2.5

    acceleration = 0.1
    clock = pygame.time.Clock()
    running = True
    dt = 0
    ball_pos = pygame.Vector2(DISPLAY.get_width() / 2, DISPLAY.get_height() / 2)

    #Player One (left) Constants
    playerVel = pygame.Vector2()
    playerVel.xy = 0, 0
    player_pos = pygame.Vector2(DISPLAY.get_width() / 8, DISPLAY.get_height() / 2)
    playerOneScore = 0

    #Player two (right) Constants
    player2Vel = pygame.Vector2()
    player2Vel.xy = 0, 0
    player2_pos = pygame.Vector2(DISPLAY.get_width() - DISPLAY.get_width() / 8, DISPLAY.get_height() / 2)
    playerTwoScore = 0

    counter = 0
    myFont = pygame.font.Font(None, 74)

    while True:

        if(playerOneScore == 5):
            pass
        if(playerTwoScore == 5):
            pass

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

        #Speed up ball
        if(counter == 750):
            counter = 0
            defaultBallVel *= 1.2

        if(ball_pos.x + radius > DISPLAY.get_width()):
            velocity.x = -defaultBallVel.x
        if(ball_pos.x - radius < 0):
            velocity.x = defaultBallVel.x
        if(ball_pos.y + radius > DISPLAY.get_height()):
            velocity.y = -defaultBallVel.y
        if(ball_pos.y - radius < 0):
            velocity.y = defaultBallVel.y

        # Player One
        pygame.draw.rect(DISPLAY, "white", (player_pos.x, player_pos.y, 10, 50))

        #Player Two
        pygame.draw.rect(DISPLAY, "white", (player2_pos.x, player2_pos.y, 10, 50))

        # Move Player One
        if keys[K_w]:
            player_pos.y -= 3
        if keys[K_s]:
            player_pos.y += 3

        # Move Player Two
        if keys[K_i]:
            player2_pos.y -= 3
        if keys[K_k]:
            player2_pos.y += 3
        
        # Player collision with walls 
        if player_pos.y < 0:
            player_pos.y = 0
        if player_pos.y + 50 > DISPLAY.get_height():
            player_pos.y = DISPLAY.get_height() - 50
        
        # Player 2 collision with walls
        if player2_pos.y < 0:
            player2_pos.y = 0
        if player2_pos.y + 50 > DISPLAY.get_height():
            player2_pos.y = DISPLAY.get_height() - 50

        # Collision with player
        if ball_pos.x - radius < player_pos.x + 10 and ball_pos.x - radius > player_pos.x and ball_pos.y + radius > player_pos.y and ball_pos.y - radius < player_pos.y + 50:
            velocity.x = defaultBallVel.x
        
        # Collision with player 2
        if ball_pos.x + radius > player2_pos.x and ball_pos.x + radius < player2_pos.x + 10 and ball_pos.y + radius > player2_pos.y and ball_pos.y - radius < player2_pos.y + 50:
            velocity.x = -defaultBallVel.x
        
        # Score Reset
        #Player 2 Scores
        if ball_pos.x - radius < 0: 
            ball_pos.x = DISPLAY.get_width() / 2
            ball_pos.y = DISPLAY.get_height() / 2
            playerTwoScore += 1
            defaultBallVel.xy = 2.5, 2.5

        #Player 1 Scores
        if ball_pos.x + radius > DISPLAY.get_width(): 
            ball_pos.x = DISPLAY.get_width() / 2
            ball_pos.y = DISPLAY.get_height() / 2
            playerOneScore += 1
            defaultBallVel.xy = 2.5, 2.5
            
        score_text = myFont.render(f"{playerOneScore}       -       {playerTwoScore}", True, WHITE)

        DISPLAY.blit(score_text, (DISPLAY.get_width() / 2 - 125, DISPLAY.get_height() / 20))

        counter += 1
        
        # Update the display    
        pygame.display.update()
        pygame.time.delay(10)

    pygame.quit()

main()