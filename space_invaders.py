import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

player_image = pygame.image.load("battleship (1).png")
player_x = 370
player_y = 500

enemy_image = pygame.image.load("ufo (2).png")
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 150)


def player(x, y):
    screen.blit(player_image, (x, y))


def enemy(x, y):
    screen.blit(
        enemy_image, (x + random.randint(-0.5, 0.5), y + random.randint(-0.2, 0.2))
    )


while True:
    looper = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            looper = False

    screen.fill((0, 0, 80))
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    pygame.display.update()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_x -= 0.5
        if event.key == pygame.K_RIGHT:
            player_x += 0.5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            player_x += 0

    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    if enemy_x <= 0:
        enemy_x += 0.5
    elif enemy_x >= 736:
        enemy_x -= 0.5
