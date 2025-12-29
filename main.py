import pygame
import sys
import time
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField




pygame.init()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # 1. Create a clock object and dt variable before the loop
    clock = pygame.time.Clock()  # Correct way to instantiate the Clock
    dt = 0                       # Delta time in seconds


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(
    SCREEN_WIDTH / 2,
    SCREEN_HEIGHT / 2
    )
    asteroid_field = AsteroidField()

    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Game logic would go here (using dt for time-based movement)
        # 🔹 UPDATE (lógica del juego)
        updatable.update(dt)

        

        
        log_state()

        # Draw everything
        screen.fill("black")
        # Draw the player in every frame. 
        for object in drawable:
            object.draw(screen)
        
        # (later you'll draw your game objects here)
        pygame.display.flip()

        # 2 & 3. Limit to 60 FPS and get delta time
        # tick() returns milliseconds since last call → convert to seconds
        dt = clock.tick(60) / 1000.0

        #Checking collitions
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                time.sleep(1) #se pause por 1 segundos
                sys.exit()

        

    pygame.quit()

if __name__ == "__main__":
    main()