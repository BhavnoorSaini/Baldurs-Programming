from game import pygame
import os

class Battle:
    def draw_battle(self,screen):
        battle_path = os.path.join(os.path.dirname(__file__), "assets", "battlewindow.jpg")
        background = pygame.image.load(battle_path)
        size = pygame.transform.scale(background, (1280, 720))
        screen.blit(size, (0, 0))
       
