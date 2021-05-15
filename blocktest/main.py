import pygame
from pygame.locals import *
import os

# Initiating Enviroment
pygame.init()
screen = pygame.display.set_mode( (720, 480) )
pygame.display.set_caption('Blocks')


# Constant Variables
GRAY = (200,200,200)
BLUE = (0,0,200)
FPS = 30
clock = pygame.time.Clock()
active = True
player_x = 30
player_y = 321

# Sets Drawing
def draw():
    screen.fill(GRAY)
    player_sprite = pygame.draw.rect(screen, BLUE, pygame.Rect(player_x, player_y, 60, 60))
    ground = pygame.draw.line(screen, (0, 0, 100), (0, 390), (720, 390), 20)
    platforms = [
        pygame.Rect(500, 350, 60, 1200)
    ]

    # screen.blit(player_sprite, (30, 321)) [Only works on sprite images not on shapes]
    pygame.display.flip()

# Allows to have an active state to later quit the game
while active:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    # ------------------------------
    # CASTS PLAYER INPUTS TO ACTIONS
    # ------------------------------

    # Allows to move horizontally
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if keys[pygame.K_RSHIFT]:
            player_x += 15
        elif keys[pygame.K_LSHIFT]:
            player_x += 15
        else:
            player_x += 7.5

    if keys[pygame.K_LEFT]:
        if keys[pygame.K_RSHIFT]:
            player_x -= 15
        elif keys[pygame.K_LSHIFT]:
            player_x -= 15
        else:
            player_x -= 7.5


    # -----------------------
    # NON-PLAYER INTERACTIONS
    # -----------------------

    # Nothing yet!


    # Draws the pre-set drawing
    draw()

# Quits the window
pygame.quit()
