import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # initialize game
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # grouping objects
    updatable_obj = pygame.sprite.Group()
    drawable_obj = pygame.sprite.Group()
    asteroids_obj = pygame.sprite.Group()
    shot_obj = pygame.sprite.Group()

    Asteroid.containers = (asteroids_obj, updatable_obj, drawable_obj)
    AsteroidField.containers = updatable_obj
    asfield = AsteroidField()

    Player.containers = (updatable_obj, drawable_obj)
    Shot.containers = (shot_obj, updatable_obj, drawable_obj)
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
   
   # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updatable in updatable_obj:
            updatable.update(dt)

        for asteroid in asteroids_obj:
            if asteroid.isCollision(player1):
                print("Game over!")
                sys.exit()
            for bullet in shot_obj:
                if asteroid.isCollision(bullet):
                    asteroid.split()
                    bullet.kill()

        screen.fill((0,0,0))
        
        for drawable in drawable_obj:
            drawable.draw(screen)
        
        pygame.display.flip()

        # Limit FPS to 60
        dt = clock.tick(60) / 1000
        
        
if __name__ == "__main__":
    main()
