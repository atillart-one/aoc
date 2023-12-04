from sys import stdin
from functools import lru_cache
lines = stdin.readlines()
sum = 0
scores = []

for line in lines:
    _, line = line.replace("\n", "").split(": ")
    win, current = line.split("|")
    win = [x for x in win.split(" ") if x != '']
    current = [x for x in current.split(" ") if x != '']
    tmp = 0
    for x in win:
        if x in current:
            tmp += 1
    scores.append(tmp)

cards = [i for i in range(len(scores))]
cards.reverse()


@lru_cache(maxsize=1000)
def cards_returned(c):
    cards = [c]
    sum = 1
    while len(cards) > 0:
        a = int(cards.pop(0))
        for i in range(a+1, a+scores[a]+1):
             sum += cards_returned(i)
    return(sum)

for i in cards:
    sum += cards_returned(i)

print(sum)
