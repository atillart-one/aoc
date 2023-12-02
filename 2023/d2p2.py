from sys import stdin

lines = stdin.readlines()
index = 0
sum = 0
for line in lines:
    test = True 
    index += 1
    games = line.split(": ")[1].split("; ")
    games = [y.replace(", ", " ").replace("\n", "").split(" ") for y in games]
    red = 0
    blue = 0
    green = 0
    for game in games:
        for i in range(1, len(game), 2):
            if game[i] == 'red' and int(game[i-1]) > red:
                red = int(game[i-1]) 
            if game[i] == 'green' and int(game[i-1]) > green:
                green = int(game[i-1]) 
            if game[i] == 'blue' and int(game[i-1]) > blue:
                blue = int(game[i-1]) 
    sum += red*blue*green

print(sum)
    
