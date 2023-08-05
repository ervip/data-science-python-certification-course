"""
A Robot moves in a Plane starting from the origin point (0,0). The robot can move 
UP, DOWN, LEFT, or RIGHT. The trace of Robot movement is as given following:
    UP 5
    DOWN 3
    LEFT 3
    RIGHT 2
The numbers after directions are steps. 

Write a program to compute the distance current position after a sequence of movements.
"""

from math import sqrt


def distance(p1, p2):
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


if __name__ == '__main__':
    print((
        "Let's start our journey... Currently, We are at (0,0)\n"
        "Input Format: Direction(UP, DOWN, LEFT, RIGHT) Steps(Number)\n"
        "Write 'exit' to calculate result and exit the program."
    ))

    x, y = 0, 0

    while True:
        cmd = input().strip()
        
        if cmd == "exit":
            break
        
        direction, steps = cmd.split()
        steps = int(steps)
        
        if direction == "UP":
            y += steps
        elif direction == "DOWN":
            y -= steps
        elif direction == "LEFT":
            x -= steps
        elif direction == "RIGHT":
            x += steps
        else:
            print("Invalid input, Please enter again...\n")

    print(f"Distance between (0,0) and ({x}, {y}): {distance((0,0), (x,y))}")