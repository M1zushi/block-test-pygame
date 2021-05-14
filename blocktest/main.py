import pygame
from pygame.locals import *
import os

# Initiating
pygame.init()
screen = pygame.display.set_mode( (720, 480) )
pygame.display.set_caption('Blocks')


# Constant Variables
GRAY = (200,200,200)
BLUE = (0,0,200)
FPS = 30
clock = pygame.time.Clock()
active = True

# Drawings
def draw():
    player_sprite = pygame.draw.rect(screen, BLUE, pygame.Rect(30, 321, 60, 60))
    ground = pygame.draw.line(screen, (0, 0, 100), (0, 390), (719, 390), 20)

    # screen.blit(player_sprite, (30, 321)) [Only works on sprite images not on shapes]
    screen.fill(GRAY)
    pygame.display.flip()

# Game Loop
while active:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    # Inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_sprite.x += 10
    if keys[pygame.K_d]:
        player_sprite.x -= 10

    # Draw
    draw()

# Quit
pygame.quit()
