import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player


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

    player = Player(
    SCREEN_WIDTH / 2,
    SCREEN_HEIGHT / 2
    )


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
        for player in drawable:
            player.draw(screen)
        # (later you'll draw your game objects here)
        pygame.display.flip()

        # 2 & 3. Limit to 60 FPS and get delta time
        # tick() returns milliseconds since last call → convert to seconds
        dt = clock.tick(60) / 1000.0

        

    pygame.quit()

if __name__ == "__main__":
    main()