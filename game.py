import pygame
import sys

pygame.init()


pygame.display.set_caption("Ninja Game")
screen = pygame.display.set_mode((640,480))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)