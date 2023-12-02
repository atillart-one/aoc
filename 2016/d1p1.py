c=0
for x in input().split(', '):c*=1j*(x[0]=='L'or-1);c+=int(x[1:])
print(abs(c.real)+abs(c.imag))
