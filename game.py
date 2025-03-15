import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 1800
screen_height = 1080

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Shooter")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Player properties
player_size = 50
player_pos = [screen_width // 2, screen_height - 2 * player_size]
player_speed = 10

# Bullet properties
bullet_size = 10
bullet_speed = 20
bullets = []

# Enemy properties
enemy_size = 50
enemy_pos = [random.randint(0, screen_width - enemy_size), 0]
enemy_speed = 10

# Game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < screen_width - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_SPACE]:
        bullets.append([player_pos[0] + player_size // 2, player_pos[1]])

    screen.fill(black)

    # Move bullets
    for bullet in bullets:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Move enemy
    enemy_pos[1] += enemy_speed
    if enemy_pos[1] > screen_height:
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, screen_width - enemy_size)

    # Check for collisions
    for bullet in bullets:
        if (enemy_pos[0] < bullet[0] < enemy_pos[0] + enemy_size) and \
           (enemy_pos[1] < bullet[1] < enemy_pos[1] + enemy_size):
            bullets.remove(bullet)
            enemy_pos = [random.randint(0, screen_width - enemy_size), 0]

    if (player_pos[0] < enemy_pos[0] < player_pos[0] + player_size or
        player_pos[0] < enemy_pos[0] + enemy_size < player_pos[0] + player_size) and \
       (player_pos[1] < enemy_pos[1] < player_pos[1] + player_size or
        player_pos[1] < enemy_pos[1] + enemy_size < player_pos[1] + player_size):
        game_over = True

    # Draw everything
    pygame.draw.rect(screen, red, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, white, (player_pos[0], player_pos[1], player_size, player_size))
    for bullet in bullets:
        pygame.draw.rect(screen, blue, (bullet[0], bullet[1], bullet_size, bullet_size))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()