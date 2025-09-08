## Using For Loop##

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(5):
    turn()
    
move()
