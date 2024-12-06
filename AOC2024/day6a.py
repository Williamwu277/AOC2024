# AOC 2024 Day 6
import sys

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
    for j in range(len(line)):

        vis[i].append([])
        arr[i].append(line[j])
    
    # find the position of the guard
    for j in range(len(line)):
        
        if line[j] == "^":
            posx = i
            posy = j

# starting node 
arr[posx][posy] = 'X'
vis[posx][posy].append(0)
count = 1

# dfs function to simulate the path of the guard
def dfs(cx, cy, d):
    global count
    
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
    if d in vis[nx][ny]:

        return
    
    # mark down the X. If first time visiting cell, add 1
    arr[nx][ny] = 'X'

    if len(vis[nx][ny]) == 0:

        count += 1

    # mark down on visited array and move to next cell
    vis[nx][ny].append(d)
    dfs(nx, ny, d)


# start the dfs
dfs(posx, posy, 0)
print(count)
