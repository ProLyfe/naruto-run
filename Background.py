import pygame, sys
from pygame.locals import *
import random

class Background():
      def __init__(self, display):
            self.bgimage = pygame.image.load('forest.jpeg')
            self.rectBGimg = self.bgimage.get_rect()
 
            self.bgY1 = 0
            self.bgX1 = 0
 
            self.bgY2 = self.rectBGimg.height
            self.bgX2 = 0
 
            self.movingUpSpeed = 5
         
            self.display = display
      def update(self):
        self.bgY1 -= self.movingUpSpeed
        self.bgY2 -= self.movingUpSpeed
        if self.bgY1 <= -self.rectBGimg.height:
            self.bgY1 = self.rectBGimg.height
        if self.bgY2 <= -self.rectBGimg.height:
            self.bgY2 = self.rectBGimg.height
             
      def render(self):
         self.display.blit(self.bgimage, (self.bgX1, self.bgY1))
         self.display.blit(self.bgimage, (self.bgX2, self.bgY2))
    