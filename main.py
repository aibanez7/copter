import random 

import pygame 

import functions

pygame.init()

win_width = 1000
win_height = 600
window = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption('Copter')
font = pygame.font.Font('freesansbold.ttf', 20)
fps = 60 
timer = pygame.time.Clock()
new_map = True
map_rects = []
rect_width = 10
total_rects = win_width//rect_width
spacer = 10
player_x = 100
player_y = 300
flying = False
y_speed = 0
gravity = 0.3
map_speed = 2
score = 0
high_score = 0
active = True
image = pygame.image.load('helicopter.png')
copter = pygame.transform.scale(image, (60, 60))

def move_rects(rects):
    global score
    for i in range(len(rects)):
        rects[i] = (rects[i][0] - map_speed, rects[i][1], rect_width, rects[i][3])
        if rects[i][0] + rect_width < 0:
            rects.pop(1)
            rects.pop(0)
            top_height = random.randint(rects[-2][3] - spacer, rects[-2][3] + spacer)
            if top_height < 0:
                top_height = 0
            elif top_height > 300:
                top_height = 300
            rects.append((rects[-2][0] + rect_width, 0, rect_width, top_height))
            rects.append((rects[-2][0] + rect_width, top_height + 300, rect_width, win_height))
            score += 1
    return rects

'''def check_colision(map_rects, player_circle, active):
    for i in range(len(map_rects)):
        if player_circle.colliderect(map_rects[i]):
            active = False
    return active'''

run = True 
while run:
    window.fill((0,0,0))
    timer.tick(fps)

    if new_map:
        top_height = random.randint(0,300)
        player_y = top_height + 150
        map_rects = functions.generate_new(top_height, player_y, total_rects, spacer, window, rect_width, win_height)
        new_map = False
    functions.draw_map(map_rects, window, win_width, win_height)

    player_circle = functions.draw_player(window, player_x, player_y, copter)

    if active:
        player_y, y_speed = functions.move_player(player_y, y_speed, flying, gravity)
        map_rects = move_rects(map_rects)

    active = functions.check_colision(map_rects, player_circle, active)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flying = True
            if event.key == pygame.K_RETURN:
                if not active:
                    new_map = True 
                    active = True
                    y_speed = 0 
                    map_speed = 2
                    if score > high_score: 
                        high_score = score 
                    score = 0
        if event.type == pygame.KEYUP:
            if event.key  == pygame.K_SPACE:
                flying = False
    
    map_speed = 2 + score//50
    spacer = 10 + score//100

    window.blit(font.render(f'Score: {score}', True, (0,0,0)), (20, 15))
    window.blit(font.render(f'High Score: {high_score}', True, (0,0,0)), (20, 565))
    if not active:
        window.blit(font.render(f'Press Enter to Restart', True, (0,0,0)), (300, 15))
        window.blit(font.render(f'Press Enter to Restart', True, (0,0,0)), (300, 565))
    pygame.display.flip()


pygame.quit()
