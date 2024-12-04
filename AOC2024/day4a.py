# AOC 2024 Day 4

n = int(input())
arr = []


for _ in range(n):

    arr.append(input())


# look for horizontal

count = 0

for i in range(n):

    for j in range(3, len(arr[i])):

        if arr[i][j-3: j+1] in ["XMAS", "SAMX"]:
            
            count += 1

# look for vertical

for j in range(len(arr[0])):

    for i in range(3, n):

        if arr[i-3][j] + arr[i-2][j] + arr[i-1][j] + arr[i][j] in ["XMAS", "SAMX"]:

            count += 1


# look for horizontal

for i in range(3, n):

    for j in range(3, len(arr[i])):

        if arr[i-3][j-3] + arr[i-2][j-2] + arr[i-1][j-1] + arr[i][j] in ["XMAS", "SAMX"]:

            count += 1
        
        if arr[i-3][j] + arr[i-2][j-1] + arr[i-1][j-2] + arr[i][j-3] in ["XMAS", "SAMX"]:

            count += 1


print(count)