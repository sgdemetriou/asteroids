import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    pygame.init()
    fps_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updateables, drawables)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updateables.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = fps_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
