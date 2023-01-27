import pygame
import sys


pygame.init()
WINOW_WIDTH, WINDOW_HEIGHT = 1280, 720
clock = pygame.time.Clock()

display_surface = pygame.display.set_mode((WINOW_WIDTH, WINDOW_HEIGHT))

# importing images 
ship_surf = pygame.image.load("graphics\spaceship.png").convert_alpha()
ship_surf = pygame.transform.scale(ship_surf, (80,90))
ship_y_pos = 600

background_surf = pygame.image.load("graphics\galaxy.jpg").convert_alpha()
background_surf = pygame.transform.scale(background_surf, (WINOW_WIDTH, WINDOW_HEIGHT))

# import text
font =  pygame.font.Font("graphics\subatomic.tsoonami.ttf" ,50)
text_surf = font.render("Spaaceeee", True,"White")

pygame.display.set_caption("Asteroid shooter V1")

while True:
    
    # input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # if event.type == pygame.
    
    # framerate limit
    clock.tick(120)
    
    # updates
    display_surface.blit(background_surf,(0,0))
    # display_surface.fill((0, 0, 0))
    display_surface.blit(ship_surf,(300,ship_y_pos))
    ship_y_pos -= 2
    display_surface.blit(text_surf, (WINOW_WIDTH/2 -150, WINDOW_HEIGHT-50))
    
    
    
    # show the frame to the player / update display surface
    pygame.display.update()