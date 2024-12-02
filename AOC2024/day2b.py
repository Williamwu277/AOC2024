# AOC 2024 Day 1

# read input

n = 1000  # points
l1, l2 = [], []

for _ in range(n):

    a, b = map(int, input().split())
    l1.append(a)
    l2.append(b)

# find how many times each number is in the right list

mp = dict()
for i in range(n):

    if l2[i] in mp:
        mp[l2[i]] += 1
    else:
        mp[l2[i]] = 1

# find the answer

answer = 0
for i in range(n):

    if l1[i] in mp:
        answer += l1[i] * mp[l1[i]]


print(answer)
