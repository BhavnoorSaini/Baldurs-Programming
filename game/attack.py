from game import pygame
import os

class Battle:
    def draw_battle(self,screen):
        battle_path = os.path.join(os.path.dirname(__file__), "assets", "battlewindow.jpg")
        background = pygame.image.load(battle_path)
        size = pygame.transform.scale(background, (1280, 720))
        screen.blit(size, (0, 0))
       
    def draw_buttons(self, screen):
        button_width = 280
        button_height = 60
        button_spacing = 20
        button_count = 4
        start_x = 90
        start_y = 540

        for i in range(button_count):
            row = i // 2  # Calculate the row index
            col = i % 2  # Calculate the column index

            button_x = start_x + (button_width + button_spacing) * col
            button_y = start_y + (button_height + button_spacing) * row

            pygame.draw.rect(screen, (255, 0, 0), (button_x, button_y, button_width, button_height))
            # Add code to draw text on the button here
