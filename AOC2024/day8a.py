# AOC 2024 Day 8
import math


n = int(input())
m = 0


# for each frequency store an array of the coordinates that it appears at
antenna = dict()
arr = []
vis = []


for i in range(n):

    arr.append(input())
    vis.append([])
    m = len(arr[-1])

    for j in range(m):

        vis[i].append(False)

        if arr[i][j] != '.':

            if arr[i][j] in antenna:

                antenna[arr[i][j]].append((i, j))

            else:

                antenna[arr[i][j]] = [(i, j)]


count = 0

# for each point, go through all the frequencies
# within each frequency check all combinations of the antennas to see if 
# its valid with this point
for i in range(n):

    for j in range(m):

        for nxt in antenna:

            for l in range(len(antenna[nxt])):

                for k in range(l+1, len(antenna[nxt])):

                    f = antenna[nxt][l]
                    s = antenna[nxt][k]

                    dist1 = math.sqrt((f[0] - i) ** 2 + (f[1] - j) ** 2)
                    dist2 = math.sqrt((s[0] - i) ** 2 + (s[1] - j) ** 2)

                    slope1 = (f[0] - i, f[1] - j)
                    slope2 = (s[0] - i, s[1] - j)
                    
                    # make sure to avoid division by 0
                    if slope1[0] == 0: 

                        slope1 = "inf"

                    else:

                        slope1 = slope1[1] / slope1[0]

                    if slope2[0] == 0:

                        slope2 = "inf"

                    else:

                        slope2 = slope2[1] / slope2[0]

                    if (dist1 == 2 * dist2 or dist1 * 2 == dist2) and slope1 == slope2:

                        vis[i][j] = True


# count answers
for i in range(n):

    for j in range(m):

        if vis[i][j]:

            count += 1


print(count)
                    
                    