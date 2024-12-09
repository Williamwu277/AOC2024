# AOC 2024 Day 9

'''
Remarks:
- Today took a bit too long to debug and read the question
- Code is also a little dirty
'''

line = input()
arr = []
cnt = 0

for i in range(len(line)):

    # store in tuples of (id, 0 for file 1 for space, length)
    if i % 2 == 0: # file

        arr.append((cnt, 0, int(line[i])))
        cnt += 1

    else:

        arr.append((0 , 1, int(line[i])))


# iterate from back to front
# loop from left to right
# if you can slot it there, slot it there
# O(N^2)
for i in range(len(arr)-1, 0, -1):

    if arr[i][1] == 0:

        for j in range(i):

            if arr[j][1] == 1 and arr[j][2] == arr[i][2]:

                arr[j], arr[i] = arr[i], arr[j]
                break

            elif arr[j][1] == 1 and arr[j][2] > arr[i][2]:

                arr[j] = (0, 1, arr[j][2] - arr[i][2])
                arr.insert(j, (arr[i][0], 0, arr[i][2]))
                i += 1
                arr[i] = (0, 1, arr[i][2])
                break
        
        # make sure to clean up the blocks so that there are no
        # two space-blocks side by side
        for j in range(len(arr)-1, 0, -1):

            if arr[j][1] == arr[j-1][1] == 1:

                arr[j-1] = (0, 1, arr[j][2] + arr[j-1][2])
                arr.pop(j)
                i -= 1


score, pos = 0, 0

for i in range(len(arr)):

    for j in range(arr[i][2]):

        score += arr[i][0] * pos
        pos += 1


print(score)
    
