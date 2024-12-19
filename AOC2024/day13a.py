# AOC 2024 Day 13


# 320 inputs
n = int(input())
s = 0

for _ in range(n):

    # parse input
    a = input().split('+')
    b = input().split('+')
    p = input().split('=')
    input()

    aX = int(a[1].split(',')[0])
    aY = int(a[2])

    bX = int(b[1].split(',')[0])
    bY = int(b[2])

    pX = int(p[1].split(',')[0])
    pY = int(p[2])

    best = -1

    # iterate through all combinations
    for i in range(100):

        for j in range(100):

            if aX * i + bX * j == pX and aY * i + bY * j == pY:

                if best == -1:

                    best = 3 * i + j
                
                else:

                    best = min(best, 3 * i + j)
    
    if best != -1:
        
        s += best

print(s)
