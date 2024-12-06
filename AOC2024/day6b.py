# AOC 2024 Day 6
import sys

'''
Remarks:
- total program was O(n^4)
- a bit hefty, takes some time to run fully
- the algorithm goes into an infinite loop if all 4 directions the guard is facing are walls
'''

# need to increase the recursion limit for python to avoid error
sys.setrecursionlimit(1000000)

# 130 lines of input
n = int(input())
m = 0

# direction to travel in order
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

arr = []
vis = []
posx, posy = 0, 0

for i in range(n):

    line = input()
    arr.append([])
    vis.append([])
    m = len(line)

    # visited array stores the directions you've faced at each cell
    for j in range(m):

        vis[i].append([])
        arr[i].append(line[j])

    # find the position of the guard
    for j in range(m):

        if line[j] == "^":
            posx = i
            posy = j

answer = 0
repeated = False

# dfs function to simulate the path of the guard
# max number of steps should be n * m * 4
def dfs(cx, cy, d):
    global repeated
    
    # next cell reached
    nx = cx + dx[d]
    ny = cy + dy[d]

     # if out of the map, end the recursion
    if nx < 0 or nx >= n or ny < 0 or ny >= m:

        return
    
    # if reached a wall, recurse with a different direction
    if arr[nx][ny] == '#':

        dfs(cx, cy, (d+1)%4)
        return
    
    # if reached an exact same spot, infinite loop
    # increment score by 1
    if d in vis[nx][ny]:

        repeated = True
        return
    
    # mark down on visited array and move to next cell
    vis[nx][ny].append(d)
    dfs(nx, ny, d)

# simulate replacing each cell with a wall
for i in range(n):

    for j in range(m):

        # avoid existing walls or starting cell
        if arr[i][j] != '#' and arr[i][j] != "^":

            arr[i][j] = '#'

            # clear the visited array for each time
            for l in range(n):

                for k in range(m):

                    vis[l][k].clear()
            
            # put the initial cell in the visited array and dfs
            vis[posx][posy].append(0)
            repeated = False
            dfs(posx, posy, 0)

            # replace back with empty space
            arr[i][j] = '.'

            if repeated:

                answer += 1


print(answer)

