# AOC 2024 Day 4

n = int(input())
arr = []


for _ in range(n):

    arr.append(input())

count = 0

# look for X

for i in range(2, n):

    for j in range(2, len(arr[i])):

        first = arr[i-2][j-2] + arr[i-1][j-1] + arr[i][j] in ["MAS", "SAM"]
        second = arr[i-2][j] + arr[i-1][j-1] + arr[i][j-2] in ["MAS", "SAM"]

        if first and second:

            count += 1


print(count)