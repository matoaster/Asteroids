from circleshape import CircleShape
from constants import *
import pygame
import random
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=(self.position),
            radius=self.radius,
            width= LINE_WIDTH
            )

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        else:
            log_event("asteroid_split")
            angles = random.uniform(20, 50)
            vector1 = self.velocity.rotate(angles)
            vector2 = self.velocity.rotate(-angles)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid1.velocity = vector1 * 1.2
            asteroid2.velocity = vector2 * 1.2 
