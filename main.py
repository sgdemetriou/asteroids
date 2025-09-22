import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    pygame.init()
    fps_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateables, drawables)
    Asteroid.containers = (updateables, drawables, asteroids)
    AsteroidField.containers = (updateables)
    Shot.containers = (updateables, drawables, shots)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updateables.update(dt)

        for asteroid in asteroids:
            # player collision check
            if asteroid.collision(player):
                print("Game over!")
                return
            # shot collision check
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()

        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = fps_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
