file = 'G:/python/adv_of_code/day2/d2_games.txt'
#константы
#RedCube = 12
#GreenCube = 13
#BlueCube = 14
RedCube = 0
GreenCube = 0
BlueCube = 0
NotPass = 0
total = 0
CubePower = 0
with open(file, 'r') as file:
    for line in file:
        #print(line)
        line = line.replace(';' , ',')
        line = line.replace('\n' , '')
        line = line.replace(':' , ',')
        tries = line.split(',')
        #print(tries)
        for value in tries:
            digits = ''.join(char for char in value if char.isdigit())
            if 'green' in value:
                if GreenCube < int(digits):
                    GreenCube = int(digits)
                    #NotPass = 1
                    #break
            if 'red' in value:
                if RedCube < int(digits):
                    RedCube = int(digits)
                    #NotPass = 1
                    #break
            if 'blue' in value:
                if BlueCube < int(digits):
                    BlueCube = int(digits)
                    #NotPass = 1
                    #break
            if 'Game' in value:
                GameNum = int(digits)
        if NotPass == 0:
            total += GameNum
        CubePower += RedCube * GreenCube * BlueCube
        RedCube = 0
        GreenCube = 0
        BlueCube = 0
        NotPass = 0    
        #cube = [string.split(',') for string in tries]
        #print(cube)
print(CubePower)
        