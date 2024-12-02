# AOC 2024 Day 1

# read input

n = 1000  # points
l1, l2 = [], []

for _ in range(n):

    a, b = map(int, input().split())
    l1.append(a)
    l2.append(b)

# sort both lists

l1.sort()
l2.sort()

# find the answer

answer = 0
for i in range(n):

    answer += abs(l1[i] - l2[i])


print(answer)
