import random 

import pygame

def generate_new(top_height, player_y, total_rects, spacer, window, rect_width, win_height):
    rects = []
    for i in range(total_rects):
        top_height = random.randint(top_height - spacer, top_height + spacer)
        if top_height < 0:
            top_height = 0
        elif top_height > 300:
            top_height = 300
        top_rect = pygame.draw.rect(window, (0,255,0), [i * rect_width, 0, rect_width, top_height])
        bot_rect = pygame.draw.rect(window, (0,255,0), [i * rect_width, top_height + 300, rect_width, win_height])
        rects.append(top_rect)
        rects.append(bot_rect)
    return rects