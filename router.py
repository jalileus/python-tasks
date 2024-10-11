# Time limit	1 second
# Memory limit	64.0 MB
# Input	stdin or input.txt
# Output	stdout or output.txt

# The task is to calculate the coordinates of the new router which is symmetrical to the original router
# relative to the column's center and verify that the column is not inside or on the border of the router.

# Input format:
# Six integers separated by line breaks:
# xa, ya - coordinates of one corner of the original router (point A).
# xb, yb - coordinates of the opposite corner of the original router (point B).
# xc, yc - coordinates of the column center.

# Output format:
# 1. If the column is inside or on the border of the router, print "False".
# 2. Otherwise, print the coordinates of the symmetrical points of the new router relative to the column.

# Sample Input:
# 1
# 0
# 8
# 3
# 6
# 0

# Sample Output:
# False

# Sample Input:
# 3
# 0
# 0
# 7
# 4
# 4

# Sample Output:
# 5
# 8
# 8
# 1


def CheckWindow(l, b, a):
    j = 0
    s = ""
    for j in range(b):
        s += l[j]
    if len(s) > a - 1:
        print()


a = int(input())
if a > 100:
    a = 100
elif a < 1:
    a = 1
b = int(input())
if b > 60:
    b = 60
elif b < 1:
    b = 1
count = 0
l = []
while count <= 1000:
    word = input()
    l.append(word)
    if l[count] == "0":
        break
    count += 1
l.remove("0")
j = 0
i = 0
space = 0
s = ""
while i < count:
    for j in range(b):
        if i >= count:
            break
        else:
            s += l[i]
            if len(s) > a - space:
                break
            else:
                print(l[i], end=" ")
                i += 1
                space += 1
    print()
    s = ""
    space = 0
