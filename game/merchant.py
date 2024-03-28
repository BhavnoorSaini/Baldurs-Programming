from game import pygame
import os

class Merchant:
    def draw_merchant(self):
        screen_width = pygame.display.get_surface().get_width()
        screen_height = pygame.display.get_surface().get_height()

        # Draw the brown square
        square_width = screen_width // 2 - 50
        square_height = screen_height
        square_color = (139, 69, 19)  # Brown color
        pygame.draw.rect(pygame.display.get_surface(), square_color, (screen_width // 2 + 50, 0, square_width, square_height))

        # Draw the text
        font = pygame.font.Font(None, 36)
        text_color = (255, 255, 255)  # White color
        text_damage = font.render("DAMAGE", True, text_color)
        text_heal = font.render("HEAL", True, text_color)
        pygame.display.get_surface().blit(text_damage, (screen_width // 2 + 100, screen_height // 2 - 50))
        pygame.display.get_surface().blit(text_heal, (screen_width // 2 + 100, screen_height // 2 + 50))

        # Draw the buttons
        button_width = 50
        button_height = 50
        button_color = (0, 0, 0)  # Black color
        pygame.draw.rect(pygame.display.get_surface(), button_color, (screen_width // 2 + 250, screen_height // 2 - 50, button_width, button_height))
        pygame.draw.rect(pygame.display.get_surface(), button_color, (screen_width // 2 + 250, screen_height // 2 + 50, button_width, button_height))
        button1 = pygame.Rect(screen_width // 2 + 250, screen_height // 2 - 50, button_width, button_height)
        button2 = pygame.Rect(screen_width // 2 + 250, screen_height // 2 + 50, button_width, button_height)


        # Draw the "+" symbol
        plus_symbol = font.render("+", True, text_color)
        plus_symbol_width = plus_symbol.get_width()
        plus_symbol_height = plus_symbol.get_height()
        plus_symbol_x = screen_width // 2 + 250 + (button_width - plus_symbol_width) // 2
        plus_symbol_y = screen_height // 2 - 50 + (button_height - plus_symbol_height) // 2
        pygame.display.get_surface().blit(plus_symbol, (plus_symbol_x, plus_symbol_y))

        plus_symbol_y = screen_height // 2 + 50 + (button_height - plus_symbol_height) // 2
        pygame.display.get_surface().blit(plus_symbol, (plus_symbol_x, plus_symbol_y))
        
        # Load the image of the gold
        image_path = os.path.join(os.path.dirname(__file__), "assets", "gold-removebg-preview.png")
        gold_image = pygame.image.load(image_path)

        # Get the original image dimensions
        original_width = gold_image.get_width()
        original_height = gold_image.get_height()

        # Calculate the new image dimensions
        new_width = original_width // 4
        new_height = original_height // 4

        # Resize the image
        gold_image = pygame.transform.scale(gold_image, (new_width, new_height))

        # Calculate the position of the image
        image_x = screen_width // 2 + 50
        image_y = screen_height - new_height

        # Draw the image
        pygame.display.get_surface().blit(gold_image, (image_x, image_y))

        # Draw the text
        text = font.render("$0", True, text_color)      #amount of gold the player has
        text_x = image_x + new_width + 10
        text_y = image_y + (new_height - text.get_height()) // 2
        pygame.display.get_surface().blit(text, (text_x, text_y))
        
        # Clicks the buttons
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button1.collidepoint(mouse_pos):
                    print("Button 1")# Perform action for button 1
                    pass
                elif button2.collidepoint(mouse_pos):
                    print("Button 2")# Perform action for button 2
                    pass