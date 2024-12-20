# this import allows us to use the
# pygameopen source library
import pygame
from pygame.locals import *
import constants
from constants import *
from player import Player


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
    # instanciate a player
    player = Player(x = constants.SCREEN_WIDTH / 2, y = constants.SCREEN_HEIGHT / 2)

    # creating an infinite game loop with a black screen
    running = True
    while running:
        # creating a pitch black screen
        screen.fill((0,0,0))
        # drawing the player
        player.draw(screen)
        # refreshing the display
        pygame.display.flip()
        # handling events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        # configuring the FPS to 60
        dt = clock.tick(60) / 1000
        
        

    # quitting the game once the loop ends
    pygame.quit()


if __name__ == "__main__":
    main()

