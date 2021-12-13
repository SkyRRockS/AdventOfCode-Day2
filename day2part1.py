INPUT_S='''\
forward 8
forward 3
forward 8
down 6
forward 3
up 6
down 3
down 8
down 5
down 1
down 4
up 4
'''

#Day 2 advent of code 2021 :
#part 1 : at the start we are at 0,0 and we move like the guidelines.
#And then we multiply the x and the y together;

commands = [str(line) for line in INPUT_S.splitlines()];



posX = 0
posY = 0

for i in range(len(commands)) :
    if commands[i][0] == 'f' :
        move = int(commands[i][8])
        posX += move
    if commands[i][0] == 'd' :
        move = int (commands[i][5])
        posY += move
    if commands[i][0] == 'u' :
        move = int (commands[i][3])
        posY -= move
print(posX*posY)
