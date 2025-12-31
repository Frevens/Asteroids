import pygame
import sys
import time
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot




pygame.init()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # 1. Crea un reloj y una variable de tiempo delta dt.
    clock = pygame.time.Clock()  # Inicia el reloj
    dt = 0                       # Delta time en segundos


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

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

        # Lógica del juego va acá (usa dt para movimientos basados en tiempo (time-based movement)).
        # 🔹 UPDATE (lógica del juego)
        updatable.update(dt)

        

        
        log_state()

        # Dibuja todo
        screen.fill("black")
        # Dibuja Player en cada cuadro. 
        for object in drawable:
            object.draw(screen)
        
        # (later you'll draw your game objects here)
        pygame.display.flip()

        # 2 & 3. Limita a 60 FPS y obtiene delta time
        # tick() regresa milisegundos desde la última llamada → convierte a segundos
        dt = clock.tick(60) / 1000.0

        #Chequea coliciones
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                time.sleep(1) #se pause por 1 segundo
                sys.exit()
        
        # 🔫 Colisiones disparos ↔ asteroides
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    break  # el asteroide ya no existe

        

    pygame.quit()

if __name__ == "__main__":
    main()