import turtle


def create_string(n, initial, F_rule, f_rule=None):
    if n == 0:
        return initial
    onestep = ''
    for character in initial:
        if character == 'F':
            onestep += F_rule
        if character == 'f':
            assert f_rule is not None
            onestep += f_rule
        else:
            onestep += character
    if n == 1:
        return onestep
    return create_string(n-1, onestep, F_rule, f_rule)


def draw_l_system(string, speed=10, angle=90, distance=100, start_pos=(0,0), start_heading=0):
    turtle.rIn [3]: def create_string(n, initial, F_rule, f_rule=None): 
   ...:     if n == 0: 
   ...:         return initial 
   ...:     onestep = '' 
   ...:     for character in initial: 
   ...:         if character == 'F': 
   ...:             onestep += F_rule 
   ...:         if character == 'f': 
   ...:             assert f_rule is not None 
   ...:             onestep += f_rule 
   ...:         else: 
   ...:             onestep += character 
   ...:     if n == 1: 
   ...:         return onestep 
   ...:     return create_string(n-1, onestep, F_rule, f_rule) 
eset()
    turtle.speed(speed)
    turtle.penup()
    turtle.goto(*start_pos)
    turtle.setheading(start_heading)
    turtle.pendown()
    stack_index = 0
    stack = []
    for character in string:
        if character == 'F':
            turtle.forward(distance)
        if character == 'f':
            turtle.penup()
            turtle.forward(distance)
            turtle.pendown()
        if character == '-':
            turtle.right(angle)
        if character == '+':
            turtle.left(angle)
        if character == '[':
            stack_index -= 1
            stack.append([turtle.pos(), turtle.heading()])
        if character == ']':
            turtle.penup()
            turtle.goto(stack[stack_index][0])
            turtle.pendown()
            turtle.setheading(stack[stack_index][1])
            stack_index += 1

    turtle.done()
