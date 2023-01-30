import pygame
import sys


def laser_update(laser_list, speed=300):
    for rect in laser_list:
        rect.y -= speed *dt
        if rect.bottom < 0:
            laser_list.remove(rect)

pygame.init()
WINOW_WIDTH, WINDOW_HEIGHT = 1280, 720
clock = pygame.time.Clock()

display_surface = pygame.display.set_mode((WINOW_WIDTH, WINDOW_HEIGHT))

# importing images 
ship_surf = pygame.image.load("graphics\spaceship.png").convert_alpha()
ship_surf = pygame.transform.scale(ship_surf, (80,90))
ship_rect = ship_surf.get_rect(midbottom=(WINOW_WIDTH/2, WINDOW_HEIGHT-100))
print(ship_rect)

laser_surf = pygame.image.load("graphics\laser.png").convert_alpha()
laser_surf = pygame.transform.rotate(laser_surf, angle=90)
laser_surf = pygame.transform.scale(laser_surf, (35,45))
laser_list =[]
# laser_rect = laser_surf.get_rect(midbottom=(ship_rect.midtop[0] + 90, ship_rect.midtop[1]))

background_surf = pygame.image.load("graphics\galaxy.jpg").convert_alpha()
background_surf = pygame.transform.scale(background_surf, (WINOW_WIDTH, WINDOW_HEIGHT))

# import text
font =  pygame.font.Font("graphics\subatomic.tsoonami.ttf" ,50)
text_surf = font.render("Spaaceeee", True,"White")
text_rect = text_surf.get_rect(midbottom=(WINOW_WIDTH/2, WINDOW_HEIGHT - 20))



pygame.display.set_caption("Asteroid shooter V1")
while True:
    
    # framerate limit
    dt = clock.tick(120)/1000
    
    # input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            laser_rect = laser_surf.get_rect(midbottom=ship_rect.midtop)
            laser_list.append(laser_rect)
            
            
    
    # mouse position
    move_ship_pos = pygame.mouse.get_pos()[0]
    mouse_buttons = pygame.mouse.get_pressed()
    
    
    
    if move_ship_pos > 20 and move_ship_pos < WINOW_WIDTH - 20 and ship_rect.centerx != move_ship_pos:
        if move_ship_pos >= ship_rect.centerx:
            
           if move_ship_pos - ship_rect.centerx > 4 or move_ship_pos - ship_rect.centerx < -4:
                ship_rect.centerx += 4 
           else:
                ship_rect.centerx += 1
        else:
            if move_ship_pos - ship_rect.centerx > 4 or move_ship_pos - ship_rect.centerx < -4:
               
                ship_rect.centerx -= 4 
            else:
                ship_rect.centerx -= 1
            
    
    laser_update(laser_list)
    # Not perfect but rn ensures consistant speed of the game despite frame rates
    
    
    # updates
    display_surface.blit(background_surf,(0,0))
    # display_surface.fill((0, 0, 0))
    
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, (255, 255, 255), text_rect.inflate(25,25), 7, 5)
    
    # if mouse_buttons[0] or shoot_flag:
        
    #     print("passed")
    #     display_surface.blit(laser_surf, laser_rect)
    #     shoot_flag = True
    for rect in laser_list:
        display_surface.blit(laser_surf, rect) 
    display_surface.blit(ship_surf, ship_rect)
    
    # show the frame to the player / update display surface
    pygame.display.update()
    print(len(laser_list))