# AOC 2024 Day 7

'''
Remarks:
- I didn't optimize the recursion enough
- While making changes took a minute
- Actually running the code took almost 15 minutes
'''

n = int(input())


possible = False

# recursive function to try all possibilities
def rec(f, arr, eq):
    global possible

    # if there are enough operators, try it out
    if len(arr) == len(eq) + 1:

        v = arr[0]

        for i in range(1, len(arr)):

            # special case for the append operator
            if eq[i-1] == "||":

                v = int(str(v) + str(arr[i]))

            else:

                v = eval(str(v) + eq[i-1] + str(arr[i]))

        if v == f:

            possible = True

        return

    # recurse with all three operators
    rec(f, arr, eq + ['*'])
    rec(f, arr, eq + ['+'])
    rec(f, arr, eq + ["||"])


count = 0

for _ in range(n):

    # parse the input into result, and a list of numbers to operate on
    line = input().split(": ")
    res = int(line[0])
    rem = line[1].split()

    possible = False
    rec(res, rem, [])

    if possible:

        count += res


print(count)

