import pygame, sys
import random
from pygame.locals import *

def main():

    defaultPlayerVel = 0.3 #0.6
    gameVel = 3 #1.5
    
    pygame.init()
    myFont = pygame.font.Font(None, 200)
    myFontRest = pygame.font.Font(None, 72)
    myFontSmall = pygame.font.Font(None, 40)

    pygame.display.set_caption("Spacedash")

    DISPLAY=pygame.display.set_mode((1000,600),0,32)

    WHITE = (255,255,255)
    BLUE = (0,0,255)

    player = pygame.Vector2()
    player.xy = 200,200
    playerVel = defaultPlayerVel
    playerAccel = 0.08 #0.03

    groundHeight = DISPLAY.get_height() - DISPLAY.get_height() / 8
    
    MIN_WALL_CLEARANCE = 80
    wallClearance = 150

    wall = pygame.Vector2()

    wall.xy = DISPLAY.get_width(), random.randint(75+wallClearance, int(groundHeight - 75))

    pointsScored = 0
    hasScored = False

    collectable = pygame.Vector2()
    collectable.xy = random.randint(DISPLAY.get_width(), DISPLAY.get_width() + int(DISPLAY.get_width() / 2) ), random.randint(15, int(groundHeight - 15))
    collectableScore = 0

    dead = False

    invincible = False
    invincibleTimer = 0
    invincibleTimeout = 0

    inverse = False
    blackholeTimer = 0

    #Black Hole
    blackhole = pygame.Vector2()
    blackhole.xy = 100000, 0
    inBlackHole = False
    blackholePosOffScore = random.randint(7, 7) + pointsScored

    

    while True:
        DISPLAY.fill(WHITE)

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            #Test Inverse
            if event.type == pygame.KEYDOWN and event.key==K_UP:
                inverse = True
            #Invincible
            if event.type == pygame.KEYDOWN and event.key==K_RETURN and collectableScore - 5 >= 0:
                invincible = True
                collectableScore -= 5
                invincibleTimeout += 500
            #Slow Down
            if event.type == pygame.KEYDOWN and event.key == K_RSHIFT and collectableScore - 5>= 0:
                gameVel = gameVel * .75
                collectableScore -= 5

        #Black Hole
        if checkCollision(player.x, player.y, 50, blackhole.x + 50, blackhole.y, 50, DISPLAY.get_height()) and not inBlackHole:
            inBlackHole = True
            inverse = not inverse
            blackholePosOffScore = random.randint(7, 10) + pointsScored

        if inBlackHole:
            blackholeTimer += 1

        #Stop Inverse Time
        if blackholeTimer == 200:
            blackholeTimer = 0
            inBlackHole = False

        #Reset Wall
        if wall.x < -50:
            wall.y = random.randint(75+wallClearance, int(groundHeight - 75)) # - wallClearance
            wall.x = DISPLAY.get_width()
            hasScored = False
            if blackholePosOffScore - 1 == pointsScored:
                blackhole.x = wall.x

        DISPLAY.blit(pygame.image.load('fx/gfx/BlackholeResize.png'), (blackhole.x, wall.y - wallClearance))
        
        #Create random obstical
        pygame.draw.rect(DISPLAY, "red", (wall.x, wall.y, 50, DISPLAY.get_height())) # Bottom
        pygame.draw.rect(DISPLAY, "red", (wall.x, 0, 50, wall.y - wallClearance)) # Top
        
        blackhole.x = blackhole.x - gameVel

        wall.x = wall.x - gameVel

        #Player Gravity
        player.y = player.y + playerVel

        #Ground
        pygame.draw.rect(DISPLAY, "black", (0, groundHeight, DISPLAY.get_width(), 10))

        #Slide on ground
        if player.y + 50 > groundHeight:
            player.y = groundHeight - 50
        
        #Slide on Ceiling
        if player.y < 0:
            player.y = 0
        
        if not inverse:
            playerVel += playerAccel
            DISPLAY.blit(pygame.image.load('fx/gfx/UFO1.png'), (player.x - 40, player.y - 25))
        else:
            playerVel -= playerAccel
            DISPLAY.blit(pygame.transform.flip(pygame.image.load('fx/gfx/UFO1.png'), False, True), (player.x - 40, player.y - 25))

        keys = pygame.key.get_pressed()

        #Flying
        if keys[K_SPACE]and not dead and not inverse:
            playerVel = defaultPlayerVel
            player.y -= 4 #3.5 #4
        elif keys[K_SPACE] and not dead:
            playerVel = -defaultPlayerVel
            player.y += 4 
        
        #Die
        if checkWallCollision(player.x, player.y, wall.x, wall.y, wallClearance) and not invincible:
            gameVel = 0
            playerVel = 0
            dead = True
            resetText = myFontRest.render("Press P to Reset", True, "black")
            DISPLAY.blit(resetText, (DISPLAY.get_width() / 2 - 150, DISPLAY.get_height() / 2))
        
        #Reset
        if dead and keys[K_p]:
            gameVel = 3 #1.5
            playerVel = defaultPlayerVel
            player.xy = 200,200
            wall.xy = DISPLAY.get_width(), random.randint(75+wallClearance, int(groundHeight - 75))
            pointsScored = 0
            hasScored = False
            dead = False
            collectable.xy = random.randint(DISPLAY.get_width(), DISPLAY.get_width() + int(DISPLAY.get_width() / 2) ), random.randint(22, int(groundHeight - 22))
            collectableScore = 0
            inverse = False
            blackhole.xy = 1000000, 0
            inBlackHole = False
            blackholePosOffScore = random.randint(7, 10) + pointsScored
            blackholeTimer = 0

        #Score Points
        if player.x > wall.x + 50 and not hasScored:
            pointsScored += 1
            hasScored = True
            gameVel += 3*0.1

        #Collectable
        DISPLAY.blit(pygame.image.load('fx/gfx/PowerCellResize.png'), (collectable.x, collectable.y))
        collectable.x -= gameVel

        #Respawn Collectable if not Collected
        if(collectable.x < 0):
            collectable.xy = random.randint(DISPLAY.get_width(), DISPLAY.get_width() + int(DISPLAY.get_width() / 2) ), random.randint(15, int(groundHeight - 15))
        
        #Collecting Collectable
        if checkCollision(player.x, player.y, 50, collectable.x, collectable.y, 13, 22):
            collectableScore = collectableScore + 1
            collectable.x = random.randint(DISPLAY.get_width(), DISPLAY.get_width() + int(DISPLAY.get_width() / 2))
            collectable.y = random.randint(15, int(groundHeight - 15))
        
        #Making Sure Collectable isn't in a Wall
        if checkWallCollision(collectable.x, collectable.y, wall.x, wall.y, wallClearance):
            collectable.x = collectable.x - 100
        
        #Score Display
        scoreText = myFont.render(str(pointsScored), True, "grey")
        DISPLAY.blit(scoreText, (DISPLAY.get_width() / 2 - 50, 0))

        #Collectable Counter Display
        DISPLAY.blit(pygame.image.load('fx/gfx/PowerCellResize.png'), (5, 5))
        DISPLAY.blit(pygame.image.load('fx/gfx/TimesResize.png'), (23, 9))
        collectableText = myFontSmall.render(str(collectableScore), True, "black")
        DISPLAY.blit(collectableText, (50,5))

        if invincible:
            invincibleTimer += 1
            print(invincibleTimer)

        if invincibleTimer == invincibleTimeout:
            invincible = False
            invincibleTimer = 0
            invincibleTimeout = 0
        
        if not dead:
            if gameVel < 3:
                gameVel = 3
            if gameVel > 11:
                gameVel = 11
            
        

        pygame.draw.rect(DISPLAY, "white", (0, groundHeight + 10, DISPLAY.get_width(), DISPLAY.get_height() - groundHeight))
        pygame.display.update()
        pygame.time.delay(10)

def checkWallCollision(x1, y1, x2, y2, wallClearance):
    return (x2 <= x1 + 50 and x1 <= x2 + 50) and (y1 + 50 >= y2 or y1 <= y2 - wallClearance)

def checkCollision(x1, y1, width_1, x2, y2, width_2, height_2):
    return x1 + width_1 >= x2 and x1 <= x2 + width_2 and y1 + width_1 >= y2 and y1 <= y2 + height_2
    
main()