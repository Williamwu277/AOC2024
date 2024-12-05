# AOC 2024 Day 5

# 1176 different rules, 187 things to check
n = 1176
m = 187

rule = dict()

# take in the rule inputs
for _ in range(n):

    a, b = input().split("|")
    
    if a in rule:

        rule[a].append(b)
    
    else:

        rule[a] = [b]

input() # get rid of the new line
answer = 0

# read the queries
for _ in range(m):

    queries = input().split(",")
    flag = True

    # just check whether or not the following numbers require you to come before it
    for i in range(len(queries)):

        for j in range(i+1, len(queries)):

            if queries[j] in rule and queries[i] in rule[queries[j]]:

                flag = False

    if flag:
        answer += int(queries[len(queries)//2])


print(answer)