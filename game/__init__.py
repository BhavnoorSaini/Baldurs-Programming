import pygame
import os
from game.enemy import sharkEnemy, shark2Enemy
from game.character import XP

# pygame setup
def start_game():
    pygame.init()
    
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Baldurs Programming")
    clock = pygame.time.Clock()
    running = True
    dt = 0

    sharkEnemies = [sharkEnemy(screen) for _ in range(2)]
    shark2Enemies = [shark2Enemy(screen) for _ in range(2)]
    
    map_path = os.path.join(os.path.dirname(__file__), "assets", "Final Map.jpg")
    background = pygame.image.load(map_path)
    def draw_background(backgrond):
        size = pygame.transform.scale(backgrond, (screen.get_width(), screen.get_height()))
        screen.blit(size, (0, 0))
    
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        #screen.fill("white")
        draw_background(background)
        
        
        
        pygame.draw.circle(screen, "black", player_pos, 40)

        for sharkEnemy in sharkEnemies:
            sharkEnemy.move()
            sharkEnemy.draw()
            # Calculate distance between player and enemy
            distance = pygame.math.Vector2(sharkEnemy.x, sharkEnemy.y).distance_to(player_pos)

            # If distance is less than threshold, draw a red rectangle
            if distance < 60:  # adjust this value as needed
                font = pygame.font.Font(None, 28)
                text = font.render("PRESS E TO ATTACK", True, (255, 255, 255))
                text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() - 45))
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() - 70, 200, 50))
                screen.blit(text, text_rect)
        for shark2Enemy in shark2Enemies:
            shark2Enemy.move()
            shark2Enemy.draw()
            # Calculate distance between player and enemy
            distance = pygame.math.Vector2(shark2Enemy.x, shark2Enemy.y).distance_to(player_pos)

            # If distance is less than threshold, draw a red rectangle
            if distance < 60:  # adjust this value as needed
                font = pygame.font.Font(None, 28)
                text = font.render("PRESS E TO ATTACK", True, (255, 255, 255))
                text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() - 45))
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() - 70, 200, 50))
                screen.blit(text, text_rect)
        
        xp_bar = XP(screen)
        xp_bar.draw(100)        # can either swap to the 0%, 50%, 75%, or 100% xp bar
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if player_pos.y > 40:
                player_pos.y -= 500 * dt
        if keys[pygame.K_s]:
            if player_pos.y < screen.get_height() - 40:
                player_pos.y += 500 * dt
        if keys[pygame.K_a]:
            if player_pos.x > 40:
                player_pos.x -= 500 * dt
        if keys[pygame.K_d]:
            if player_pos.x < screen.get_width() - 40:
                player_pos.x += 500 * dt
        print(player_pos.x, ",",player_pos.y)
    
        if player_pos.x < 700 and player_pos.x > 600 and player_pos.y < 420 and player_pos.y > 270:
            font = pygame.font.Font(None, 28)
            text = font.render("PRESS Q TO SHOP AT THE MERCHANT", True, (255, 255, 255))
            text_rect = text.get_rect(center=(screen.get_width() // 2, 600))
            rect_width = text.get_width() + 20  # Add 20 pixels padding
            pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(screen.get_width() // 2 - rect_width // 2, 575, rect_width, 50))
            screen.blit(text, text_rect)
            
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()