# this import allows us to use the
# pygame open source library
import pygame
import sys
from pygame.locals import *
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from explosion import Explosion
import os

def main():
    # initializing pygame modules
    pygame.init()
    # setting the screen to the values of constants currently defined as 1280 x 720
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("tp-coder Pygame Asteroids")

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # creating a clock to control the screen frame rate
    clock = pygame.time.Clock()
    dt = 0

    # initializing pygame font
    font = pygame.font.Font(None, 24)
    
    def show_controls_screen(screen, font):
        controls = [
            "Controls:",
            "Move: W/A/S/D or Arrow Keys",
            "Shoot: Space",
            "Restart: R (after game over)",
            "Quit: Q (after game over)",
            "",
            "Press any key to start..."
        ]
        screen.fill((0, 0, 0))
        for i, line in enumerate(controls):
            text = font.render(line, True, (255, 255, 255))
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 200 + i * 30))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    waiting = False

    # groups that can hold and manage multiple game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    explosions = pygame.sprite.Group()

    # adding player objects into the groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    Explosion.containers = (explosions, updatable, drawable)

    # instanciate a player
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    # instanciate asteroids otherwise they don't spawn
    asteroid_field = AsteroidField()

    # Show controls screen before starting the game loop
    show_controls_screen(screen, font)

    # rendering the player score and remaining lives
    def render_score_and_lives(screen, score, lives):
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 30))

    HIGHSCORE_FILE = "highscores.txt"

    def load_highscores():
        if not os.path.exists(HIGHSCORE_FILE):
            return []
        with open(HIGHSCORE_FILE, 'r') as f:
            scores = [int(line.strip()) for line in f if line.strip().isdigit()]
        return scores

    def save_highscores(scores):
        with open(HIGHSCORE_FILE, 'w') as f:
            for score in scores[:10]:
                f.write(f"{score}\n")

    def update_highscores(new_score):
        scores = load_highscores()
        scores.append(new_score)
        scores = sorted(scores, reverse=True)[:10]
        save_highscores(scores)
        return scores

    # Print Game Over and give player the option to quit or restart
    def game_over_screen(screen):
        game_over_text = font.render("Game Over", True, (255, 255, 255))
        restart_text = font.render("Press R to restart the game or Q to quit", True, (255, 255, 255))
        screen.blit(game_over_text, (SCREEN_WIDTH / 2 - game_over_text.get_width() / 2, SCREEN_HEIGHT / 2 - 50))
        screen.blit(restart_text, (SCREEN_WIDTH / 2 - restart_text.get_width() / 2, SCREEN_HEIGHT / 2 + 10))

        # Update and display high scores
        highscores = update_highscores(player.score)
        highscore_title = font.render("High Scores:", True, (255, 255, 255))
        screen.blit(highscore_title, (SCREEN_WIDTH / 2 - highscore_title.get_width() / 2, SCREEN_HEIGHT / 2 + 50))
        for i, score in enumerate(highscores):
            score_text = font.render(f"{i+1}. {score}", True, (255, 255, 255))
            screen.blit(score_text, (SCREEN_WIDTH / 2 - score_text.get_width() / 2, SCREEN_HEIGHT / 2 + 80 + i * 25))

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_r:
                        waiting = False
                        main()
                    elif event.key == K_q:
                        pygame.quit()
                        sys.exit()

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
        
        # explosions are also updated here
        
        # checking for collision between asteroids and shots
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    # calling asteroids.get_score method to increase the player score
                    player.increase_score(asteroid.get_points())
                    # If it's the smallest asteroid, spawn an explosion
                    if asteroid.radius == ASTEROID_MIN_RADIUS:
                        Explosion(asteroid.position.x, asteroid.position.y)
                    asteroid.split()
                    shot.kill()

        # checking for collision between asteroids and the player
        for asteroid in asteroids:
            if asteroid.collision(player):
                player.lose_life()
                # Remove all asteroids when the player dies
                for a in list(asteroids):
                    a.kill()
                asteroid.split()
                if player.lives <= 0:
                    game_over_screen(screen)
                    running = False
        
        # drawing the player
        for draw in drawable:
            draw.draw(screen)
        
        # explosions are also drawn here
        
        # rendering the player score
        render_score_and_lives(screen, player.score, player.lives)

        # refreshing the display
        pygame.display.flip()

        # handling events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False


if __name__ == "__main__":
    main()

