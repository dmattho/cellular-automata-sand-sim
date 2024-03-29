import pygame
import numpy as np
pygame.init()
from world import World
#Framerate
clock = pygame.time.Clock()

#declare resolution of screen
screen_width, screen_height = 1280, 720

#declaring running bool for loop
running = True

#initialize window
screen = pygame.display.set_mode((screen_width, screen_height))
    
#colors
screen_color = pygame.Color(156,188,187)
sand_color = pygame.Color(163,147,130)

#Call world Class
world = World(screen_width,screen_height, screen)


#main loop
while running:
 
    clock.tick(60)
    screen.fill(screen_color)
    #screen.fill(screen_color)
    current_mouse_pos = pygame.mouse.get_pos()
    pygame.display.set_caption(f"({current_mouse_pos[0]}, {current_mouse_pos[1]})")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            
    if pygame.mouse.get_pressed()[0] == 1:
        world.create_pix(current_mouse_pos)
            
            

    world.update_world()
    

    pygame.display.update()
    
    world.update_next_position()

    



pygame.quit()