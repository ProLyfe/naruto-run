import pygame 
import time

module_charge = pygame.init()
print(module_charge)

ecran = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
fond = pygame.image.load("bg.webp").convert()


time.sleep(10)
pygame.display.set_caption("Space Invader 3000")

loop = True
i = 0

while loop:
    circle = pygame.draw.circle(ecran, (0, 0, 255), (i, 250), 20)
    ecran.fill((0, 0, 0))
    # i = i+1
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                loop = False
            elif event.key == pygame.K_DOWN:
                i = i - 1
            elif event.key == pygame.K_UP:
                i = i + 1
        if event.type == pygame.QUIT:
            loop = False  
        # ecran.blit(fond, (0, 0))
    ecran.blit(fond, (0, 0))
  
    pygame.display.flip()

pygame.quit()