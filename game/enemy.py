import random
import math
from game import pygame
import os

class Enemy:
    def __init__(self, screen):
        self.screen = screen
        self.x = random.randint(50, screen.get_width() - 50)
        self.y = random.randint(50, screen.get_height() - 50)
        self.speed = 0.1
        self.direction = random.randint(0, 360)

    def draw(self):
        image_path = os.path.join(os.path.dirname(__file__), "assets", "scary2_shark-removebg-preview.png")
        shark_image = pygame.image.load(image_path)
        shark_image = pygame.transform.scale(shark_image, (shark_image.get_width() // 3, shark_image.get_height() // 3))
        image_width, image_height = shark_image.get_size()
        self.screen.blit(shark_image, (self.x - image_width // 3, self.y - image_height // 3))

    def move(self):
        # Change the direction of the enemy slightly
        self.direction += random.randint(-1, 1)
        # Update the enemy's position based on its speed and direction
        self.x += self.speed * math.cos(math.radians(self.direction))
        self.y += self.speed * math.sin(math.radians(self.direction))
        # Ensure the enemy stays within the screen boundaries
        self.x = max(100, min(self.x, self.screen.get_width() - 100))
        self.y = max(100, min(self.y, self.screen.get_height() - 100))