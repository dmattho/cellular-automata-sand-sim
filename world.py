import pygame
import numpy as np
from pixel import *
import random

class World():
    def __init__(self, screen_width, screen_height, screen):

        self.cell_size = 16
        self.cell_rows, self.cell_columns = screen_width//self.cell_size, screen_height//self.cell_size
        self.pix_size = self.cell_size
        self.screen = screen

        #initialize cell grid
        self.cell_grid = np.zeros((self.cell_rows, self.cell_columns))

       

        
        
    # Calculate where to place 1 in the grid list
    def create_pix(self, click_pos):
        #Get cell coordinates from the click. click_pos[0] = x coordinate, click_pos[1] = y coordinate
        cell_pos_x, cell_pos_y = click_pos[0]//self.cell_size, click_pos[1]//self.cell_size
        if cell_pos_x < self.cell_rows and cell_pos_y < self.cell_columns:
            self.cell_grid[cell_pos_x][cell_pos_y] = 1

            random_number = random.randint(1,10)
            
            """for gen in range(random_number):
                random_x = random.randint(0,3)
                random_y = random.randint(0,3)
                add_or_subtract = random.randint(0,1)
                if add_or_subtract == 1:
                    if cell_pos_x + random_x < self.cell_rows and cell_pos_y + random_y < self.cell_columns:
                        self.cell_grid[cell_pos_x + random_x][cell_pos_y+ random_y] = 1
                elif add_or_subtract == 0:
                    if cell_pos_x - random_x < self.cell_rows and cell_pos_y - random_y < self.cell_columns:
                        self.cell_grid[cell_pos_x - random_x][cell_pos_y] = 1"""

            


            


    def update_world(self):
        counter_speed = 100

        for x in range(self.cell_rows):
            for y in range(self.cell_columns):
                if self.cell_grid[x][y] == 1 :
                
                    x_cell_coordinate, y_cell_coordinate = (x * self.cell_size) + (self.cell_size // 2), (y * self.cell_size) + (self.cell_size // 2)
                    self.draw_pixel(x_cell_coordinate, y_cell_coordinate)
                    
                    


    #TO DO: SEE IF I CAN MAKE THIS MORE EFFICIENT
    def update_next_position(self):
        next_grid = np.zeros((self.cell_rows, self.cell_columns))
        for x in range(self.cell_rows):
            for y in range(self.cell_columns):
                current = self.cell_grid[x][y]
                
                if current == 1:
                    if y + 1 < self.cell_columns:
                        next = self.cell_grid[x][y+1]
                        if next ==0:
                            next_grid[x][y + 1] = 1
                        else:
                            next_grid[x][y] = 1
                        
                    else:
                        next_grid[x][y] = 1
                        
        self.cell_grid = next_grid

                            
 

        
        


                    
    def draw_pixel(self, x, y):
        type = 0

        if type == 0:
            sand = Sand()
            #pygame.draw.circle(self.screen, sand.color, [x, y], self.pix_size)
            rect = pygame.Rect(x, y, self.pix_size, self.pix_size)
            pygame.draw.rect(self.screen, sand.color, rect)



        
