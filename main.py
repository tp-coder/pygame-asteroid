# this import allows us to use the
# pygame open source library
import pygame
import sys
from pygame.locals import *
import constants
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # initializing pygame modules
    pygame.init()
    # setting the screen to the values of constants currently defined as 1280 x 720
    screen = pygame.display.set_mode(size=(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    # creating a clock to control the screen frame rate
    clock = pygame.time.Clock()
    dt = 0
    
    # groups that can hold and manage multiple game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    # adding player objects into the groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # instanciate a player
    player = Player(x = constants.SCREEN_WIDTH / 2, y = constants.SCREEN_HEIGHT / 2)
    # instanciate asteroids
    asteroid_field = AsteroidField()

    # creating an infinite game loop with a black screen
    running = True
    while running:
        # configuring the FPS to 60
        dt = clock.tick(60) / 1000

        # creating a pitch black screen
        screen.fill((0,0,0))

        
        # moving the player object
        for update in updatable:
            update.update(dt)
        
        # checking for collision between asteroids and the player
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over")
                sys.exit()
        
        # drawing the player
        for draw in drawable:
            draw.draw(screen)
        
        # refreshing the display
        pygame.display.flip()

        # handling events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False


if __name__ == "__main__":
    main()

