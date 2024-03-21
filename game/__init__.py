import pygame
import random

# pygame setup

def start_game():
    pygame.init()
    
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    
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

        # Define a list to store the positions of the circles
        circle_positions = []

        # Generate random positions for the circles
        for _ in range(3):
            circle_pos = pygame.Vector2(random.randint(40, screen.get_width() - 40), random.randint(40, screen.get_height() - 40))
            circle_positions.append(circle_pos)

        # Move and draw the circles
        for circle_pos in circle_positions:
            # Move the circle slowly
            circle_pos.x += random.uniform(-1, 1) * 0.1 * dt
            circle_pos.y += random.uniform(-1, 1) * 0.1 * dt

            # Ensure the circle stays within the window
            circle_pos.x = max(40, min(circle_pos.x, screen.get_width() - 40))
            circle_pos.y = max(40, min(circle_pos.y, screen.get_height() - 40))

            # Draw the circle
            pygame.draw.circle(screen, "red", circle_pos, 40)
        
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()