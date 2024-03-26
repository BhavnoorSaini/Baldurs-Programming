import pygame
import os
from game.enemy import sharkEnemy, shark2Enemy
from game.character import XP
from game.merchant import Merchant
from game.attack import Battle

# pygame setup
def start_game():
    pygame.init()
    
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Baldurs Programming")
    icon = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "hacket-removebg-preview.png"))
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    running = True
    dt = 0

    # Create enemy instances
    enemies1 = [sharkEnemy(screen) for _ in range(2)]
    enemies2 = [shark2Enemy(screen) for _ in range(2)]
    
    # Load background image
    map_path = os.path.join(os.path.dirname(__file__), "assets", "Final Map.jpg")
    background = pygame.image.load(map_path)
    
    def draw_background(backgrond):
        size = pygame.transform.scale(backgrond, (screen.get_width(), screen.get_height()))
        screen.blit(size, (0, 0))
        
    def start_battle(screen, clock):
        battle = Battle()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            battle.draw_battle(screen)
            pygame.display.flip()
            clock.tick(60)
    
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    while running:
        # Poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw background image
        draw_background(background)
        
        # Draw player character
        pygame.draw.circle(screen, "black", player_pos, 40)

        # Handle enemy interactions
        for enemy in enemies1:
            enemy.move()
            enemy.draw()
            # Calculate distance between player and enemy
            distance = pygame.math.Vector2(enemy.x, enemy.y).distance_to(player_pos)

            # If distance is less than threshold, draw a red rectangle
            if distance < 60:  # adjust this value as needed
                font = pygame.font.Font(None, 28)
                text = font.render("PRESS E TO ATTACK", True, (255, 255, 255))
                text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() - 45))
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() - 70, 200, 50))
                screen.blit(text, text_rect)
                if keys[pygame.K_e]:
                    #battle = Battle()
                    #battle.draw_battle(screen)
                    start_battle(screen, clock)
                    
        
        for enemy in enemies2:
            enemy.move()
            enemy.draw()
            # Calculate distance between player and enemy
            distance = pygame.math.Vector2(enemy.x, enemy.y).distance_to(player_pos)

            # If distance is less than threshold, draw a red rectangle
            if distance < 60:  # adjust this value as needed
                font = pygame.font.Font(None, 28)
                text = font.render("PRESS E TO ATTACK", True, (255, 255, 255))
                text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() - 45))
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() - 70, 200, 50))
                screen.blit(text, text_rect)
                if keys[pygame.K_e]:
                    #battle = Battle()
                    #battle.draw_battle(screen)
                    start_battle(screen, clock)
        
        # Draw XP bar
        xp_bar = XP(screen)
        xp_bar.draw(50)        # can either swap to the 0%, 50%, 75%, or 100% xp bar
        
        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if player_pos.y > 40:
                player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            if player_pos.y < screen.get_height() - 40:
                player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            if player_pos.x > 40:
                player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            if player_pos.x < screen.get_width() - 40:
                player_pos.x += 300 * dt
    
        # Check if player is near the merchant
        if player_pos.x < 700 and player_pos.x > 600 and player_pos.y < 420 and player_pos.y > 270:
            font = pygame.font.Font(None, 28)
            text = font.render("HOLD Q TO SHOP AT THE MERCHANT", True, (255, 255, 255))
            text_rect = text.get_rect(center=(screen.get_width() // 2, 600))
            rect_width = text.get_width() + 20  
            pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(screen.get_width() // 2 - rect_width // 2, 575, rect_width, 50))
            screen.blit(text, text_rect)
            if keys[pygame.K_q]:
                Merchant.draw_merchant(Merchant)
            
        # Update the display
        pygame.display.flip()

        # Limit FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()