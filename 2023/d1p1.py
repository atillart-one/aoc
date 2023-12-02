from sys import stdin

lines = stdin.readlines()
sum = 0
for line in lines:
    s = [x for x in line if x.isdigit()]
    sum += int(s[0] + s[-1])
print(sum)
    
