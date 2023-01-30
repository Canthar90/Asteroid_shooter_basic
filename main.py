import pygame
import sys
import random



def laser_update(laser_list, speed=300):
    for rect in laser_list:
        rect.y -= round(speed *dt)
        if rect.bottom < 0:
            laser_list.remove(rect)
            
            
def display_score():
    score_text = f'Score: {pygame.time.get_ticks() // 1000}'
    text_surf = font.render(score_text, True,"White")
    text_rect = text_surf.get_rect(midbottom=(WINOW_WIDTH/2, WINDOW_HEIGHT - 20))
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, (255, 255, 255), text_rect.inflate(25,25), 7, 5)
    

def laser_timer(can_shoot, duration=500):
    if not can_shoot:
        current_time = pygame.time.get_ticks()
        if current_time - shoot_time > duration:
            can_shoot = True
            
    return can_shoot


def meteor_update(meteor_list, speed=250):
    for rec, direction in meteor_list:
        
        rec.center += direction * speed * dt
        # rec.y += round(speed * dt)
        if rec.bottom > WINDOW_HEIGHT:
            meteor_list.remove((rec,direction))

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

# meteor object
meteor_surf = pygame.image.load(r"graphics\asteroid.png").convert_alpha()
meteor_surf = pygame.transform.scale(meteor_surf, (70,70))
meteor_list = []

# import text
font =  pygame.font.Font("graphics\subatomic.tsoonami.ttf" ,50)

# laser timer setup
can_shoot = True
shoot_time = None 

# meteor timer
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 300)


pygame.display.set_caption("Asteroid shooter V1")

#import sound
laser_sound = pygame.mixer.Sound(r'sounds\blaster-2-81267.mp3')
laser_sound.set_volume(0.3)
explosion_sound = pygame.mixer.Sound(r"sounds\blast-37988.mp3")
backgorund_music = pygame.mixer.Sound(r"sounds\nostro5-73932.mp3")
backgorund_music.set_volume(0.7)
backgorund_music.play(-1)

while True:
    
    # framerate limit
    dt = clock.tick(120)/1000
    
    
    
    # input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
            laser_rect = laser_surf.get_rect(midbottom=ship_rect.midtop)
            laser_list.append(laser_rect)
            
            # play laser sound
            laser_sound.play()
            
            # timer
            can_shoot = False
            shoot_time = pygame.time.get_ticks()
            
            
        if event.type == meteor_timer:
            # rando position
            x_pos = random.randint(-100, WINOW_WIDTH + 100)
            y_pos = random.randint(-100, -50)
            meteor_rect = meteor_surf.get_rect(midbottom=(random.randint(0,WINOW_WIDTH), y_pos))
            
            #create a random direction
            direction = pygame.math.Vector2(random.uniform(-0.5, 0.5),1)
            
            # creating rect
            meteor_list.append((meteor_rect, direction))
            
                
            
    
    
        
    
    
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
            
    
    
    # updates
    display_surface.blit(background_surf,(0,0))
    
    
    display_score()
    laser_update(laser_list)
    can_shoot = laser_timer(can_shoot, 350)
    
    meteor_update(meteor_list)
   
    for rect in laser_list:
        display_surface.blit(laser_surf, rect) 
    display_surface.blit(ship_surf, ship_rect)
    
    for rec, direction in meteor_list:
        display_surface.blit(meteor_surf, rec)
    
    # meteor ship collisions
    for meteor_tuple in meteor_list:
        meteor_rect = meteor_tuple[0]
        if ship_rect.colliderect(meteor_rect):
            pygame.quit()
            sys.exit()
            
    # laser meteor collisions
    for meteor_tuple in meteor_list:
        meteor_rect = meteor_tuple[0]
        for laser_rect in laser_list:   
            if laser_rect.colliderect(meteor_rect):
                laser_list.remove(laser_rect)
                meteor_list.remove(meteor_tuple)
                explosion_sound.play()
            
    
    # show the frame to the player / update display surface
    pygame.display.update()