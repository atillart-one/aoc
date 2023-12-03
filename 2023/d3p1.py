from sys import stdin

lines = stdin.readlines()
matrix = []
for line in lines:
    matrix.append(list(line.replace("\n","")))

m = len(matrix)
n = len(matrix[0])

def adj(matrix, pos):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            rangeX = range(0, m) 
            rangeY = range(0, n) 
            
            (newX, newY) = (pos[0]+dx, pos[1]+dy)
            
            if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                 if not matrix[newX][newY].isdigit() and matrix[newX][newY] != '.':
                    return True    
    return False

sum = 0
special = False
num = ''
for i in range(m):
    for j in range(n):
        if matrix[i][j].isdigit():
            num += matrix[i][j]
            special = (special or adj(matrix, [i, j]))
        else:
            if num != '' and special:
                sum += int(num)                        
            num = ''
            special = False
print(sum)
