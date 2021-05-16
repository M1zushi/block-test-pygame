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
new_player_x = player_x
oldx = player_x
player_speed = 0
player_acceleration = 0.5
max_player_speed = 7.5


platforms = [
    pygame.Rect(225, 250, 300, 30),
    pygame.Rect(225, 200, 300, 30)
]

# Sets Drawing
def draw():
    screen.fill(GRAY)
    ground = pygame.draw.line(screen, (0, 0, 100), (0, 390), (720, 390), 20)
    player_sprite = pygame.draw.rect(screen, BLUE, pygame.Rect(player_x, player_y, 60, 60))

    # screen.blit(player_sprite, (30, 321)) [Only works on sprite images not on shapes]
    for o in platforms:
        pygame.draw.rect(screen, BLUE, o)

    pygame.display.flip()

# Allows to have an active state to later quit the game
while active:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    # ------------------------
    # PLAYER MOVEMENT + INPUTS
    # ------------------------

    # Allows to move horizontally only if there is no collision

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if keys[pygame.K_RSHIFT]:
            if player_speed < max_player_speed:
                player_speed += player_acceleration
            new_player_x += player_speed * 2
        elif keys[pygame.K_LSHIFT]:
            if player_speed < max_player_speed:
                player_speed += player_acceleration
            new_player_x += player_speed * 2
        else:
            if player_speed < max_player_speed:
                player_speed += player_acceleration
            new_player_x += player_speed

    if keys[pygame.K_LEFT]:
        if keys[pygame.K_RSHIFT]:
            if player_speed < max_player_speed:
                player_speed += player_acceleration
            new_player_x -= player_speed * 2
        elif keys[pygame.K_LSHIFT]:
            if player_speed < max_player_speed:
                player_speed += player_acceleration
            new_player_x -= player_speed * 2
        else:
            if player_speed < max_player_speed:
                player_speed += player_acceleration
            new_player_x -= player_speed

    new_player_rect = pygame.Rect(new_player_x, player_y, 60, 60)
    x_collision = False

    for o in platforms:
        if o.colliderect(new_player_rect):
            x_collision = True
            break

    if x_collision == False:
        player_x = new_player_x
        newx = new_player_x

    if oldx == newx:
        player_speed = 0

    oldx = player_x


    # Allows to move vertically if there is no collision

    # Code


    # -----------------
    # ITEM INTERACTIONS
    # -----------------

    # Nothing yet!

    # Draws the pre-set drawing
    draw()

# Quits the window
pygame.quit()
