def check_colision(map_rects, player_circle, active):
    for i in range(len(map_rects)):
        if player_circle.colliderect(map_rects[i]):
            active = False
    return active