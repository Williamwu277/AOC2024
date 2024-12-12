# AOC 2024 Day 12
from collections import deque
# import deque for queue-like utility

n = int(input())
m = 0
arr = []
vis = []

# read input
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
id = 1
answer = 0

# breadth first search on a grid
# if the cell hasn't been visited yet, start a new breadth first search
# only visit neighboring cells of the same value
for i in range(n):

    for j in range(m):
        
        if vis[i][j] == 0:
            
            cur_flag = arr[i][j]
            q = deque()
            q.append((i, j))
            vis[i][j] = id
            area = 0
            perimeter = 0

            # start breadth first search
            while len(q) != 0:

                cur = q[0]
                q.popleft()
                area += 1

                for k in range(4):

                    nx = cur[0] + dx[k]
                    ny = cur[1] + dy[k]

                    if 0 <= nx < n and 0 <= ny < m and vis[nx][ny] == 0 and arr[nx][ny] == cur_flag:
                    
                        # give each group a different id
                        q.append((nx, ny))
                        vis[nx][ny] = id

                    elif not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] != cur_flag:

                        perimeter += 1

            answer += area * perimeter
            id += 1


print(answer)

