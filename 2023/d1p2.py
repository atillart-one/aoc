from sys import stdin

lines = stdin.readlines()
sum = 0
nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for line in lines:
    for i in range(9):
        j = str(i+1)
        line = line.replace(nums[i], nums[i] + j + nums[i])
    s = [x for x in line if x.isdigit()]
    sum += int(s[0] + s[-1])
print(sum)
    
