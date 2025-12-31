import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,        
            self.radius,
            LINE_WIDTH
        )

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        # Siempre se destruye
        self.kill()

        # Asteroide chico → no se divide
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        # Ángulo aleatorio
        angle = random.uniform(20, 50)

        # Nuevas direcciones
        velocity_1 = self.velocity.rotate(angle)
        velocity_2 = self.velocity.rotate(-angle)

        # Nuevo tamaño
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Crear nuevos asteroides
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Más rápidos
        asteroid_1.velocity = velocity_1 * 1.2
        asteroid_2.velocity = velocity_2 * 1.2