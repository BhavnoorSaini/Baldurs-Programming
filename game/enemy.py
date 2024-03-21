import random
import math
from game import pygame
import os

class Enemy:
    def __init__(self, screen):
        self.screen = screen
        self.x = random.randint(50, screen.get_width() - 50)
        self.y = random.randint(50, screen.get_height() - 50)
        self.speed = random.randint(1, 5)
        self.direction = random.randint(0, 360)

    def draw(self):
        image_path = os.path.join(os.path.dirname(__file__), "scary2_shark-removebg-preview.png")
        shark_image = pygame.image.load(image_path)
        shark_image = pygame.transform.scale(shark_image, (shark_image.get_width() // 2, shark_image.get_height() // 2))
        self.screen.blit(shark_image, (self.x - 20, self.y - 20))

    def move(self):
        # Change the speed of the enemy
        self.direction += random.randint(-10, 10)
        self.x += self.speed * math.cos(math.radians(self.direction))
        self.y += self.speed * math.sin(math.radians(self.direction))
        self.x = max(100, min(self.x, self.screen.get_width() - 100))
        self.y = max(100, min(self.y, self.screen.get_height() - 100))