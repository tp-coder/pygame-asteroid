# this import allows us to use the
# pygameopen source library
import pygame
from pygame.locals import *
import constants
from constants import *


def game_loop(screen):
    # this function is to make the game more modular and easier to maintain
    # creating an infinite game loop with a black screen
    running = True
    while running:
        # creating a pitch black screen
        screen.fill((0,0,0))
        # refreshing the display
        pygame.display.flip()
        # handling events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False


def main():
    # initializing pygame modules
    pygame.init()
    # setting the screen to the values of constants currently defined as 1280 x 720
    screen = pygame.display.set_mode(size=(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    # calling the game loop function
    game_loop(screen)

    # quitting the game once the loop ends
    pygame.quit()


if __name__ == "__main__":
    main()

