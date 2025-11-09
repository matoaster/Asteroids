from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = SHOT_RADIUS

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=(self.position),
            radius=SHOT_RADIUS,
            width= 0
            )    

    def update(self, dt):
        self.position += (self.velocity * dt)