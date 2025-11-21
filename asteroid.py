import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from logger import log_event




class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)



    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
         self.position += self.velocity * dt
        
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
       
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        split_1_movement = self.velocity.rotate(random_angle)
        split_2_movement = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1  = Asteroid(self.position.x, self.position.y , new_radius)
        asteroid_2  = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = split_1_movement * 1.2
        asteroid_2.velocity = split_2_movement * 1.2



        
       



