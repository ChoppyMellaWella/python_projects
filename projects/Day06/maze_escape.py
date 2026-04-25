def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if wall_in_front() and wall_on_right():
        turn_left()
    elif front_is_clear() and wall_on_right():
        move()
        if right_is_clear() and not at_goal():
            turn_right()
            move()
            if right_is_clear():
                turn_right()
                move()
    elif wall_in_front() and right_is_clear():
        turn_left()
    else:
        move()