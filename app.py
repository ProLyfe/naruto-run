# import pygame 
# import time

# module_charge = pygame.init()
# print(module_charge)

# ecran = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
# time.sleep(10)
# pygame.display.set_caption("Space Invader 3000")

# import pygame
# from pygame.locals import QUIT

# # Initialise screen
# pygame.init()
# screen = pygame.display.set_mode((600, 480))
# pygame.display.set_caption('Basic Pygame program')

# # Fill background
# background = pygame.Surface(screen.get_size())
# background = background.convert()
# background.fill((250, 250, 250))

# # Display some text
# font = pygame.font.Font(None, 36)
# text = font.render("Hello There", 1, (10, 10, 10))
# textpos = text.get_rect()
# textpos.centerx = background.get_rect().centerx
# background.blit(text, textpos)

# # Blit everything to the screen
# screen.blit(background, (0, 0))
# pygame.display.flip()

# # Event loop
# continuer = 1
# while continuer:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             continuer = 0
#     screen.blit(background, (0, 0))
#     pygame.display.flip()

import pygame
from pygame.locals import K_RETURN, K_SPACE, KEYDOWN, KEYUP, QUIT, RESIZABLE

pygame.init()
fenetre = pygame.display.set_mode((200, 200), RESIZABLE)
son = pygame.mixer.Sound("./exemple/Tinquen.wav")

continuer = True
joue = False
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                if not joue:
                    son.play()
                    joue = True
                else:
                    pygame.mixer.unpause()
            elif event.key == K_RETURN:
                son.stop()
                joue = False
        elif event.type == KEYUP:
            if event.key == K_SPACE:
                pygame.mixer.pause()

pygame.quit()