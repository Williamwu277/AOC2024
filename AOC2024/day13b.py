# AOC 2024 Day 13


# 320 inputs
n = int(input())
s = 0

for _ in range(n):

    # parse the input
    a = input().split('+')
    b = input().split('+')
    p = input().split('=')
    input()

    aX = int(a[1].split(',')[0])
    aY = int(a[2])

    bX = int(b[1].split(',')[0])
    bY = int(b[2])

    pX = 10000000000000 + int(p[1].split(',')[0])
    pY = 10000000000000 + int(p[2])

    # idea: express as a systems of equations to solve
    # aX * i + bX * j = pX
    # aY * i + bY * j = pY
    # aX * aY * i + bX * aY * j = pX * aY
    # aX * aY * i + bY * aX * j = pY * aX
    # bX * aY * j - bY * aX * j = pX * aY - pY * aX
    # (bX * aY - bY * aX) * j = pX * aY - pY * aX
    # j = (pX * aY - pY * aX) / (bX * aY - bY * aX)
    jN = pX * aY - pY * aX
    jD = bX * aY - bY * aX
    
    if jN % jD != 0:
        continue

    j = jN // jD
    iN = pX - bX * j
    iD = aX

    if iN % iD != 0:
        continue

    # aX * i = pX - bX * j
    # i = (pX - bX * j) / aX
    i = iN // iD
    s += 3 * i + j


print(s)

