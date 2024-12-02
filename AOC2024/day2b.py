# AOC 2024 Day 2

# process each line of input as it comes

n = 1000
count = 0

for _ in range(n):

    li = list(map(int, input().split()))
    ascending = descending = 0
    flag = False

    # remove each index and check for validity
    for i in range(len(li)):

        new_li = li[0:i] + li[i+1:len(li)]
        ascending = descending = True

        # check for ascending
        for j in range(len(new_li)-1):

            if not (1 <= new_li[j+1] - new_li[j] <= 3):
                ascending = False

        # check for descending
        for j in range(len(new_li)-1):

            if not (-3 <= new_li[j+1] - new_li[j] <= -1):
                descending = False

        if ascending or descending:
            flag = True

    if flag:
        count += 1


print(count)

