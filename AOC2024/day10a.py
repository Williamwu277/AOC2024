# AOC 2024 Day 10

# store the different trailends that each cell can reach in a set
arr = []
dp = []

# 59 by 59
n = int(input())
m = 0

# take input
for i in range(n):

    line = input()
    m = len(line)
    arr.append([])
    dp.append([])

    for j in range(m):

        arr[i].append(int(line[j]))
        dp[i].append(set())

# travel directions
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# start from 9 and iterate to 0
for num in range(9, -1, -1):

    for i in range(n):

        for j in range(m):
            
            # 9 is the answer to itself
            if arr[i][j] == 9:

                dp[i][j] = {(i, j)}

            # otherwise check all 4 directions for a path you can move to
            for k in range(4):

                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == arr[i][j] + 1 and arr[i][j] == num:

                    dp[i][j] = dp[i][j].union(dp[nx][ny])

count = 0

# count the answers
for i in range(n):

    for j in range(m):

        if arr[i][j] == 0:

            count += len(dp[i][j])
        

print(count)

