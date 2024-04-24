def move_player(player_y, y_speed, flying, gravity):
    if flying:
        y_speed += gravity
    else:
        y_speed -= gravity
    player_y -= y_speed   
    return player_y, y_speed