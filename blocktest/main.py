import pygame
from pygame.locals import *
import os
import player

WIDTH, HEIGHT = 720, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Blocks')

WHITE = (255, 255, 255)
BLUE = (0,0,255)
FPS = 30

def draw_window():
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLUE, pygame.Rect(30, 30, 60, 60))
    pygame.draw.line(WIN, (0, 0, 0), (0, 390), (719, 390), 20)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if playerRect.colliderect(wallRect) == True:
            pass
        draw_window()
    pygame.quit()

if __name__ == '__main__':
    main()
