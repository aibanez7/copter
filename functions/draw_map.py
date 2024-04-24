import pygame 

def draw_map(rects, window, win_width, win_height):
    for i in range(len(rects)):
        pygame.draw.rect(window, (0,255,0), rects[i])
    pygame.draw.rect(window, (0,0,0), [0, 0, win_width, win_height], 10)