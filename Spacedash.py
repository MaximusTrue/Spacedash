import pygame, sys
import random
from pygame.locals import *



def main():
    pygame.init()

    pygame.display.set_caption("Spacedash")

    DISPLAY=pygame.display.set_mode((1000,600),0,32)

    WHITE = (255,255,255)
    BLUE = (0,0,255)

    player = pygame.Vector2()
    player.xy = 200,200
    playerVel = 0.6
    playerAccel = 0.03

    groundHeight = DISPLAY.get_height() - DISPLAY.get_height() / 8
    
    MIN_AST_CLEARANCE = 80
    astClearance = 150

    ast = pygame.Vector2()

    ast.xy = DISPLAY.get_width(), random.randint(astClearance, int(groundHeight - astClearance))
    astVel = 1.5

    pointsScored = 0
    hasScored = False

    while True:

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

        DISPLAY.fill(WHITE)

        #Create random obstical BOTTOM
        if ast.x < -50:
            ast.y = random.randint(astClearance, int(groundHeight - astClearance))
            ast.x = DISPLAY.get_width()
            hasScored = False

        pygame.draw.rect(DISPLAY, "red", (ast.x, ast.y, 50, DISPLAY.get_height() - ast.y)) # Bottom
        pygame.draw.rect(DISPLAY, "red", (ast.x, 0, 50, ast.y - astClearance)) # Top

        ast.x = ast.x - astVel

        #Player
        pygame.draw.rect(DISPLAY, BLUE, (player.x, player.y, 50, 50))
        player.y = player.y + playerVel
        playerVel += playerAccel

        #Ground
        pygame.draw.rect(DISPLAY, "black", (0, groundHeight, DISPLAY.get_width(), 10))

        #Slide on ground
        if player.y + 50 > groundHeight:
            player.y = groundHeight - 50

        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            playerVel = 0.6
            player.y -= 3.5 #4
            
        
        if player.y < 0:
            player.y = 0

        if checkWallCollision(player.x, player.y, ast.x, ast.y, astClearance):
            print("Game Over")

        if player.x > ast.x + 50 and not hasScored:
            pointsScored += 1
            hasScored = True
            print("Points: " + str(pointsScored))


        pygame.draw.rect(DISPLAY, "white", (0, groundHeight + 10, DISPLAY.get_width(), DISPLAY.get_height() - groundHeight))
        pygame.display.update()
        pygame.time.delay(10)

def checkWallCollision(x1, y1, x2, y2, astClearance):
    return (x2 <= x1 + 50 and x1 <= x2 + 50) and (y1 + 50 >= y2 or y1 <= y2 - astClearance)

def checkCollision(x1, y1, width_1, height_1, x2, y2, width_2, height_2):
    return x1 + width_1 >= x2 and x1 <= x2 + width_2 and y1 + width_1 >= y2 and y1 <= y2 + height_2
    
main()