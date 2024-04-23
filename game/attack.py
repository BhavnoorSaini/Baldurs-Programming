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
        start_y = 535
        import pygame.font


        font = pygame.font.Font(pygame.font.get_default_font(), 15)  # Choose the default font and font size

        
        for i in range(button_count):
            row = i // 2  # Calculate the row index
            col = i % 2  # Calculate the column index

            button_x = start_x + (button_width + button_spacing) * col
            button_y = start_y + (button_height + button_spacing) * row

            pygame.draw.rect(screen, (255, 0, 0), (button_x, button_y, button_width, button_height))
            # Add code to draw text on the button here
            
            if i == 0:
                text = "Slash (Easy)"
            elif i == 1:
                text = "Heavy Strike (Medium)"
            elif i == 2:
                text = "Domain Expansion (Hard)"
            elif i == 3:
                text = "Run"

            text_surface = font.render(text, True, (255, 255, 255))  # Render the text
            text_rect = text_surface.get_rect(center=(button_x + button_width / 2, button_y + button_height / 2))  # Center the text
            screen.blit(text_surface, text_rect)  # Draw the text on the button

        # Add code to handle button click events here
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i in range(button_count):
                    row = i // 2
                    col = i % 2
                    button_x = start_x + (button_width + button_spacing) * col
                    button_y = start_y + (button_height + button_spacing) * row
                    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
                    if button_rect.collidepoint(mouse_pos):
                        if i == 0:
                            print("Slash (Easy)")
                        elif i == 1:
                            print("Heavy Strike (Medium)")
                        elif i == 2:
                            print("Domain Expansion (Hard)")
                        elif i == 3:
                            print("Run")
                            return 1
                            
        
        
    
    def draw_enemy(self, screen):
        player_path = os.path.join(os.path.dirname(__file__), "assets", "player.png")
        player = pygame.image.load(player_path)
        player = pygame.transform.scale(player, (200, 200))
        screen.blit(player, (260, 250))
        enemy_path = os.path.join(os.path.dirname(__file__), "assets", "scary_shark-removebg-preview.png")
        enemy = pygame.image.load(enemy_path)
        enemy = pygame.transform.scale(enemy, (200, 200))
        screen.blit(enemy, (820, 150))
