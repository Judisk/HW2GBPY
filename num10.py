import random

N=int(input())

reshka = random.randrange(N)
orel=N-reshka

print(reshka,orel)

if reshka > orel:
    count = int(orel)
else:
    count = int (reshka)

print(count)