

import pygame
import this
import os


class Player(pygame.sprite.Sprite):

    acc = 1
    accGain = 0.75
    accDecrease = 1
    maxAcc = 15

    moving = False
    imgH = 50
    imgW = 200

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load("assets/player.png"), (self.imgW, self.imgH))
        self.rect = self.image.get_rect()

        # Position and direction
        self.vx = 0
        self.pos = (357, 380)
        self.vel = 0
        self.direction = "RIGHT"

    def tick(self, screen):
        if self.moving == False:
            self.decreaseAccGain()
        else:
            self.moving = False

        screen.blit(self.image, self.pos)

    def move(self, dir):

        worldSize = pygame.display.get_window_size()

        pos = self.pos
        self.moving = True

        if dir == "up":
            self.moveUp()

        if dir == "down":
            self.moveDown(worldSize)

        if dir == "left":
            self.moveLeft()

        if dir == "right":
            self.moveRight(worldSize)

        if self.acc + self.accGain <= self.maxAcc:
            self.acc += self.accGain

    def moveDown(self, worldSize):
        if self.pos[1] + self.acc + self.imgH <= worldSize[1]:
            self.pos = (self.pos[0], self.pos[1] + self.acc)

    def moveUp(self):
        if self.pos[1] - self.acc >= 0:
            self.pos = (self.pos[0], self.pos[1] - self.acc)

    def moveRight(self, worldSize):
        if self.pos[0] + self.acc + self.imgW <= worldSize[0]:
            self.pos = (self.pos[0] + self.acc, self.pos[1])

    def moveLeft(self):
        if self.pos[0] - self.acc >= 0:
            self.pos = (self.pos[0] - self.acc, self.pos[1])

    def decreaseAccGain(self):
        if self.acc - self.accDecrease <= 1:
            self.acc = 1
            pass

        self.acc -= self.accDecrease
