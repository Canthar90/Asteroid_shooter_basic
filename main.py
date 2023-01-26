import pygame
import sys


pygame.init()
WINOW_WIDTH, WINDOW_HEIGHT = 1280, 720

display_surface = pygame.display.set_mode((WINOW_WIDTH, WINDOW_HEIGHT))

test_surf = pygame.Surface((400, 100))

pygame.display.set_caption("Asteroid shooter V1")

while True:
    
    # input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # updates
    display_surface.fill((34, 34, 54))
    display_surface.blit(test_surf, (100,0))
    test_surf.fill((173, 59, 17))
    
    # show the frame to the player / update display surface
    pygame.display.update()