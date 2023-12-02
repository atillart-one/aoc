from sys import stdin

lines = stdin.readlines()
index = 0
sum = 0
for line in lines:
    test = True 
    index += 1
    games = line.split(": ")[1].split("; ")
    games = [y.replace(", ", " ").replace("\n", "").split(" ") for y in games]
    for game in games:
        for i in range(1, len(game), 2):
            if game[i] == 'red' and int(game[i-1]) > 12:
                test = False 
            if game[i] == 'green' and int(game[i-1]) > 13:
                test = False 
            if game[i] == 'blue' and int(game[i-1]) > 14:
                test = False 
    if test:
        sum += index

print(sum)
    
