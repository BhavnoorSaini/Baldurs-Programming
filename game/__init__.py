import pygame
import random
from game.enemy import Enemy

# pygame setup
def start_game():
    pygame.init()
    
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    enemies = [Enemy(screen) for _ in range(3)]
    
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")
        
        pygame.draw.circle(screen, "black", player_pos, 40)

        for enemy in enemies:
            enemy.move()
            enemy.draw()
        
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

    
        
        
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()