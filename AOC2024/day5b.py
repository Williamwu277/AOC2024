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

    if not flag:

        # count the number of values that go after each number
        # a correctly ordered list should go x, x-1, x-2 ...
        scores = []

        for i in range(len(queries)):
            
            current_score = 0

            for j in range(len(queries)):

                if queries[i] in rule and queries[j] in rule[queries[i]]:

                    current_score += 1
        
            scores.append((current_score, queries[i]))
        
        # sort scores from largest to smallest
        # use list comprehension to only get the number, and not the score
        scores = sorted(scores)[::-1]
        scores = [nxt[1] for nxt in scores]

        answer += int(scores[len(scores)//2])

print(answer)