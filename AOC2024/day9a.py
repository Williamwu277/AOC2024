# AOC 2024 Day 9


# terminal couldn't take the line of input with how long it was :(
line = input()
arr = []
cnt = 0

# convert into long form
for i in range(len(line)):

    if i % 2 == 0:

        for j in range(int(line[i])):

            arr.append(cnt)

        cnt += 1

    else:

        for j in range(int(line[i])):

            arr.append('.')


# do two pointers from start and end to move 
ptr = 0
bptr = len(arr)-1

for i in range(bptr, 0, -1):

    # could use better coding norms but I was rushing
    if arr[i] == '.':

        continue

    if ptr >= i:

        break

    while arr[ptr] != '.' and ptr < len(arr)-1:

        ptr += 1

    arr[ptr] = arr[i]
    arr[i] = '.'
    ptr += 1

# calculate score
score = 0

for i in range(len(arr)):

    if arr[i] != '.':

        score += int(arr[i]) * i


print(score)
    
    