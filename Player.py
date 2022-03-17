import pygame, sys
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, width):
        super().__init__() 
        self.width = width
        self.image = pygame.image.load("uzumaki2.png")
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center = (160, 420))
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < self.width:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
  