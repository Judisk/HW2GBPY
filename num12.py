import random

sum = int(input())
multiplie=int(input())
y=0
x=0

while x<=1001:
    x+=1
    y=sum-x
    if (y>0 and y<1000):
        if (y*x)==multiplie:
            error=0
            break;
        else:
            error=1
    y=0
if error==0:
    print(x, y)
else:
    print("Такая комбинация невозможна")
"""print(ySum,xSum)

for i in range(len(xSum)):
    for j in range(len(ySum)):
        r=xSum[i]*ySum[j]
        if r==multiplie:
            mpxlist.append(xSum[i])
            mpylist.append(ySum[j])

print(mpylist,mpxlist)

if """