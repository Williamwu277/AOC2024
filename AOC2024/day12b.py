# AOC 2024 Day 12
from collections import deque
# import deque for queue-like utility

n = int(input())
m = 0
arr = []
vis = []

for i in range(n):

    line = input()
    m = len(line)
    arr.append([])
    vis.append([])

    for j in range(m):

        arr[i].append(line[j])
        vis[i].append(0)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dd = ['r', 'l', 'u', 'd']
id = 1
answer = 0

# do bfs like in part a
# to count the number of sides, note that each cell has 4 borders
# for each border store its coordinates
# for each border direction u, d, l, r if they are in a straight line it is one side
# count it as such
for i in range(n):

    for j in range(m):
        
        if vis[i][j] == 0:

            cur_flag = arr[i][j]
            q = deque()
            q.append((i, j))
            vis[i][j] = id
            area = 0
            sides = 0

            direct = {
                'd':[],
                'u':[],
                'l':[],
                'r':[]
            }

            while not len(q) == 0:

                cur = q[0]
                q.popleft()
                area += 1

                for k in range(4):

                    nx = cur[0] + dx[k]
                    ny = cur[1] + dy[k]

                    if 0 <= nx < n and 0 <= ny < m and vis[nx][ny] == 0 and arr[nx][ny] == cur_flag:

                        q.append((nx, ny))
                        vis[nx][ny] = id

                    elif not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] != cur_flag:

                        # for each border direction store the cell coordinates
                        # store based its X or Y depending on direction 
                        if dd[k] in 'rl':

                            direct[dd[k]].append((ny, nx))

                        else:

                            direct[dd[k]].append((nx, ny))

            # sort all the border cell coordinates
            for nxt in direct:

                direct[nxt] = sorted(direct[nxt])
            

            for nxt in direct:

                preA = -2
                preB = -2

                for s in range(len(direct[nxt])):

                    # if the border is on a different line than the next, increment the side count
                    if direct[nxt][s][0] != preA:

                        sides += 1

                    # if there is a break in the same line, increment the side count
                    elif direct[nxt][s][1] != preB + 1:
                        
                        sides += 1

                    preA = direct[nxt][s][0]
                    preB = direct[nxt][s][1]
            
            answer += area * sides
            id += 1


print(answer)

