from game import pygame
import os

class XP:
    def __init__(self,screen):
        self.screen = screen
        
    def draw(self, xp):
        image_path = os.path.join(os.path.dirname(__file__), "xp", "xp_" + str(xp) + "-removebg-preview.png")
        xp_image = pygame.image.load(image_path)
        xp_image = pygame.transform.scale(xp_image, (xp_image.get_width() // 2, xp_image.get_height() // 2))
        self.screen.blit(xp_image, (0, 0))