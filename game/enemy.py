import random
import math
from game import pygame

class Enemy:
    def __init__(self, screen):
        self.screen = screen
        self.x = random.randint(50, screen.get_width() - 50)
        self.y = random.randint(50, screen.get_height() - 50)
        self.speed = random.randint(1, 5)
        self.direction = random.randint(0, 360)

    def draw(self):
        pygame.draw.circle(self.screen, (255, 0, 0), (self.x, self.y), 50)

    def move(self):
        self.direction += random.randint(-10, 10)
        self.x += self.speed * math.cos(math.radians(self.direction))
        self.y += self.speed * math.sin(math.radians(self.direction))
        self.x = max(50, min(self.x, self.screen.get_width() - 50))
        self.y = max(50, min(self.y, self.screen.get_height() - 50))