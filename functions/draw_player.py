import pygame

def draw_player(window, player_x, player_y, copter):
    #draw circle hitbox and image
    player = pygame.draw.circle(window, (0,0,0), (player_x, player_y), 20)
    window.blit(copter, (player_x - 40, player_y - 30))
    return player