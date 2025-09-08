## Usi9ng While Loop ##

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

number=5
while number>0:
    turn()
    number-=1
    
move()
