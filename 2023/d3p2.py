from sys import stdin

lines = stdin.readlines()
matrix = []

for line in lines:
    matrix.append(list(line.replace("\n","")))

m = len(matrix)
n = len(matrix[0])

star = 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] == '*':
            matrix[i][j] = f"*{star}"
            star += 1  

def adj(matrix, pos):
    a = set()
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            rangeX = range(0, m) 
            rangeY = range(0, n) 
            
            (newX, newY) = (pos[0]+dx, pos[1]+dy)
            
            if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                if '*' in matrix[newX][newY]:
                    a.add(matrix[newX][newY])
    return a

sum = 0
special = False
num = ''
stars = []
nums = []
gears = set()
for i in range(m):
    for j in range(n):
        if matrix[i][j].isdigit():
            num += matrix[i][j]
            gears = gears.union(adj(matrix, [i,j]))
            
        else:
            if num != '' and len(gears) != 0:
                stars.append(gears)
                nums.append(num)
            num = ''
            gears = set()

geardict = {}
for star in stars:
    geardict[list(star)[0]] = []
for i in range(len(nums)):
    geardict[list(stars[i])[0]].append(int(nums[i])) 
for key in geardict.keys():
    if len(geardict[key]) == 2:
        sum += geardict[key][0]*geardict[key][1]

print(sum)
