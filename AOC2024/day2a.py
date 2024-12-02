# AOC 2024 Day 2

# process each line of input as it comes

n = 1000
count = 0

for _ in range(n):

    li = list(map(int, input().split()))
    ascending = True
    descending = True

    # check for ascending
    for i in range(len(li)-1):

        if not (1 <= li[i+1] - li[i] <= 3):
            ascending = False

    # check for descending
    for i in range(len(li)-1):

        if not (-3 <= li[i+1] - li[i] <= -1):
            descending = False

    if ascending or descending:
        count += 1


print(count)

