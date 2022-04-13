import sys
import pygame
from mine import Mine
from player import Player

pygame.init()
clock = pygame.time.Clock()
gameActive = True

size = width, height = 1408, 640
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Transporter Spiel")

bg = pygame.image.load("assets/bg.png")

player = Player()
mine = Mine()

while gameActive:

    screen.blit(bg, (0, 0))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameActive = False
            print("Spieler hat Quit-Button angeklickt")

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_DOWN]:
        player.move("down")

    if pressed[pygame.K_UP]:
        player.move("up")

    if pressed[pygame.K_LEFT]:
        player.move("left")

    if pressed[pygame.K_RIGHT]:
        player.move("right")

    player.tick(screen)
    mine.tick(screen)
    pygame.display.update()

    clock.tick(60)
