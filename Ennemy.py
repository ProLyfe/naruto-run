import pygame, sys
from pygame.locals import *
import random

class Enemy(pygame.sprite.Sprite):
      def __init__(self, width, score, speed):
        super().__init__() 
        self.image = pygame.image.load("shurikens.png")
        self.surf = pygame.Surface((42, 70))
        self.width = width
        self.rect = self.surf.get_rect(center = (random.randint(40, self.width-40), 0))
        self.score = score
        self.speed = speed
 
      def move(self):
        # global SCORE
        self.rect.move_ip(0, self.speed)
        if (self.rect.top > 600):
            self.score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, self.width - 40), 0)
            return self.score
 