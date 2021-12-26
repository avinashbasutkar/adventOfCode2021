directions = [x.strip() for x in open("2directionCommands.txt")]

forward = 0
down = 0
up = 0

for i in directions:
    if i.startswith("f"):
        forward += int(i[-1])
    elif i.startswith("d"):
        down += int(i[-1])
    else:
        up += int(i[-1])

horizontalPosition = forward
depth = down - up

position = horizontalPosition * depth
