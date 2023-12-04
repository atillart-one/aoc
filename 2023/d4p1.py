from sys import stdin

lines = stdin.readlines()
sum = 0
for line in lines:
    _, line = line.replace("\n", "").split(": ")
    win, current = line.split("|")
    win = [x for x in win.split(" ") if x != '']
    current = [x for x in current.split(" ") if x != '']
    tmp = 0
    for x in win:
        if x in current:
            tmp += 1
    if tmp != 0: sum += 2**(tmp-1)
    print(tmp)
print(sum)
