import sys
import pygame
from pygame.locals import*

pygame.init()

RED = (255,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (105,105,105)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = SCREEN_WIDTH

# Function that draws a white screen
def draw_screen():
    pygame.display.set_caption("Chessboard")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.fill(WHITE)
    return screen

# Function that draws the chessboard squares
def draw_chessboard_squares(screen):
    counter = 0
    square_size = SCREEN_WIDTH / 8
    for row in range(8):
        for col in range(8):
            if counter % 2 == 1:
                 pygame.draw.rect(screen, GREY, (col*square_size, row*square_size, square_size, square_size))
            counter += 1
        counter += 1

# Function that runs and waits until user quits
def run():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    screen = draw_screen()
    draw_chessboard_squares(screen)
    pygame.display.update()
    run()
    pygame.quit()


    
