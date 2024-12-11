# AOC 2024 Day 11

'''
Remarks:
- not a very smart solution
- simulates the process exactly as described
- uses a linked list to efficiently insert into list
'''


arr = list(map(int, input().split()))

# linked list node class
class LinkedNode:

    def __init__(self, value, next):

        self.value = value
        self.next = next


root = LinkedNode(arr[0], None)
cur = root

# create the original linked list
for i in range(1, len(arr)):

    nw = LinkedNode(arr[i], None)
    cur.next = nw
    cur = nw

# simulate 25 times
for _ in range(25):

    cur = root

    # iterate through the linked list
    while cur != None:
        
        # depending on value, change behavior
        if cur.value == 0:

            cur.value = 1
            cur = cur.next

        # insert a new node in between current node and next node
        elif len(str(cur.value)) % 2 == 0:

            s = str(cur.value)
            old_value = int(str(s)[0:len(s)//2])
            nw_value = int(str(s)[len(s)//2:len(s)])
            nw_node = LinkedNode(nw_value, cur.next)
            cur.value = old_value
            cur.next = nw_node
            cur = nw_node.next

        else:

            cur.value *= 2024
            cur = cur.next


cur = root
a = set()

# count the number of nodes
while cur != None:

    a.add(cur.value)
    cur = cur.next


print(len(a))

