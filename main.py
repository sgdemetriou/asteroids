import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    pygame.init()
    fps_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=(0,0,0))
        pygame.display.flip()
        dt = fps_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
