# AOC 2024 Day 11

'''
Remarks:
- didn't see this solution at first
- the numbers branching off of each progenitor are independent of each other
- order doesn't matter and the number of unique values isn't all that great
- use a dictionary to store the number of times each value appears
'''


arr = list(map(int, input().split()))
dist = dict()

# should probably google if there is an easier way to do this
# update dictionary function
def insert(d, v, t):

    if v in d:

        d[v] += t

    else:

        d[v] = t


for i in range(len(arr)):

    insert(dist, arr[i], 1)


# do a smarter simulation of each round
for t in range(75):

    new_dist = dict()
    
    for k in dist:

        if k == 0:

            insert(new_dist, 1, dist[0])

        elif len(str(k)) % 2 == 0:

            s = str(k)
            old_value = int(str(s)[0:len(s)//2])
            nw_value = int(str(s)[len(s)//2:len(s)])
            insert(new_dist, old_value, dist[k])
            insert(new_dist, nw_value, dist[k])

        else:

            insert(new_dist, k*2024, dist[k])
    
    dist = new_dist


cnt = 0

for k in dist:

    cnt += dist[k]


print(cnt)

