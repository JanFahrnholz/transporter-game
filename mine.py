

import pygame
import this
import os


class Mine(pygame.sprite.Sprite):

    imgH = 50
    imgW = 200

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load("assets/player.png"), (self.imgW, self.imgH))
        self.rect = self.image.get_rect()
        self.pos = (246, 563)

    def tick(self, screen):

        screen.blit(self.image, self.pos)
