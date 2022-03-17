#Imports
import pygame, sys
from pygame.locals import *
import random, time
import pygame_menu
from Player import Player
from Ennemy import Enemy
from Background import Background

pygame.init()

bg_sound = pygame.mixer.Sound('boss.wav')


FPS = 60
FramePerSec = pygame.time.Clock()
 
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
 
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
P1 = Player(SCREEN_WIDTH)
E1 = Enemy(SCREEN_WIDTH, SCORE, SPEED)
 
def start_the_game():
    while True:
        pygame.mixer.Sound.play(bg_sound)
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                E1.speed += 0.5     
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    
        back_ground.update()
        back_ground.render()

        scores = font_small.render(str(E1.score), True, BLACK)
        DISPLAYSURF.blit(scores, (10,10))
    
        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()
    
        if pygame.sprite.spritecollideany(P1, enemies):
            pygame.play()
            time.sleep(0.8)
                        
            DISPLAYSURF.blit(game_over, (30,250))
            
            pygame.display.update()
            for entity in all_sprites:
                    entity.kill() 
            time.sleep(1.5)
            pygame.quit()
            sys.exit()        
            
        pygame.display.update()
        FramePerSec.tick(FPS)
    pass

menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='John Doe')
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT) 

back_ground = Background(DISPLAYSURF)
 
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
while True:
    menu.mainloop(DISPLAYSURF)




